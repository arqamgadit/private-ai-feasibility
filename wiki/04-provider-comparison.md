# 4. Provider comparison

[Back to wiki home](README.md)

Cost, content-policy limits and privacy terms for each option considered. **Short tables below were refreshed 15 November 2026** alongside the full value-offering pass. Deep write-ups:

- [Page 10 — value offering comparison](10-provider-value-offering.md) (every provider on the evaluation list)
- [Page 9 — GPU cloud research](09-gpu-cloud-provider-value-research.md) (17 self-host candidates)

Re-check before signing anything.

"Content limits" matters because the product is lightly filtered. Most providers allow frank, refusal-free text on lawful topics; nearly all ban sexually explicit content. Our policy is to block sexual content anyway (see [page 5](05-content-policy-and-trust-safety.md)), but a provider's wording still decides how much risk sits on our account.

## Pay-per-token model APIs

| Provider | Cost | Content limits | Privacy |
|---|---|---|---|
| **DeepInfra** | Cheapest serious host. Llama 3.3 70B about **$0.10 / $0.32** per 1M tokens | Terms silent on adult content; illegal use banned. Lowest contractual risk of the API set | **Zero retention by default**, written into terms. Pin FP8 where FP4 variants exist |
| **Groq** | GPT-OSS 120B **$0.15 / $0.60**; Llama 70B often enterprise / sales. Very fast (LPU) | Bans *illegal* sexual content and NCII; not a blanket lawful-adult ban | No retention by default. Abuse logs ≤30 days unless ZDR in Data Controls |
| **Novita** | Llama 3.3 70B **$0.135 / $0.40** | Aug 2026 AUP: “is sexually explicit” prohibited | ToS claims ZDR by default |
| **Together AI** | Llama 3.3 ~**$1.04 / $1.04**; DeepSeek Flash class ~**$0.30 / $1.20** | Bans pornography and obscene content. Also bars sending sensitive personal data | Stores prompts **by default**. Zero retention must be switched on at organization level |
| **Fireworks AI** | GPT-OSS 120B **$0.15 / $0.60**; DeepSeek Flash **$0.30 / $1.20** | Strictest: customers must guarantee inputs contain no nudity or sexually suggestive content | Zero retention by default, except Responses API (30 days unless `store=false`) |
| **OpenRouter** | Pass-through pricing | Depends on the underlying provider | Adds another company in the prompt path; not ideal as the main route for a privacy product |

## Confidential / private AI products

| Provider | Cost | Content limits | Privacy |
|---|---|---|---|
| **Phala / RedPill** | CVM from **$0.06/hr**; GPU TEE from **$4.40/hr**. Token API e.g. GLM 5.3 Flash **$0.15 / $0.50**; uncensored Qwen3.8 27B **$0.30 / $1.50** | Lawful use; uncensored SKUs in catalog; no explicit adult ban found in public terms checked | TEE + attested no-log compose; optional E2EE. Venice TEE partner |
| **Tinfoil** | Chat **$20/mo**. API e.g. GPT-OSS 120B **$0.15 / $0.60**; Llama 3.3 70B **$1.75 / $2.75**; DeepSeek V4.1 Flash **$0.60 / $1.45** | AUP bans CSAM, NCII of real people without consent, weapons, fraud — **no blanket adult ban**. Chat has in-enclave safeguards; **API is unmoderated** | Attested SEV-SNP/TDX + confidential GPUs; SDK verifies every connection; API no retention after response |
| **Privatemode** | Free 5M tokens once; PAYG from ~**€0.65 / 1M output**; Business **€250/mo** | Bans illegal / harmful / **offensive** — enterprise tone, not uncensored | Client-verified E2EE + EU confidential compute; no prompt retention after request |
| **Maple AI** | Pro **$20/mo**; Max **$100/mo** | CSAM / weapons / harassment bans; hosts an “uncensored” DeepSeek SKU without Venice-style NSFW marketing | Client E2EE + attested enclaves |
| **Nillion nilAI** | Credits; public rate card sparse | Builder/infra positioning | NVIDIA TEE + signed responses; HTTPS into TEE (not full client E2EE) |
| **Venice.ai** | Pro **$18/mo**; higher Max tiers | Markets legal NSFW; bans CSAM / non-consensual likeness | Modes: Anonymous → Private → TEE → E2EE. **Competitor** |
| **NEAR AI Cloud** | Per token, encryption included (see Venice stack) | Check before contract | Hardware enclaves with signed proof. Venice partner with Phala |

## GPU clouds for self-hosting

H100 on-demand prices per GPU-hour (15 Nov 2026); reserved contracts are cheaper. Full AUP and fit notes in [page 9](09-gpu-cloud-provider-value-research.md).

