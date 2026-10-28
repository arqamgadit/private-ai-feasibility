# 3. Hosting strategy

[Back to wiki home](README.md)

## Recommendation

Use a **hybrid that changes over time**: start on managed zero-retention inference providers, then move steady, predictable traffic onto GPUs we rent and run ourselves once volume justifies it. Keep managed providers for traffic spikes, niche models and overflow.

The architecture copies Venice's: a no-logging proxy we control, routing each request to one of four privacy levels (see [page 1](01-product-overview.md#privacy-modes)).

## What decides it

1. **Privacy is the product.** Every managed provider we route through sees user prompts, so we need zero-data-retention and no-training terms in writing. Self-hosting is the only setup with full control, which is a reason to get there eventually.
2. **Acceptable-use policies.** Many model APIs ban sexual content, and some ban anything "obscene". Breaking those terms can get an account shut off overnight. Check each policy against our content stance before building on it (see [page 4](04-provider-comparison.md)).
3. **Self-hosting no longer wins on price for popular models.** Serverless open-model prices are very low (DeepSeek V4 Flash about $0.14 / $0.28 per 1M tokens). An H100 at about $3/hour serving around 2,500 tokens per second at 60% utilisation works out to roughly $0.55 per 1M tokens. Self-hosting pays off through privacy, policy control, and the ability to run our own fine-tunes.
4. **Uncensored fine-tunes are usually not offered by API providers.** Versions of open models with refusals removed are typically only available on a dedicated deployment or our own GPUs. That pushes the flagship model toward self-hosting earlier than cost alone would.

## Phased plan

| Phase | When | Hosting | Why |
|---|---|---|---|
| 1. Launch | First 6–12 months | Pay-per-token APIs plus a few dedicated endpoints | No ops team needed, instant scaling, lets us learn which models users want |
| 2. Hybrid | Inference spend above roughly $50–100k/month, or steady usage | Reserved GPUs for the main 2–3 models; managed providers for overflow and long-tail models | Own GPUs only beat per-token pricing when they're busy most of the time (roughly 60%+) |
| 3. Scale | Year 3+ | Mostly self-hosted, possibly partly in-region in the UAE; managed providers as backup | Lowest cost per token, full privacy control, data residency |

## Recommended stack

| Layer | Launch phase | Scale phase |
|---|---|---|
| No-logging proxy | Our own gateway (LiteLLM or custom). Optionally on a Phala confidential VM so users can verify it keeps no logs | Same |
| Default "Private" text models | DeepInfra | Self-host main 2–3 models on CoreWeave or Nebius reserved GPUs; DeepInfra for overflow |
| Fast agent steps | Groq with zero retention switched on | Same, or self-hosted |
| Pro "verifiable privacy" mode (TEE / E2EE) | NEAR AI Cloud (per token) | Phala confidential GPUs on reserved contracts |
| Images | fal.ai | Self-hosted Flux or SDXL on our own GPUs |
| Optional frontier models | Direct provider APIs through our proxy, labelled "Anonymous" | Same |
| Agent sandboxes | E2B (code), Browserbase (browser) | Self-hosted E2B (open source) on our own servers |
| Web search | Brave Search API | Same |
| Backup for clearly safe-for-work traffic (Teams, coding) | Fireworks or Together | Same |

## Software stack for self-hosting

| Need | Tools |
|---|---|
| Text model serving | vLLM or SGLang (TensorRT-LLM for peak throughput) |
| Image serving | ComfyUI or diffusers |
| Orchestration | Kubernetes with an autoscaler |
| Routing between providers | LiteLLM gateway or a custom router, so traffic can move without code changes |

## Cost per token rule of thumb

```text
cost per 1M tokens = GPU $/hour / (tokens per second x 3600 x utilisation) x 1,000,000
```

Example: $3/hour H100, 2,500 tokens/s, 60% busy gives about $0.56 per 1M tokens. Below about 50% utilisation, serverless is usually cheaper.
