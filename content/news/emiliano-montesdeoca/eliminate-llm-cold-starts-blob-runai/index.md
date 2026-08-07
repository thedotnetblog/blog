---
title: "Stop Wasting GPU Time: Stream LLM Weights Directly from Azure Blob Storage"
description: "Run:AI Model Streamer cuts LLM cold starts from minutes to seconds by skipping the local disk hop. A practical look at performance, setup, and autoscaling."
date: 2026-09-04
author: "Emiliano Montesdeoca"
tags: [azure-blob-storage, llm-inference, vllm, runai, performance]
slug: eliminate-llm-cold-starts-blob-runai
---

Original source: [Eliminate LLM Cold starts: Load models up to 6x Faster with Azure Blob Storage and Run:AI Model Streamer](https://devblogs.microsoft.com/azure-sdk/eliminate-llm-cold-starts-load-models-up-to-6x-faster-with-azure-blob-storage-and-runai-model-streamer/)

## The Real Cost of Cold Starts

If you're serving LLMs on Azure, you already know the pain: autoscaling adds a replica, but it sits idle while model weights copy from blob storage to disk and then into GPU memory. Every second of idle GPU time is money on the bill, and a queue is building under the traffic that triggered the scale-out.

In the source benchmark, a 232.8 GiB model with the default vLLM loader took roughly 3 to 5 minutes to load on a Standard_ND96isr_H100_v5 VM. That delay can recur when an autoscaler adds a replica, a spot VM is reclaimed, a rolling deployment restarts a process, or a serving system swaps models.

The default loader performs two sequential steps: download the model from Azure Blob Storage to local disk, then read it from disk into GPU memory. Run:AI Model Streamer removes the local disk hop. It streams model data through CPU memory into GPU memory, reducing the unavailable window in the benchmark from minutes to seconds.

## Performance That Fits the Autoscaler

The comparison used an 8x NVIDIA H100 machine streaming from Premium block blob storage in the same region. The results were:

- Meta-Llama-3.1-8B-Instruct, 14.99 GiB: 3.61 seconds with the streamer versus 15.48 seconds with the default loader, about 4.3x faster.
- GPT-OSS-120B, 60.8 GiB: 12.76 seconds versus 42.29 seconds, about 3.3x faster.
- Qwen3.5-122B-A10B, 232.8 GiB: 37.14 seconds versus 225.57 seconds, about 6.1x faster.

The streamer held a steady 80 Gbps in the benchmark. The default loader peaked around 40 Gbps and dropped as low as 10 Gbps on the largest model. The most important result is not just the speedup: the largest model loaded within one typical autoscaler cycle with the streamer, while the default loader did not.

That changes the failure pattern. Existing replicas have less time to absorb the whole spike, queues are less likely to grow past gateway or client timeouts, and the next capacity decision has a better chance of seeing the new replica online. These are benchmark results, not a guarantee for every storage account or network path, so measure your own model and region.

## Quick Start with vLLM or SGLang

Both vLLM and SGLang can stream weights from Azure Blob Storage through an `az://` URI. First place SafeTensors weights in a blob container. The source uses `azcopy` for upload and passes the storage account separately with `AZURE_STORAGE_ACCOUNT_NAME`.

For vLLM:

```bash
uv pip install vllm[runai]
export AZURE_STORAGE_ACCOUNT_NAME="<your_account_name>"
vllm serve az://<your-container>/models/llama-3.1-8b \
  --load-format runai_streamer
```

For a multi-GPU deployment, the source shows tensor parallelism and distributed streaming:

```bash
vllm serve az://<your-container>/models/llama-3.1-405b \
  --load-format runai_streamer \
  --tensor-parallel-size 8 \
  --model-loader-extra-config '{"distributed": true, "concurrency": 32}'
```

SGLang follows the same pattern:

```bash
uv pip install "sglang[runai]" --prerelease=allow
python -m sglang.launch_server \
  --model-path az://<your-container>/models/llama-3.1-8b \
  --load-format runai_streamer \
  --served-model-name llama-3.1-8b
```

Authentication uses `DefaultAzureCredential`, which supports local `az login` and managed identity environments such as AKS, Azure ML, and VMs. That makes the serving path compatible with normal Azure identity practices rather than requiring a storage key in a startup script.

## Tuning and Caveats

`RUNAI_STREAMER_CONCURRENCY` controls concurrent I/O threads and defaults to 8 for object storage. The source suggests values such as 32 or 64 when the backend and network can use more parallelism. `RUNAI_STREAMER_MEMORY_LIMIT` controls the CPU buffer cap.

SafeTensors weights are required. If a model only contains `.bin` files, convert or obtain a compatible format before testing the streamer. The 6x result is also a benchmark result on specific hardware, model sizes, storage, and region placement. Verify throughput, memory pressure, and failure behavior in your own environment.

For .NET developers, the serving change is usually behind the application boundary. A .NET service may continue calling vLLM or SGLang over HTTP or gRPC, but shorter cold starts can change timeout and retry behavior. Revisit those settings after measuring the new startup profile; a client that was tuned for multi-minute loading may now retry too aggressively during a different failure mode.

## What to Do Next

1. Measure current model load time and the autoscaler cadence for one representative workload.
2. Upload a SafeTensors model to a same-region Premium blob account in a test environment.
3. Compare the default loader and Run:AI Model Streamer under cold-start conditions.
4. Tune concurrency only after checking network and CPU-buffer behavior.
5. Update application timeouts and retry policies based on observed serving behavior.

The useful idea is simple: remove an unnecessary copy from object storage to local disk. For large models, that small architectural change can decide whether autoscaling feels like recovery or like another incident.