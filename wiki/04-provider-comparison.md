# 4. Provider comparison

[Back to wiki home](README.md)

Cost, content-policy limits and privacy terms for each option considered. **Prices and policies were checked on 26 October 2026** from provider pricing pages, terms of service and public price trackers. Re-check before signing anything.

"Content limits" matters because the product is lightly filtered. Most providers allow frank, refusal-free text on lawful topics; nearly all ban sexually explicit content. Our policy is to block sexual content anyway (see [page 5](05-content-policy-and-trust-safety.md)), but a provider's wording still decides how much risk sits on our account.

## Pay-per-token model APIs

| Provider | Cost | Content limits | Privacy |
|---|---|---|---|
| **DeepInfra** | Cheapest. Llama 3.3 70B about $0.10 input / $0.32 output per 1M tokens | Terms say nothing about adult content; only illegal use is banned. Lowest risk of the API providers | Zero retention by default, written into the terms. Some models run at lower precision (FP4), so pin FP8 versions |
| **Groq** | Llama 3.3 70B $0.59 / $0.79 per 1M tokens; very fast | Bans *illegal* sexual content and non-consensual imagery; lawful exceptions can be requested | No retention by default. Abuse logs can be kept up to 30 days unless you opt out in Data Controls |
| **Cerebras** | Very fast; rates not public for these models | Bans pornographic and obscene content; vague "objectionable" clause | Stores no prompts or outputs |
| **Together AI** | Llama 3.3 70B $0.88 per 1M; DeepSeek V4 Flash $0.14 / $0.28 | Bans pornography and obscene content. Also bars sending sensitive personal data | Stores prompts **by default**. Zero retention must be switched on at organization level |
| **Fireworks AI** | Similar to Together | Strictest: customers must guarantee inputs contain no nudity or sexually suggestive content | Zero retention by default, except the Responses API (30 days unless `store=false`) |
| **OpenRouter** | Pass-through pricing | Depends on the underlying provider | Adds another company in the prompt path; not ideal as the main route for a privacy product |

## Confidential computing

| Provider | Cost | Content limits | Privacy |
|---|---|---|---|
| **NEAR AI Cloud** | Per token, encryption included. Qwen 3.8 27B $0.04 / $1.35; DeepSeek V3.2 $1.10 / $1.10; Kimi K3 $3.30 / $16.50 | Not yet checked | Hardware-isolated enclaves with signed proof on every response. A Venice partner |
| **Phala** | H100 $3.08/hour ($2.38 with 24-hour minimum); H200 $5.50/hour; confidential VMs from $0.06/hour | Not yet checked | Same enclave approach. Venice's other partner. Good host for the proxy |

## GPU clouds for self-hosting

H100 on-demand prices per GPU-hour; reserved contracts are cheaper.

| Provider | H100 cost | Content limits | Privacy |
|---|---|---|---|
| **CoreWeave** | $6.16 | Most permissive of the big clouds: bans only *unlawful* pornography (child abuse material, non-consensual content) | We control the whole stack |
| **Nebius** | $4.50 | Bans "obscene" content (vague); fine for our policy | We control the stack |
| **Lambda** | $3.99 (8-GPU machine) | Bans obscene and indecent content and illegal pornography | We control the stack |
| **Crusoe** | $3.90 | Content terms not visible in the policy text checked | We control the stack |
| **RunPod** | $2.69–3.49 | **Bans pornography and graphic adult content**, with lifetime bans | Fine on Secure Cloud; avoid Community Cloud (third-party machines) |
| **Modal** | $3.95, billed per second | Bans indecent and obscene content | Fine |
| **Vast.ai** | Cheapest marketplace | Varies by host | Weak: unknown machine owners. Don't use for user prompts |
| **DediGPU, RedSwitches** (bare metal) | Fixed monthly rental | Explicitly allow legal adult content (RedSwitches only in legal jurisdictions such as Amsterdam) | Strong: the machine is ours. Not needed under our current policy |
| **AWS / Azure / GCP** | $6.88–12.29 | Strict | Fine, but too expensive for inference. Use for the web app and databases |
| **Core42 / UAE data centres** | Quote only | UAE law applies, so safe-for-work only | Local data residency and low latency for Gulf users |
| **Akash, io.net** (decentralised) | Varies | Varies | Uneven reliability; overflow only |

## Images

| Provider | Cost | Content limits | Privacy |
|---|---|---|---|
| **fal.ai** | Per image, roughly in line with the $0.004 model assumption | Formal adult-content policy, but the safety filter is on by default and turning it off needs account approval. Bans child abuse material, non-consensual imagery and deepfakes of real people | Scans every request with hash matching and OpenAI's moderation model, so it sees all prompts |
| **Replicate** | Per run | Check per model | Sees prompts |
| **Self-hosted Flux / SDXL** | GPU cost only | Our own policy | Full control |

## Agent tools

| Provider | Cost | Content limits | Privacy |
|---|---|---|---|
| **E2B** (code sandboxes) | About $0.17/hour for 2 CPUs and 4 GB, billed per second; Pro plan $150/month | Sandboxes run tools rather than generate content; terms not yet checked | Short-lived sandboxes; open source, so self-hostable |
| **Browserbase** (browser sandboxes) | $0.10–0.12 per browser-hour; Startup plan $99/month | Terms not yet checked; browsing adult sites may be restricted | Sees every page the agent visits; get a data processing agreement |
| **Steel, Hyperbrowser** | Alternatives to Browserbase | Not yet checked | Not yet checked |
| **Daytona** | Alternative to E2B | Not yet checked | Not yet checked |
| **Brave Search API** | $5 per 1,000 searches, $5 free credit a month | None relevant | Privacy-first search with no user profiling |
| **Exa, Tavily, Serper** | Alternatives to Brave | Not yet checked | Not yet checked |

## Frontier models ("Anonymous" mode)

| Provider | Cost | Content limits | Privacy |
|---|---|---|---|
| **OpenAI / Anthropic / Google** | About $2–25 per 1M tokens | Strict; refuse many "uncensored" requests | They see and may keep prompts, which is why Venice labels these "Anonymous" |

## Still to check

- NEAR AI and Phala acceptable-use policies.
- E2B, Browserbase and search-API terms.
- Zero-retention contract terms (not just website settings) for every provider in the launch stack.
