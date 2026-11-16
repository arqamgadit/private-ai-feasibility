# 10. Hosted private & uncensored AI — value offering comparison

[Back to wiki home](README.md)

Full comparison of every provider on the evaluation list, checked **15 November 2026**. Companion pages: short cost/AUP table in [page 4](04-provider-comparison.md); deep GPU IaaS detail in [page 9](09-gpu-cloud-provider-value-research.md). Interactive filterable matrix: [Private AI provider value offering](https://cursor.com/canvas/store-6d9201ae-7bc3-4f73-868f-a4721e776fc1/51ed0eb0-5eaf-491e-819c-e0f54a868022).

**How to read “uncensored” here:** our product wants **low refusals on lawful topics** and blocks sexual content ([page 5](05-content-policy-and-trust-safety.md)). Provider AUPs that ban pornography still fit us; they only become a problem if enforcement treats frank lawful text as “obscene.” Venice-style NSFW marketing is treated as a **competitor pattern to avoid**, not a requirement.

**Value dimensions (same for every row):**

| Dimension | What we score |
|---|---|
| Privacy | Contractual ZDR vs hardware TEE / client E2EE vs “we own the VM” |
| Content / refusal posture | AUP adult/obscene language; model refusals for frontier APIs |
| Economics | Public token or H100 rates (indicative) |
| Catalog / capability | Models, speed, regions, ops maturity |
| Role for us | Launch partner, Teams/EU, Competitor, Overflow, Avoid |

**Compliance depth** (interactive table on the canvas — filterable):

### Uncensored depth (U0–U5)

| Level | Meaning |
|---|---|
| **U0** | Strict frontier refusals (Model Spec / erotic bans) |
| **U1** | Moderated product (assistant safety; no 18+ mode) |
| **U2** | Open weights but hard sexual / obscene ToS or warranty |
| **U3** | Open weights; AUP silent or legality-scoped; no abliterated SKUs |
| **U4** | Abliterated / uncensored SKUs offered, or self-host full control |
| **U5** | Markets unrestricted / legal NSFW brand |

Our product targets lawful low-refusal (**~U3–U4**) while blocking sexual content in product policy. **U5** (Venice-style branding) is what we avoid.

### No-logs / no-retention depth (R0–R5)

| Level | Meaning |
|---|---|
| **R0** | Stores prompts by default (ZDR is opt-in) |
| **R1** | Short abuse / safety retention (~30 days) by default |
| **R2** | Contractual ZDR — operator still sees plaintext during inference |
| **R3** | You own the VM — you control logging |
| **R4** | TEE attested — operator designed not to read prompts |
| **R5** | Client E2EE + TEE — platform cannot decrypt |

Private mode launch can live on **R2** (DeepInfra/Groq). Pro TEE/E2EE needs **R4–R5**. Self-host is **R3**.

### Snapshot (selected)

| Provider | Models (highlights) | U | R |
|---|---|---|---|
| Phala / RedPill | DeepSeek, Kimi, Qwen, GLM, Llama, GPT-OSS + **uncensored** Qwen/Gemma SKUs | U4 | R4 |
| Tinfoil | GPT-OSS, DeepSeek V4.1 Flash, Llama 3.3 70B, Gemma 4, GLM 5.3, Kimi; containers for custom | U3 | R4 |
| Privatemode | GLM-5.3, GPT-OSS, STT, OCR | U2 | R5 |
| Maple | DeepSeek Flash **+ Uncensored**, GLM, Kimi, GPT-OSS, Llama | U4 | R5 |
| Venice | Broad open + frontier Anonymous + media | U5 | R5 |
| DeepInfra | Very large open catalog (Llama/DeepSeek/Qwen/GLM/…) | U3 | R2 |
| Groq | GPT-OSS, Qwen, Llama (often enterprise) | U3 | R2 |
| Together | Broad open + fine-tunes | U2 | R0→R2 if ZDR on |
| Fireworks / Novita | Broad open | U2 | R2 |
| OpenAI / Anthropic ZDR | Closed frontier only | U0 | R2 |
| GPU Primary (CoreWeave, etc.) | Any you deploy | U3–U4 (AUP-capped) | R3 |

Prices and policies move; re-check before contracting.

---

## Executive stack recommendation

| Layer | Pick | Why |
|---|---|---|
| Private open-weight (launch) | **DeepInfra** + **Groq** | Default ZDR; DeepInfra cheapest + AUP silent on adult; Groq LPU speed + legality-scoped sexual AUP |
| TEE / E2EE (Pro) | **Phala** (+ NEAR path as Venice does); **Tinfoil** as attested API overflow; **Privatemode** for EU/Teams | Attested enclaves; Phala also rents confidential VMs for our no-log proxy; Tinfoil API is unmoderated with SDK attestation |
| Search (agent) | **Brave Search API** with enterprise ZDR | Privacy-positioned index; default API keeps queries ~90 days without ZDR |
| Frontier “Anonymous” | **OpenAI ZDR** / **Anthropic ZDR** (approved orgs) | Capability only; high refusals; label honestly |
| Self-host reserved | **CoreWeave / Nebius** + **Vultr / Denvr / Seeweb** | Control + competitive H100; see [page 9](09-gpu-cloud-provider-value-research.md) |
| Do not build Private mode on | Together / Fireworks / Novita serverless as default; RunPod Community; AWS as primary GPU | Retention defaults, hard sexual ToS warranties, marketplace hosts, or cost |

---

## Cohort A — Confidential / private AI products

Consumer or API products whose pitch is **privacy by construction** (TEE, E2EE, no-store), not raw GPU rental.

### Phala Network / RedPill

| Field | Detail |
|---|---|
| **Category** | Confidential compute (Phala) + multi-TEE private AI gateway / chat (RedPill) |
| **Value proposition** | Attested Intel TDX CVMs and GPU TEE inference; RedPill unifies Phala, NEAR, Tinfoil, Chutes, Privatemode behind one OpenAI-compatible API with verification |
| **Privacy** | TEE + encrypted client→enclave paths; no-log claimed as attested compose property; optional E2EE. Upstream ZDR for some backends is contractual |
| **Content** | Phala ToS: lawful use; no explicit adult ban found. Catalog includes **uncensored** SKUs (e.g. Qwen3.8 27B Uncensored, Gemma-4 Uncensored) |
| **Economics** | CVM from **$0.06/hr**; GPU TEE from **$4.40/hr**. Token API e.g. GLM 5.3 Flash **$0.15/$0.50**, Qwen3.8 27B Uncensored **$0.30/$1.50**, gpt-oss-120b **$0.15/$0.60**. RedPill Pro chat **$50/mo** |
| **Differentiators** | Rentable confidential proxy VMs; Venice already uses Phala for TEE; explicit uncensored TEE models |
| **Fit** | **Launch partner** for TEE/E2EE and attested proxy hosting. RedPill as optional multi-provider router, not required |
| **Risks** | Higher $/token than DeepInfra; attestation diligence (TCB freshness); uncensored labels clash with clean UAE brand if shown to end users |
| **Sources** | [phala.com/pricing](https://phala.com/pricing), [redpill.ai/pricing](https://redpill.ai/pricing), [phala.com/terms](https://phala.com/terms) |

### Tinfoil

| Field | Detail |
|---|---|
| **Category** | Confidential inference API + chat + confidential containers |
| **Value proposition** | OpenAI-compatible private inference on AMD SEV-SNP / Intel TDX with confidential NVIDIA GPUs; client SDKs verify attestation on every connection against open-source builds and public transparency logs |
| **Privacy** | Plaintext designed inaccessible to Tinfoil / cloud hosts during normal operation. **API: no retention** of prompts/responses after return (temporary encrypted enclave prompt cache only); no training on API content. Chat may keep **device-keyed encrypted backups**. Optional web search / fetch leave the enclave trust boundary |
| **Content** | AUP (12 Oct 2026): CSAM, weapons, fraud, malware, NCII of real people without consent, circumventing safety controls. **No blanket lawful-adult / pornography ban.** Chat has in-enclave safeguards (hard-no on child endangerment, mass violence, self-harm); **Inference API is not moderated or inspected** by Tinfoil |
| **Economics** | Chat **$20/mo**. API PAYG e.g. GPT-OSS 120B **$0.15/$0.60**; Gemma 4 31B **$0.40/$1.00**; Llama 3.3 70B **$1.75/$2.75**; DeepSeek V4.1 Flash **$0.60/$1.45**; GLM 5.3 **$1.80/$5.75**; Kimi K3.1 Pro **$4/$20**. Also PII filter, embeddings, STT/TTS. Confidential containers: hourly CPU/GPU with **monthly GPU commitment** |
| **Differentiators** | Strongest “verify every connection” SDK story among API peers; unmoderated API path; also rent confidential containers (proxy / custom serving); listed as a RedPill confidential backend |
| **Fit** | **Launch partner** for TEE Private/Pro overflow and attested open-weight API — especially if we want hardware privacy without running Phala VMs ourselves |
| **Risks** | Token prices above DeepInfra for many SKUs; Chat safeguards ≠ API (product must not confuse modes); search/fetch opt-ins weaken the privacy claim; container GPUs need monthly commit |
| **Sources** | [tinfoil.sh/pricing](https://tinfoil.sh/pricing), [tinfoil.sh/inference](https://tinfoil.sh/inference), [Security FAQ](https://tinfoil.sh/security-and-privacy-faq), [AUP](https://tinfoil.sh/terms/aup), [Safety](https://tinfoil.sh/safety-and-safeguards) |

### Phala vs Tinfoil — self-host infra cost variables (16 Nov 2026)

**RedPill** does not sell these line items (token API + chat only). Use **Phala Cloud** when modelling a self-hosted no-log proxy / TEE gateway on the RedPill path. **Tinfoil Containers** is the parallel path for attested custom serving. If you only buy either product as an inference API, leave these at **$0 / N/A** and use $/M token prices instead.

Monthly CVM figures assume ~730 hours. Sources: [cloud.phala.com/about/pricing](https://cloud.phala.com/about/pricing), [phala.com/pricing](https://phala.com/pricing), [tinfoil.sh/pricing](https://tinfoil.sh/pricing), [tinfoil.sh/containers](https://tinfoil.sh/containers); Tinfoil CPU/RAM/volume rates also corroborated via public calculator snapshots (~$0.06/vCPU-hr, ~$0.01/GB-RAM-hr, ~$0.10/GB-mo).

| Variable | Phala Cloud (RedPill TEE infra) | Tinfoil Containers |
|---|---|---|
| **GPU discount off on-demand** | H200×1: **~9%** (30d @ $5.00 vs $5.50 OD) / **~20%** (180d @ $4.40). H200×8: **~17%** / **~27%**. B300×1: **~6%** / **~9%**. GPU+CPU+disk bundled; cannot pause to save. | **Not published.** GPUs billed hourly but **require a monthly commitment**; rates in dashboard / sales only. |
| **Managed Kubernetes $/month** | **$0 / N/A** — docker-compose on CVMs, not managed K8s. | **$0 / N/A** — `tinfoil-config.yml` enclaves, not K8s. |
| **Model storage $/GB-month** | **~$0.10** ($0.000139/GB-hr; billed while the CVM exists, even stopped). GPU rentals: disk **included** in the hourly GPU rate. | **~$0.10** (volumes billed as provisioned GB-hours until deleted). No separate “model storage” SKU. |
| **Storage base fee $/month** | **$0** (min disk 20 GB × ~$0.10 ≈ **~$2** if you keep a tiny disk). | **$0** (no base fee). |
| **Load balancer $/month** | **$0** — included in Phala gateway / HTTPS endpoints. | **$0** published — custom domain is an add-on; price not listed. |
| **Egress $/GB** | **$0 published** — bandwidth included by machine size; no per-GB meter listed. | **Not published** — egress closed by default (hostname allowlist / open). |
| **Gateway machine $/month** | CVM compute: **tdx.small ~$44** ($0.06/hr) · **tdx.medium ~$88** ($0.12/hr) · **tdx.large ~$169** ($0.232/hr) **+** disk at ~$0.10/GB-mo. | CPU+RAM: **$0.06/vCPU-hr + $0.01/GB-RAM-hr**. Example **4 vCPU / 8 GB ≈ $0.32/hr ≈ $234/mo**. Whole-hour billing. |
| **Self-hosted Grafana machine $/month** | Same as gateway — run Grafana on another CVM (**~$44–$169+/mo** + disk). Not a Phala SKU. | Same as gateway — another container at the CPU/RAM rates above. Not a Tinfoil SKU. |

### Privatemode (Edgeless Systems)

| Field | Detail |
|---|---|
| **Category** | Enterprise confidential AI API + chat (Germany / EU) |
| **Value proposition** | OpenAI/Anthropic-compatible private inference with **client-verified E2EE**, confidential computing, and remote attestation |
| **Privacy** | Plaintext only inside attested CC; no retention of prompts/responses after request; no training; EU hosts (Scaleway FR, Lyceum DE). Metadata retained (~90 days / billing). Proxyless mode weaker (no client attestation) |
| **Content** | AUP bans illegal, harmful, abusive, **offensive** content — broad; not marketed as uncensored |
| **Economics** | Free 5M tokens/org once. PAYG from ~**€0.65 / 1M output**. Business **€250/mo** token budget. GLM-5.3-Flash **€0.20/€0.65**; gpt-oss-120b **€0.20/€0.65** |
| **Differentiators** | Strongest EU procurement / professional-secrecy story (BSI C5 attestation grade, §203 StGB review claims) |
| **Fit** | **Launch partner for Teams / regulated API**; weak for consumer low-refusal face |
| **Risks** | “Offensive” AUP; EUR + EU latency for Gulf users; smaller catalog |
| **Sources** | [privatemode.ai/pricing](https://www.privatemode.ai/pricing), [docs.privatemode.ai](https://docs.privatemode.ai/) |

### Venice.ai

| Field | Detail |
|---|---|
| **Category** | Consumer private + “unrestricted” AI platform |
| **Value proposition** | Device-side history, no-store proxy, labelled privacy modes through TEE/E2EE; markets private & uncensored creative use |
| **Privacy** | Anonymous (frontier sees prompts) → Private (contractual ZDR) → TEE (NEAR + Phala) → E2EE (device encrypt → enclave). History claimed device-only |
| **Content** | Markets NSFW within legal limits; bans CSAM / non-consensual likeness |
| **Economics** | Free tier; Pro **$18/mo**; Pro+ **$68**; Max **$200**; API credits |
| **Differentiators** | Scale, tokenomics (VVV), architectural template our product copies |
| **Fit** | **Competitor** — primary architectural and market peer; do not copy adult marketing for UAE |
| **Risks** | NSFW brand vs payments/app stores; Anonymous mode undercuts “private” if mislabelled |
| **Sources** | [venice.ai/privacy](https://venice.ai/privacy), [venice.ai/pricing](https://venice.ai/pricing), [competitor note](competitor-research/venice-ai.md) |

### Maple AI (OpenSecret)

| Field | Detail |
|---|---|
| **Category** | Consumer private AI chat + desktop agent + API |
| **Value proposition** | Client encryption; decrypt only in attested enclaves; “Maple cannot see your chats”; usage-dollar subscriptions |
| **Privacy** | Client E2EE + TEE; encrypted sync; open/reproducible attestation narrative |
| **Content** | Bans CSAM, weapons facilitation, harassment, circumventing safety filters. Hosts **DeepSeek V4.1 Flash Uncensored** framed for defensive security — adult/NSFW not explicitly banned nor marketed like Venice |
| **Economics** | Free; Pro **$20/mo**; Max **$100/mo**; Team **$30/user/mo**. DeepSeek Flash / Uncensored **$0.65/$1.45**; GPT-OSS 120B **$0.23/$0.90** |
| **Differentiators** | Cleanest **E2EE-first consumer** brand among peers; transparent dollar usage |
| **Fit** | **Competitor** for the clean private-consumer slot; API could be overflow TEE capacity |
| **Risks** | Smaller than Venice; ToS vs abliterated models tension |
| **Sources** | [maple.ai/pricing](https://maple.ai/pricing), [maple.ai/terms](https://maple.ai/terms) |

### Nillion (nilAI)

| Field | Detail |
|---|---|
| **Category** | Decentralized “Blind Computer” — private LLM API on TEE (nilCC) + private storage (nilDB) |
| **Value proposition** | OpenAI-compatible LLMs in NVIDIA TEEs with attestation and per-response signatures; optional Brave search; nilDB for private system prompts |
| **Privacy** | TEE hides prompts from operators (claimed); HTTPS into TEE (not full client-E2EE like Maple/Privatemode). Retention/training language **uncertain** in materials reviewed |
| **Content** | Builder/infra positioning; no strong uncensored consumer marketing found |
| **Economics** | Credits / Stripe; docs show schema defaults **2.0/2.0 per 1M** — treat as **unconfirmed live rates** |
| **Differentiators** | Blind stack (storage + compute + AI); crypto-native credits |
| **Fit** | **Overflow / experimental** — thin model catalog for launch primary |
| **Risks** | Pricing opacity; HTTPS≠E2EE; crypto UX; search breaks “blind” when enabled |
| **Sources** | [docs.nillion.com LLMs](https://docs.nillion.com/blind-computer/build/llms/overview) |

### Brave Leo / Brave Search API

Treat as two products.

**Leo (assistant)** — browser-embedded private AI. No cloud chat storage by default; Premium unlinkable tokens; subset of models on **NEAR AI TEE + device E2EE + OHTTP**. Moderated (no 18+ mode). Premium **~$15/mo**. **Fit: Competitor** for privacy-user mindshare, not an inference supplier.

**Search API** — independent web index for agents. **$5 / 1k** searches (LLM Context); **$5 free credit/mo**. Default query logs up to **90 days**; **enterprise ZDR** available. **Fit: Launch partner** for agent search — buy ZDR if search must match no-store story.

**Sources:** [brave.com/search/api](https://brave.com/search/api/), [Brave Search ZDR](https://brave.com/blog/search-api-zero-data-retention/), [Leo Premium](https://brave.com/premium/)

---

## Cohort B — Managed open-weight inference APIs

Pay-per-token hosts for open models. Best launch economics; privacy is contractual unless noted.

| Provider | Privacy | Content / AUP | Indicative price | Fit |
|---|---|---|---|---|
| **DeepInfra** | **Default ZDR**; no training | Silent on adult; illegal use banned | Llama 3.3 70B **$0.10/$0.32** | **Launch partner** |
| **Groq** | Default no retention; abuse logs ≤30d unless ZDR | Illegal sexual content / NCII; **not** blanket lawful-adult ban | GPT-OSS 120B **$0.15/$0.60**; Llama 70B often enterprise | **Launch partner** (speed) |
| **Together AI** | Stores prompts **by default**; org ZDR toggle | Hard ban: obscene / pornography; bars sensitive PII | Llama 3.3 ~**$1.04/$1.04**; DeepSeek Flash class ~**$0.30/$1.20** | **Avoid** as Private default; SFW overflow only |
| **Fireworks AI** | **ZDR by default** for open inference | Strict warranty: no nudity / sexually suggestive inputs | GPT-OSS 120B **$0.15/$0.60**; DeepSeek Flash **$0.30/$1.20** | **Avoid** for our product (ToS warranty) |
| **Novita** | ToS default ZDR | Aug 2026 AUP: “is sexually explicit” prohibited | Llama 3.3 70B **$0.135/$0.40** | **Avoid** / narrow SFW overflow |

**Takeaway:** DeepInfra + Groq win the launch open-weight lane. Together/Fireworks/Novita have strong platforms but AUPs that create suspension risk even for a clean product if users probe edges — and Fireworks’ input warranty is the hardest contractual conflict.

---

## Cohort C — Frontier APIs with Zero Data Retention

| Provider | Privacy | Content | Indicative price | Fit |
|---|---|---|---|---|
| **OpenAI API (ZDR)** | Default ~30-day abuse logs; **ZDR by prior approval** (not self-serve); no training on API data by default; PSP rolling out | Model Spec: erotica limited; high refusals | gpt-5 class ~**$1.25/$10**; higher for newer SKUs | **Frontier Anonymous** only |
| **Anthropic API (ZDR)** | Default ~30-day commercial retention; **ZDR via sales**; classifier scores may remain; some “covered” models not ZDR-eligible | Usage Policy (Nov 2026): **do not generate sexually explicit / erotic chats** — applies to end users of integrations | Opus 5.5 **$4/$20**; Sonnet 5.5 **$2/$10**; Haiku 5.5 from **$0.10/$0.50** | **Frontier Anonymous** with heavy caveats |

These are capability layers, not Private-mode backends. Always label them Anonymous (provider sees plaintext unless an enterprise private-processing path applies).

---

## Cohort D — GPU clouds for self-hosting

We control the stack (except marketplace Community). Full write-ups: [page 9](09-gpu-cloud-provider-value-research.md).

### Fit summary

| Fit | Providers |
|---|---|
| **Primary reserved** | CoreWeave, Nebius, Vultr (~$2.30), Denvr ($2.45), Seeweb EU (~€1.89) |
| **Secondary** | Crusoe, Lambda, DigitalOcean, NexGen/Hyperstack, GMI, Verda, Scaleway, Gcore, Bitdeer |
| **Overflow** | RunPod **Secure** only; Together dedicated / clusters |
| **Avoid (inference primary)** | AWS as primary GPU path; RunPod **Community**; Together serverless as Private default |

### One-line value cards

| Provider | Value offering in one line | H100 OD (indicative) | AUP note |
|---|---|---|---|
| **AWS** | Enterprise app plane + Bedrock/SageMaker; too dear for primary inference | ~$7.9 SageMaker / ~$5.97 Capacity Block | Strict Responsible AI + Guardrails |
| **DigitalOcean** | Simple GPU Droplets; published 12-mo reserved | $4.41 ($3.26 reserved) | Unlawful porn ban |
| **Lambda** | Research/production neocloud; 1-Click Clusters | $4.59 8× SXM (from 16 Nov 2026) | Obscene / indecent / illegal porn |
| **RunPod** | Cheap pods; Secure vs Community split | Secure PCIe ~$2.89 | **Explicit porn ban** + lifetime ban; Community = avoid |
| **CoreWeave** | AI-native K8s / InfiniBand production cloud | $6.16 (commit up to −60% quote) | Unlawful porn only — clearest big neo |
| **Nebius** | Transparent EU-friendly GPU cloud | $4.50 (eu-north1) | “Obscene” + illegal porn |
| **Crusoe** | Energy-differentiated GPU cloud | $3.90 → **$4.50** 1 Dec 2026 | Illegal / CSAM / NCEI; no blanket adult ban found |
| **Vultr** | Global mid-cloud; aggressive HGX list | **$2.30** | Obscene / offensive |
| **Verda** (ex-DataCrunch) | EU AI cloud; spot + serverless | $5.24 (spot $2.62) | No explicit porn ban found in excerpt |
| **NexGen / Hyperstack** | On-demand/reserved/spot; hibernation | $2.50–3.20 (reserved from $1.75) | Law-based; no named adult ban in summary |
| **GMI Cloud** | Dedicated GPU + Inference Engine; APAC factory story | from $2.60 | AUP English body **not retrieved** |
| **Denvr** | Canada/US transparent AI cloud | **$2.45** | Illegal/CSAM; mining banned |
| **Bitdeer** | Mining-heritage → AI cloud; public reserved columns | ~$2.90 (tracker) | “Obscene”; brand diligence heavier |
| **Scaleway** | FR/EU sovereign GPU + generative APIs | PCIe ~€2.86; SXM ~€6.61 | Unlawful porn / sexualized (FR context) |
| **Gcore** | Edge + GPU VMs/bare metal | ~$2.61–3.12 | “Inappropriate or unlawful” |
| **Seeweb** | Italian EU GPU; among cheapest public EU lists | **€1.89** (~$2.09) | Legality on customer; confirm Italian ToS |
| **Together AI** (dedicated) | DMI endpoints + GPU clusters without owning vLLM | Clusters $3.99; DMI $5.49 | Obscene/pornography ban; serverless stores by default |

---

## Cross-cohort comparison matrix

| Provider | Cohort | Privacy strength | Low-refusal friendliness | Economics | Role |
|---|---|---|---|---|---|
| Phala / RedPill | Confidential | Hardware TEE | High (uncensored SKUs) | Mid–high $/token | Launch TEE |
| Tinfoil | Confidential | Attested TEE API (+ containers) | High (API unmoderated; AUP illegal/NCII-focused) | Mid $/token; Chat $20 | Launch TEE |
| Privatemode | Confidential | Client E2EE + TEE | Low–mid (enterprise AUP) | Mid EUR | Teams / EU |
| Venice | Confidential consumer | Modes through E2EE | High (NSFW brand) | Consumer SaaS | Competitor |
| Maple AI | Confidential consumer | Client E2EE + TEE | Mid–high | Consumer SaaS | Competitor |
| Nillion nilAI | Confidential builder | TEE (+ HTTPS) | Uncertain | Opaque | Overflow |
| Brave Leo | Browser assistant | Policy + optional TEE | Low (moderated) | Consumer | Competitor |
| Brave Search API | Agent tool | ZDR optional | N/A (search) | $5/1k | Launch search |
| DeepInfra | Open API | Default ZDR | Highest among APIs | Best $/token | Launch |
| Groq | Open API | Near-ZDR + opt-out | High (legality-scoped) | Mid; speed premium | Launch speed |
| Together | Open API + GPU | ZDR opt-in | Low (porn ban) | Mid–high | SFW overflow |
| Fireworks | Open API | Default ZDR | Lowest (nudity warranty) | Mid | Avoid |
| Novita | Open API | Default ZDR | Low (sexual ban Aug 2026) | Very cheap | Avoid |
| OpenAI ZDR | Frontier | Approved ZDR | Low | High | Anonymous |
| Anthropic ZDR | Frontier | Sales ZDR | Lowest (erotic ban) | High | Anonymous |
| CoreWeave | GPU IaaS | Own stack | High (illegal-only porn) | High OD / good reserved | Primary |
| Nebius | GPU IaaS | Own stack | Mid (“obscene”) | Mid | Primary |
| Vultr | GPU IaaS | Own stack | Mid | Best big-list OD | Primary |
| Denvr | GPU IaaS | Own stack | High | Excellent OD | Primary |
| Seeweb | GPU IaaS | Own stack (EU) | Mid | Best EU OD | Primary EU |
| Crusoe | GPU IaaS | Own stack | High | Mid (rising Dec) | Secondary |
| Lambda | GPU IaaS | Own stack | Mid | Mid (rising 16 Nov) | Secondary |
| DigitalOcean | GPU IaaS | Own stack | Mid–high | Mid | Secondary |
| NexGen | GPU IaaS | Own stack | Mid | Strong reserved | Secondary |
| GMI | GPU IaaS | Own stack | Uncertain AUP | Attractive “from” | Secondary |
| Verda | GPU IaaS | Own stack (+ CC marketing) | Mid | Mid OD / good spot | Secondary |
| Scaleway | GPU IaaS | Own stack (EU sovereign) | Mid–low | PCIe OK / SXM dear | Secondary EU |
| Gcore | GPU IaaS | Own stack | Mid | Competitive | Secondary |
| Bitdeer | GPU IaaS | Own stack | Mid | Competitive | Secondary |
| RunPod Secure | GPU hybrid | Partner DCs | Low (porn ban) | Cheap | Overflow |
| RunPod Community | Marketplace | Third-party hosts | Low | Cheapest | **Avoid** |
| AWS | Hyperscaler | Own stack / Bedrock multi-tenant | Low | Highest | App plane only |

---

## Relationships worth remembering

- Venice TEE/E2EE → **Phala + NEAR AI**.
- RedPill aggregates **Phala, Privatemode, NEAR, Tinfoil, Chutes**.
- **Tinfoil** is a first-party confidential API/chat/containers product (tinfoil.sh), not only a RedPill backend.
- Brave Leo strong path → **NEAR AI** TEEs; nilAI optional search → **Brave**.
- Privatemode hosts in EU on **Scaleway** (among others) — stack coupling if both are in the design.

---

## Still to nail before contracts

1. Written ZDR / no-training addenda for DeepInfra, Groq, Brave Search (enterprise), Phala, Privatemode.
2. Phala / NEAR / Privatemode AUPs re-read against our content policy wording.
3. GMI Cloud full English AUP; Seeweb Italian adult clause.
4. Reserved quotes: CoreWeave −60%, Nebius, Crusoe, Together DMI, AWS Capacity Blocks.
5. Lambda (16 Nov) and Crusoe (1 Dec) list-price changes before any board pack.