| Provider | H100 cost | Content limits | Privacy |
|---|---|---|---|
| **Seeweb** | ~**€1.89** (~$2.09) | Confirm Italian ToS; customer responsible for legality | We control the stack (EU) |
| **Vultr** | **$2.30** | Obscene / offensive | We control the stack |
| **Denvr** | **$2.45** | AUP (Jul 2023): illegal incl. **CSAM**; mining banned; **no porn/obscene ban**. Cloud ToS (Jul 2025) adds timesharing/commercial-exploit limits — Sales Order carve-out needed. Deep dive: [page 9 §12](09-gpu-cloud-provider-value-research.md#12-denvr-dataworks) | We control the stack |
| **NexGen / Hyperstack** | $2.50–3.20 (reserved from $1.75) | **No adult/porn ban.** General AUP: illegal/abusive/fraudulent/violent. Extra AI Model rule: no misleading/harmful/discriminatory/defamatory generation; **monitor** + suspend on **perceived** breach. England & Wales / LCIA. Deep dive: [page 9 §10](09-gpu-cloud-provider-value-research.md#10-nexgen-cloud-hyperstack) | We control the stack (VMs). AI Studio is a separate managed lane |
| **GMI Cloud** | from $2.60 | AUP English body not retrieved | We control the stack |
| **RunPod Secure** | PCIe ~$2.89 | **Bans pornography and graphic adult content**, lifetime bans | Fine on Secure Cloud; **avoid Community** |
| **Bitdeer** | ~$2.90 (tracker) | “Obscene” | We control the stack |
| **Gcore** | ~$2.61–3.12 | Inappropriate / unlawful | We control the stack |
| **Scaleway** | PCIe ~€2.86; SXM ~€6.61 | Unlawful porn / sexualized (FR) | We control the stack (EU sovereign) |
| **Crusoe** | $3.90 → **$4.50** (1 Dec 2026) | Illegal / CSAM / NCEI; no blanket adult ban found | We control the stack |
| **DigitalOcean** | $4.41 ($3.26 reserved) | Unlawful pornography | We control the stack |
| **Nebius** | $4.50 | “Obscene” (vague); fine for our policy | We control the stack |
| **Lambda** | $4.59 8× SXM (from 16 Nov 2026) | Obscene / indecent / illegal pornography | We control the stack |
| **Verda** (ex-DataCrunch) | $5.24 (spot $2.62) | Schedule 1 AUP bans **“obscene”** (+ unlawful/harmful). No named porn ban but greyer than Denvr/Seeweb. Schedule 5 for managed AI. Finland law. Deep dive: [page 9 §9](09-gpu-cloud-provider-value-research.md#9-verda-formerly-datacrunch--verified-rename) | We control the stack |
| **Together dedicated** | Clusters $3.99; DMI $5.49 | Obscene / pornography ban | Dedicated replicas / bare metal; serverless stores by default |
| **CoreWeave** | $6.16 (commit up to −60% quote) | Most permissive of the big clouds: bans only *unlawful* pornography | We control the whole stack |
| **AWS** | ~$7.9 SageMaker / ~$5.97 Capacity Block | Strict Responsible AI | Fine for app plane; too expensive for primary inference |
| **Modal** | ~$3.95, billed per second | Indecent and obscene content | Fine |
| **Vast.ai** | Cheapest marketplace | Varies by host | Weak: unknown machine owners. Don't use for user prompts |

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
| **Brave Search API** | $5 per 1,000 searches, $5 free credit a month | None relevant for search results policy | Default query logs ≤90 days; **enterprise ZDR** available — buy it for Private mode |
| **Exa, Tavily, Serper** | Alternatives to Brave | Not yet checked | Not yet checked |

## Frontier models ("Anonymous" mode)

| Provider | Cost | Content limits | Privacy |
|---|---|---|---|
| **OpenAI API (ZDR)** | About $1–50 per 1M tokens by model | Strict Model Spec; limited erotica contexts; high refusals | ZDR by **prior approval**; default abuse logs ~30 days; no training on API data by default |
| **Anthropic API (ZDR)** | Haiku from ~$0.10/$0.50; Sonnet ~$2/$10; Opus ~$4/$20 | Explicit ban on sexually explicit / erotic chats for API **and** end users of integrations | ZDR via sales; some covered models not ZDR-eligible |
| **Google (Anonymous path)** | Check current | Strict | Sees and may keep prompts unless a separate enterprise path applies |

## Still to check

- Written ZDR / no-training addenda for every launch-stack provider.
- GMI Cloud full English AUP; Seeweb Italian adult clause.
- E2B, Browserbase and remaining search-API terms.
- Reserved GPU quotes before board packs that cite $/hr.
