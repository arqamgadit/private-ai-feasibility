# 9. GPU cloud provider value research (self-host phase)

[Back to wiki home](README.md)

Research compiled **15 November 2026** for Venice-style private AI self-hosting of open-weight LLM inference. Focus: who controls the stack, AUP (especially adult/obscene bans), public H100/H200/B200 rates, reserved options, and fit for Primary reserved / Secondary / Overflow / Avoid.

**Product context:** our content policy blocks sexual content (see [page 5](05-content-policy-and-trust-safety.md)). AUP still matters: vague “obscene” clauses can create account-suspension risk even for lawful frank text. Community / third-party hosts are unsuitable for user prompts.

**Pricing caveat:** list prices move often (several providers announced Nov–Dec 2026 rises). Figures below are public list / tracker-confirmed unless marked **quote-only**. Confirm on the provider console before contracting. FX for EUR≈USD used ~1.10–1.11 where noted.

---

## Summary ranking for Venice-style self-host

| Fit | Providers | Why in one line |
|---|---|---|
| **Primary reserved** | CoreWeave, Nebius, Vultr, Seeweb (EU), Denvr | Dedicated stack we control; competitive H100; AUP compatible with our clean policy; reserved paths |
| **Secondary** | Crusoe, Lambda, DigitalOcean, NexGen/Hyperstack, GMI Cloud, Verda, Scaleway, Gcore, Bitdeer | Good IaaS options; price, region, ops maturity, or AUP grey areas make them backup rather than first pick |
| **Overflow** | RunPod **Secure Cloud**, Together AI dedicated / GPU clusters | Burst capacity; Together also for managed dedicated endpoints — not Community, not serverless-as-default for Private mode |
| **Avoid (for inference self-host)** | AWS Bedrock/SageMaker as primary GPU path; RunPod Community; Together serverless as privacy default | Cost, multi-tenant prompt visibility, marketplace hosts, or default retention / AUP |

---

## 1. AWS (GPU / Bedrock / SageMaker)

| Field | Detail |
|---|---|
| **Category** | Hyperscaler |
| **Core value prop** | Full enterprise cloud: EC2/SageMaker for self-managed GPUs; Bedrock for managed FM APIs with VPC/PrivateLink, Guardrails, and “inputs/outputs not used to train base models.” Best for the **non-GPU app tier** (API, DB, identity), not cheapest inference. |
| **Privacy posture** | Customer controls EC2/SageMaker stack. Bedrock: AWS states data not shared with model providers / not used to train base models; still AWS-operated multi-tenant inference unless custom model hosting. Regions worldwide; residency via Region choice + PrivateLink. |
| **Content / AUP** | AWS Responsible AI Policy bans non-consensual sexual imagery, harm to minors, etc. Bedrock adds model-provider AUPs + Guardrails (sexual content filterable). Not a blanket “legal adult OK,” and model filters are strict. |
| **H100 pricing** | SageMaker `ml.p5.48xlarge` (8×H100): ~**$63.30/hr** ≈ **~$7.91/GPU-hr** on-demand (third-party lesson + AWS pricing page). EC2 P5 Capacity Blocks / Savings Plans lower; Rillor (7 Nov 2026): Capacity Block ~**$5.97/GPU-hr**. Spot much lower, unsuitable for always-on private inference. |
| **Differentiators** | Nitro confidential compute options; Bedrock Custom Model Import / SageMaker for fine-tunes; deepest compliance portfolio (HIPAA, etc.). |
| **Fit** | **Avoid** as primary inference self-host (cost). **Secondary** for Teams/enterprise residency demos or app plane. |
| **Key risks** | 2–3× neocloud H100 list; Bedrock is not “we control the model process”; content filters fight “low refusal on lawful topics.” |
| **Sources** | [SageMaker pricing](https://aws.amazon.com/sagemaker/ai/pricing/), [Bedrock privacy](https://aws.amazon.com/bedrock/security-privacy-responsible-ai/), [Responsible AI Policy](https://aws.amazon.com/ai/responsible-ai/policy/), [Rillor neocloud vs hyperscaler](https://rillor.com/insights/neocloud-vs-hyperscaler-gpu-pricing/report) |

---

## 2. DigitalOcean (GPU Droplets)

| Field | Detail |
|---|---|
| **Category** | Regional / mid-cloud (developer cloud with GPU line) |
| **Core value prop** | Simple Droplet UX for 1×/8× H100/H200/MI300X; per-second billing; 12-month reserved rates published. |
| **Privacy posture** | Customer-controlled VMs in DO DCs (Paperspace heritage for ML tooling). Not a marketplace. |
| **Content / AUP** | AUP bans **unlawful** pornography (CSAM, non-consensual). Legal adult historically “may permit at sole discretion.” Compatible with our clean policy; not as permissive-clarity as CoreWeave’s “unlawful only” framing for porn. |
| **H100 pricing** | On-demand **$4.41/GPU-hr**; 12-mo reserved **$3.26/GPU-hr**. H200 OD **$4.47**, reserved **$3.40**. (New pricing effective 1 Aug 2026.) |
| **Differentiators** | Simple ops for small teams; AMD MI300X cheaper alternative; Spot GPU Droplets (interruptible). |
| **Fit** | **Secondary** — solid reserved path if we want DO elsewhere in the stack; not the cheapest or most AI-native K8s platform. |
| **Key risks** | Capacity windows for H100/H200; powered-off Droplets still bill until destroyed; 99% GPU SLA vs higher CPU SLA. |
| **Sources** | [GPU Droplets pricing](https://www.digitalocean.com/pricing/gpu-droplets), [AUP](https://www.digitalocean.com/legal/acceptable-use-policy), [Docs pricing](https://docs.digitalocean.com/products/droplets/details/pricing/) |

---

## 3. Lambda

| Field | Detail |
|---|---|
| **Category** | Neocloud |
| **Core value prop** | Research/production GPU cloud: self-serve instances + InfiniBand 1-Click Clusters; strong NVIDIA relationship. |
| **Privacy posture** | Customer-controlled instances/clusters; Lambda-operated DCs (US-centric). |
| **Content / AUP** | Prohibits distributing materials that are **obscene, illegal pornography, indecent, or hateful**; use for “obscene or unlawful purpose” banned. **Grey for legal adult**; our clean policy fits, but “obscene/indecent” is discretionary. |
| **H100 pricing** | **Price rise effective 16 Nov 2026 00:00 UTC:** 8× H100 SXM **$4.59/GPU-hr**; 1× H100 SXM **$4.89**; 1× H100 PCIe **$3.79**. 1-Click Clusters (2 wk–1 yr): 16 GPU **$6.16**, 64 **$5.85**, 256 **$5.54**/GPU-hr (IB fabric premium). 1 year+ **quote-only**. |
| **Differentiators** | 1-Click Clusters; free egress often cited; Superclusters for large training. |
| **Fit** | **Secondary** — good reserved cluster vendor; on-demand rising; AUP greyer than CoreWeave. |
| **Key risks** | Cluster $/hr above single-node OD; capacity contention; AUP discretion. |
| **Sources** | [lambda.ai/pricing](https://lambda.ai/pricing), [AskGPU Lambda](https://askgpu.com/lambda-pricing/), ToS via [lambda.ai/legal](https://lambda.ai/legal/terms-of-service) |

---

## 4. RunPod

| Field | Detail |
|---|---|
| **Category** | Marketplace + Secure Cloud hybrid |
| **Core value prop** | Cheap on-demand Pods/Serverless/Clusters; Secure Cloud in partner T3/T4 DCs vs Community (third-party hosts). |
| **Privacy posture** | **Secure Cloud:** RunPod/partner DCs — acceptable for production if contractually diligent. **Community Cloud:** third-party hosts — **do not put user prompts**. |
| **Content / AUP** | Explicit ban: “**pornography or graphic adult content**, images, or other adult products”; lifetime ban risk. Also “obscene… as determined by us.” **Strict** — fine for our clean product; hostile to Venice-like unrestricted brand. |
| **H100 pricing** (updated ~12 Nov 2026) | Secure: H100 PCIe **$2.89**, H100 SXM **~$3.99–4.39**, H200 **~$5.29**. Community: H100 PCIe from **$1.99**, SXM from **$2.69**. Reserved clusters available (sales). |
| **Differentiators** | Serverless workers; templates; very fast spin-up; low barrier. |
| **Fit** | **Overflow** (Secure only). Community = **Avoid**. |
| **Key risks** | Community host compromise; AUP lifetime bans; Secure capacity variability; disk idle charges. |
| **Sources** | [runpod.io/pricing](https://www.runpod.io/pricing), [ToS](https://www.runpod.io/legal/terms-of-service) |

---

## 5. CoreWeave

| Field | Detail |
|---|---|
| **Category** | Neocloud |
| **Core value prop** | AI-first GPU cloud with Kubernetes-native platform, InfiniBand clusters, free egress often highlighted; preferred for production LLM serving at scale. |
| **Privacy posture** | Customer controls workload on CoreWeave-operated infrastructure; NA + EU regions on public pricing. |
| **Content / AUP** | Bans **unlawful** pornography (CSAM, revenge porn). Does **not** blanket-ban legal adult. **Most permissive of large neoclouds** among those checked — still fine/safer for our clean policy. |
| **H100 pricing** | HGX H100 8× node **$49.24/hr** = **$6.16/GPU-hr** OD; Spot ~**$19.71**/node (~$2.46/GPU). H200 **$6.31**, B200 **$8.60**/GPU-hr. Committed usage “**up to 60% off**” — **quote** for reserved. |
| **Differentiators** | Mission Control / CKS Kubernetes; RDMA; inference single-GPU SKUs; enterprise SLAs. |
| **Fit** | **Primary reserved** — wiki hosting strategy already names CoreWeave; AUP + K8s maturity. |
| **Key risks** | Highest published OD among primary candidates; reserved needs sales; capacity commitments. |
| **Sources** | [coreweave.com/pricing](https://www.coreweave.com/pricing), [AUP](https://docs.coreweave.com/policies/terms-of-service/acceptable-use-policy) |

---

## 6. Nebius

| Field | Detail |
|---|---|
| **Category** | Neocloud (EU-rooted; NL entity Nebius B.V.) |
| **Core value prop** | Transparent GPU cloud with Managed K8s, Soperator (Slurm on K8s), free egress/public IP often cited; EU/US/ME regions. |
| **Privacy posture** | Customer-controlled VMs; EU-friendly contracting (Nebius B.V. + Inc + Israel entities, DPAs published). H100 only in `eu-north1`. |
| **Content / AUP** | Bans content that is **defamatory, obscene, abusive…** including child or **other illegal pornography**, bestiality, non-consensual sex. “Obscene” is **grey** for edge cases; our sexual-content ban aligns. Agreement also limits consumer/personal use of Services. |
| **H100 pricing** | **$4.50/GPU-hr** OD (H100 NVLink, `eu-north1`); preemptible from **$0.79** (dynamic). H200 **$5.40**. Commitment discounts for multi-month large clusters — **sales**. |
| **Differentiators** | EU residency; InfiniBand; transparent docs pricing; me-west / uk-south for newer GPUs. |
| **Fit** | **Primary reserved** — alongside CoreWeave in [hosting strategy](03-hosting-strategy.md). |
| **Key risks** | H100 region-limited; OD raised Oct 2026; “obscene” discretion; not for personal/consumer accounts under agreement. |
| **Sources** | [docs pricing](https://docs.nebius.com/compute/resources/pricing), [nebius.com/prices](https://nebius.com/prices), [AUP](https://docs.nebius.com/legal/aup), [Agreement](https://docs.nebius.com/legal/agreement) |

---

## 7. Crusoe

| Field | Detail |
|---|---|
| **Category** | Neocloud (energy-differentiated) |
| **Core value prop** | GPU cloud powered by stranded/cleaner energy narrative; instances + Managed Inference + Self-Serve Deployments + Managed K8s. |
| **Privacy posture** | Customer-controlled GPU instances; Crusoe-operated US-focused infrastructure. Customer Data treated as confidential under MSA. |
| **Content / AUP** | Bans illegal activity, child sexual exploitation, **NCEI**; no blanket legal-adult ban found in AUP PDF. Compatible with clean product. |
| **H100 pricing** | Current OD **$3.90/GPU-hr** (through 30 Nov 2026); **$4.50** from **1 Dec 2026**. H200 **$4.29 → $5.40**. Reservations: sales; unused reserved capacity **does not roll over**. |
| **Differentiators** | Energy story; Managed Inference token APIs; CMK $0.10/cluster-hr. |
| **Fit** | **Secondary** (was primary-candidate on price; Dec rise + SemiAnalysis ClusterMAX downgrade notes raise caution). |
| **Key risks** | Dec 2026 price hike; reservation no-rollover; reported cluster reliability concerns in third-party ClusterMAX commentary. |
| **Sources** | [crusoe.ai/cloud/pricing](https://www.crusoe.ai/cloud/pricing), [Oct 2025 pricing FAQ](https://support.crusoecloud.com/hc/en-us/articles/37421109850907-FAQ-Determining-On-Demand-Pricing-for-Crusoe-Offerings), [AUP PDF](https://crusoeenergy.pactsafe.io/versions/6a763aa330efed65d371105d.pdf), [legal.crusoe.ai](https://legal.crusoe.ai/) |

---

## 8. Vultr

| Field | Detail |
|---|---|
| **Category** | Regional / global mid-cloud |
| **Core value prop** | On-demand Cloud GPU + Bare Metal + Clusters without special reservation requests; many PoPs. |
| **Privacy posture** | Customer-controlled VMs/bare metal in Vultr DCs worldwide. |
| **Content / AUP** | Use Policy bans **offensive** content including **obscene**, child pornography, non-consensual sex acts. Broader than CoreWeave; grey for adult. Clean product OK. |
| **H100 pricing** | NVIDIA HGX H100 starting **$2.300/GPU-hr** (8× config on pricing page). Contract duration options via sales. |
| **Differentiators** | Geographic spread; Clusters for Slurm/K8s; aggressive list price. |
| **Fit** | **Primary reserved** candidate on **price + control**; diligence AUP + which city for residency. |
| **Key risks** | “Obscene/offensive” discretion; confirm InfiniBand/NVLink topology for multi-node serving; GPU billing uses 730-hour month model. |
| **Sources** | [vultr.com/pricing](https://www.vultr.com/pricing/), [H100 product](https://www.vultr.com/products/cloud-gpu/nvidia-h100/), [Use Policy](https://www.vultr.com/legal/use-policy/) |

---

## 9. Verda (formerly DataCrunch) — **verified rename**

| Field | Detail |
|---|---|
| **Category** | Neocloud / regional (European AI cloud) |
| **Core value prop** | Full-stack AI cloud (instances, serverless containers, clusters); EU sovereignty/sustainability positioning. **DataCrunch → Verda** announced Nov 2025; invoices may show “Verda (formerly DataCrunch)” from ~17 Nov 2025. |
| **Privacy posture** | Customer-controlled; European DC posture; Hopper Confidential Computing mentioned on H100 product page. |
| **Content / AUP** | Schedule 1 AUP: illegal AI uses (social scoring, untargeted facial scraping, etc.), spam, crypto-mining abuse, sanctions. **No explicit pornography ban** found in fetched T&Cs excerpt — confirm Schedule 1 in full before relying. |
| **H100 pricing** | Instances: OD **$5.241/GPU-hr**, Spot **$2.621**. Serverless continuous: **$5.77** / Spot **$2.88**. Instant clusters 16–64 IB: **on request**. |
| **Differentiators** | Spot + serverless scale-to-zero; EU brand; confidential compute marketing. |
| **Fit** | **Secondary** — EU option; OD higher than Vultr/Seeweb/Denvr. |
| **Key risks** | Rebrand transition; fixed pricing restructure in progress; confirm AUP adult silence with counsel. |
| **Sources** | [Rename blog](https://verda.com/blog/datacrunch-is-changing-its-name-to-verda), [Pricing](https://verda.com/pricing), [H100](https://verda.com/h100), [Terms](https://verda.com/terms-and-conditions) |

---

## 10. NexGen Cloud (Hyperstack)

| Field | Detail |
|---|---|
| **Category** | Neocloud (UK) |
| **Core value prop** | Hyperstack brand: on-demand/reserved/spot GPU VMs, hibernation, AI Studio; **NexGen Cloud Limited** is the contracting entity. Regions: CANADA-1, NORWAY-1, US-1 (docs). |
| **Privacy posture** | Customer VMs; region-selectable storage; DPA + Privacy Policy published. England & Wales law; LCIA arbitration in London. |
| **Content / AUP** | **No named adult/porn ban.** Dual rule: (1) general AUP bans illegal / abusive / fraudulent / violent use; (2) **AI Model** use adds “misleading, harmful, discriminatory, defamatory…” + applicable law. Can suspend on **actual or perceived** breach **without notice**; reserves right to **monitor**. See deep dive below. |
| **H100 pricing** | OD: H100 PCIe **$2.50**, NVLink **$2.60**, SXM **$3.20**. Reserved from **$1.75 / $1.82 / $2.72**. Spot H100 PCIe **$2.00**. H200 SXM **$3.99** (reserved from **$2.79**). Free bandwidth claim. |
| **Differentiators** | VM hibernation; 100% renewable energy claim; minute billing; AI Studio (managed inference + fine-tune). |
| **Fit** | **Secondary** — strong published reserved discounts; smaller than CoreWeave/Nebius for large reserved fleets. Self-host GPU ≈ **U3–U4** with more soft-kill risk than Seeweb; AI Studio ≈ **U2–U3**. |
| **Key risks** | Vague “harmful / discriminatory” AI clause + monitoring + perceived-breach suspension; capacity depth; brand confusion (NexGen vs Hyperstack). |
| **Sources** | [GPU pricing](https://www.hyperstack.cloud/gpu-pricing), [Terms (13 Jan 2026)](https://www.hyperstack.cloud/terms-and-conditions), [Docs](https://docs.hyperstack.cloud/), [nexgencloud.com T&Cs](https://www.nexgencloud.com/terms-and-conditions) |

### NexGen / Hyperstack “uncensored” terms deep dive (18 Nov 2026)

**Product split (do not mix):**

| Product | What it is | Uncensored relevance |
|---|---|---|
| **Hyperstack GPU / CPU VMs** (+ K8s, storage) | IaaS — you run vLLM/SGLang and your weights | Primary self-host path. Bound by **general** AUP + English law. |
| **AI Studio** | Managed catalog / playground / OpenAI-compatible API; third-party models labelled | Extra **AI Model** content sentence + upstream model licences. Not the abliterated-weights lane. |

**Who contracts:** NexGen Cloud Limited (“NexGen”), affiliates/subsidiaries. Hyperstack (`hyperstack.cloud`) is the product brand; same AUP text appears on nexgencloud.com.

**What the T&Cs actually say** ([Hyperstack Terms, version dated 13 Jan 2026](https://www.hyperstack.cloud/terms-and-conditions)):

1. **§1.1 Eligibility** — registration/use only if it does not contravene applicable law; NexGen “shall promptly terminate” if they determine a contravention.
2. **§6.1 Sanctions** — refuse / suspend / terminate for UK, US, or EU sanctions breaches (direct or indirect).
3. **§6.2 Acceptable use — general (all Services):**
   - Must not be **illegal, abusive, deceitful, fraudulent, violent or threatening**;
   - Must not introduce malware, overload, or violate security of any network/system;
   - **Actual or perceived** breach → account suspended/terminated **immediately, without prior notice**.
4. **§6.2 Acceptable use — AI Model sentence (added vs older Aug 2023 text on the same page):**
   - “You must not use **AI Model** to generate content that is **misleading, harmful, discriminatory, defamatory**, violates any third-party rights, or otherwise contravenes any applicable law.”
   - “NexGen reserves the right to **monitor** and suspend accounts found in violation.”
5. **Defined term “AI Model”** = “each third-party and/or NexGen provided model **made available on the Platform**.” That wording points at **catalog / AI Studio models**, not necessarily weights you install yourself on a rented VM. The **general** AUP still covers VM use.
6. **§4.6 Third-party AI Models** — labelled third-party models bring **their own** T&Cs / privacy / data policies on top; NexGen disclaims control.
7. **§4.4 / §12** — sole discretion to refuse service; termination for any T&Cs breach with or without notice; serious breach may lose data (normally ~30 days retrieval window).
8. **§11 Indemnity** — broad customer indemnity for use via the account (including third-party/end-user use), T&Cs breach, laws, IP.
9. **§14.6 / §13** — England & Wales law; LCIA arbitration seated in London (English).

**What is *not* in the contract:**

| Peer | Explicit sexual / obscenity bar? | NexGen / Hyperstack |
|---|---|---|
| Together | Yes — pornography / obscene | **No** |
| Fireworks | Yes — nudity / sexual warranty | **No** |
| Novita | Yes — sexually explicit | **No** |
| RunPod | Yes — porn / graphic adult | **No** |
| Seeweb Cloud GPU | No — legality + Art. 5 only | **No named adult ban** either |
| NexGen | — | **No porn clause**, but soft **“harmful / discriminatory / misleading”** AI language + **monitor** right |

**How this differs from Seeweb (for our clean private-AI stack):**

| | Seeweb Cloud GPU | NexGen Hyperstack GPU VMs | NexGen AI Studio |
|---|---|---|---|
| Adult / porn AUP | None | None | None |
| Soft content adjectives | No (“any law” only) | General AUP is conduct/infra-focused | **Yes** — harmful / discriminatory / misleading / defamatory |
| Monitoring reserved | Not in General Conditions | Yes (tied to AUP/AI clause) | Yes |
| Kill-switch | Art. 8 “behavioural” + Art. 10 listed triggers | **Perceived** breach, no notice; sole-discretion refuse | Same |
| Uncensored depth (our U-scale) | **U3–U4** | **U3–U4** with more discretionary risk | **U2–U3** (platform models + soft adjectives) |

**Score for our stack**

- **Self-host on Hyperstack VMs:** Contractually compatible with lawful low-refusal (no Together-style porn ban). Deploying our own open / abliterated weights is not barred by name. Residual risk is broader than Seeweb’s: **“perceived” breach**, **monitoring**, and the chance ops stretch “abusive / harmful” if complaints arrive.
- **AI Studio:** Treat like other managed catalogs — upstream model refusals + §6.2 AI sentence. Not where we get U4 control.
- **Our product policy** (block sexual content, allow frank lawful text) still fits; we are not asking them to host a Venice-style NSFW brand.
- **Must-do before production:** sales/comfort email that self-hosted lawful low-refusal inference (non-porn) on GPU VMs is in-bounds, and that the AI Model sentence is aimed at AI Studio / platform models, not customer-installed weights.

**Bottom line:** NexGen is **not morals-banned like Together/RunPod**, but it is **not as clean a “legality only” contract as Seeweb**. For uncensored-as-low-refusal, prefer **Hyperstack GPU VMs** over AI Studio, and get the AI-Model scope confirmed in writing.

---

## 11. GMI Cloud

| Field | Detail |
|---|---|
| **Category** | Neocloud (US HQ; APAC expansion) |
| **Core value prop** | Dedicated GPU compute + Inference Engine; Taiwan AI Factory; US/APAC/EU capacity messaging; SemiAnalysis ClusterMAX Silver (per third-party). |
| **Privacy posture** | GMI-operated DCs; region-aware pricing; dedicated single-tenant instances claimed. Live rates in console. |
| **Content / AUP** | AUP page exists under Legal; **full English text not retrieved** (JS/empty fetch) — **mark incomplete**; do not assume adult stance. |
| **H100 pricing** | Published “from” **$2.60/GPU-hr**; H200 from **$3.20**; B200 from **$5.00**; GB200 from **$8.00**. Committed plans discounted — **sales/console**. |
| **Differentiators** | Taiwan/Japan factory scale story; Inference + Compute unified; NVIDIA partner. |
| **Fit** | **Secondary** — price attractive; AUP verification and APAC latency for Gulf/EU users TBD. |
| **Key risks** | “From” pricing opacity; AUP unread; rapid expansion ops risk. |
| **Sources** | [gmicloud.ai/en/pricing](https://www.gmicloud.ai/en/pricing), [Legal index](https://www.gmicloud.ai/en/legal), [Pricing blog Oct 2026](https://www.gmicloud.ai/en/blog/gpu-cloud-pricing-explained-on-demand-reserved-and-bare-metal) |

---

## 12. Denvr (Dataworks)

| Field | Detail |
|---|---|
| **Category** | Neocloud / regional (Canada-rooted) |
| **Core value prop** | Transparent AI cloud: bare metal / VM / endpoints; InfiniBand 3200G H100 nodes; Calgary + Houston regions. |
| **Privacy posture** | Customer-controlled; Canada West (MSC1 Calgary) + US South (HOU1 Houston); DPA; Alberta/Canadian law for site ToS. |
| **Content / AUP** | Bans illegal activity including CSAM; no blanket pornography ban. Crypto **mining** banned. Clean product OK. |
| **H100 pricing** | H100 SXM 8× **$2.45/GPU-hr** OD (public, confirmed trackers 14–15 Nov 2026). Reserved up to **~20%** off — **sales**. H200 reserved-only on pricing page. |
| **Differentiators** | Canadian residency option; Weka/NVMe; per-minute billing; strong list price. |
| **Fit** | **Primary reserved** candidate on price + North America residency; diligence scale/SLA. |
| **Key risks** | Smaller footprint than CoreWeave; H200 not OD; confirm multi-region failover. |
| **Sources** | [denvr.com/pricing](https://www.denvr.com/pricing), [H100 product](https://www.denvr.com/product-pages/nvidia-h100), [AUP](https://www.denvr.com/acceptable-use-policy), [Data centers](https://docs.denvrdata.com/docs/overview/data-centers) |

---

## 13. Bitdeer

| Field | Detail |
|---|---|
| **Category** | Neocloud (crypto-mining heritage → AI cloud; Singapore entity) |
| **Core value prop** | GPU compute VMs/bare metal/containers + AI Studio; NVIDIA Cloud Partner; published 1y/3y reserved columns. |
| **Privacy posture** | Customer content as processor under ToS; Singapore PDPA framing; ISO 27001 / SOC2 claimed. |
| **Content / AUP** | Prohibits publishing material that is **false, defamatory, harassing, obscene, or otherwise unlawful**. **Grey/obscene.** |
| **H100 pricing** | Trackers (Nov 2026): OD about **$2.90**/GPU-hr H100 SXM; reserved listings ~**$2.46** (1y/3y) — **reconfirm live table** (pricing page is dynamic/empty in fetch). Earlier Oct read showed ~$2.36 OD. |
| **Differentiators** | Aggressive reserved public rates; Asia-Pacific HQ; mining→AI power ops. |
| **Fit** | **Secondary** — price good; brand/compliance diligence heavier (sanctions lists, crypto association). |
| **Key risks** | “Obscene” clause; pricing page volatility; Restricted Persons lists; reputational optics for a privacy VPN-adjacent product. |
| **Sources** | [bitdeer.ai GPU pricing](https://www.bitdeer.ai/services/pricing/gpu-compute), [Terms](https://www.bitdeer.ai/en/terms), [GPU cloud svc agreement](https://www.bitdeer.ai/en/legal-agreement/gpu-cloud-svc), [gpueconomy Bitdeer H100](https://gpueconomy.com/providers/bitdeer/h100-sxm) |

---

## 14. Scaleway

| Field | Detail |
|---|---|
| **Category** | Regional (French / EU sovereign cloud) |
| **Core value prop** | EU jurisdiction GPU instances (Paris PAR-2, Warsaw WAW-2) + Generative APIs + Managed Inference; “immune to extraterritorial regulations” marketing. |
| **Privacy posture** | Strong EU residency story; customer-controlled GPU Instances; AI services have separate multi-tenant Generative API terms. |
| **Content / AUP** | Abuse categories include “**Pornography or sexualized content**” framed as **unlawful** pornography/sexualized content (incl. adult sexual abuse material). French/EU law context is strict. Clean product required. |
| **H100 pricing** | Marketing: H100 PCIe from **€2.86/GPU-hr** (~**$3.15**); H100-SXM from **€6.61/GPU-hr** (~**$7.3**). Managed Inference H100-1-80G **€3.40/hr**. Zone-gated on pricing tables. Minute billing. |
| **Differentiators** | EU sovereign; also sells serverless generative APIs for overflow of *safe* traffic. |
| **Fit** | **Secondary** for EU user residency / Teams; SXM list expensive vs Seeweb. |
| **Key risks** | FR content law exposure; capacity per AZ; Generative API ≠ self-host privacy. |
| **Sources** | [scaleway.com/en/h100](https://www.scaleway.com/en/h100/), [choose GPU](https://www.scaleway.com/fr/choose-the-right-gpu/), [GPU pricing](https://www.scaleway.com/en/pricing/gpu/), [Abuse notice](https://www.scaleway.com/en/abuse-notice/) |

---

## 15. Gcore

| Field | Detail |
|---|---|
| **Category** | Regional / global edge+cloud (Luxembourg HQ) |
| **Core value prop** | GPU VMs + bare metal + InfiniBand + Managed K8s + Everywhere Inference across many PoPs. |
| **Privacy posture** | Customer-controlled cloud resources; multi-region including EU, US, Dubai, etc. |
| **Content / AUP** | ToS: Customer Content must not be **inappropriate or unlawful**; AUP incorporated (details on legal hub). Streaming product has NSFW detectors — separate from GPU cloud. Treat as standard EU host diligence. |
| **H100 pricing** | Trackers 15 Nov 2026: virtual GPU from ~**$2.61–3.12**/GPU-hr; bare metal ~**$3.01**. Reserved tables (EUR, volume tiers) e.g. 12-mo ~**€3.05–3.50**/GPU-hr by cluster size — confirm live portal. |
| **Differentiators** | Edge network + GPU; Everywhere Inference; EUR pricing API. |
| **Fit** | **Secondary** — useful if we need edge proximity; not first for dedicated LLM fleet. |
| **Key risks** | Price heterogeneity across SKUs; AUP “inappropriate” vagueness; GPU product maturity vs CoreWeave. |
| **Sources** | [gcore.com/pricing/cloud](https://gcore.com/pricing/cloud), [GPU prices API docs](https://docs.gcore.com/api-reference/cloud/pricing/list-gpu-prices), [ToS](https://gcore.com/legal?tab=terms_of_service), [gpueconomy Gcore](https://gpueconomy.com/providers/gcore/h100) |

---

## 16. Seeweb

| Field | Detail |
|---|---|
| **Category** | Regional (Italy / EU) |
| **Core value prop** | Italian GPU cloud: dedicated hardware, hourly billing, K8s/IaC, GDPR EU DCs, free network traffic claim. |
| **Privacy posture** | EU data processing; ISO claims; customer-controlled Cloud Server GPU. |
| **Content / AUP** | General terms: customer responsible for legality of content; **no explicit adult ban** found in English product page / summary — Italian law still applies. Confirm with Seeweb before production. |
| **H100 pricing** | **€1.89/GPU-hr** OD (~**$2.09**); committed **€1.80 / 1.70 / 1.61** for 3/6/12 months. H200 **€2.60**. Spot option (up to 40% off, interruptible, 2-min notice). |
| **Differentiators** | Among cheapest public EU H100 lists; 99.99% uptime claim; serverless GPU product. |
| **Fit** | **Primary reserved** for **EU residency / GDPR** self-host slice. |
| **Key risks** | Smaller global footprint; confirm multi-GPU NVLink topology vs list SKU; AUP explicitness. |
| **Sources** | [seeweb.it EN Cloud Server GPU](https://www.seeweb.it/en/products/cloud-server-gpu), [computeprices Seeweb H100](https://computeprices.com/providers/seeweb/gpus/h100) |

---

## 17. Together AI (dedicated / GPU endpoint vs serverless)

| Field | Detail |
|---|---|
| **Category** | Neocloud + model platform (hybrid) |
| **Core value prop** | Three layers: (1) **Serverless** per-token APIs, (2) **Dedicated Model Inference (DMI)** — single-tenant GPU replicas billed per minute, (3) **GPU Clusters** — bare metal Slurm/K8s. Distinct from pure IaaS: they also run the inference stack for DMI. |
| **Privacy posture** | Clusters: dedicated bare metal, “your data stays yours,” SOC2. DMI: dedicated replicas but Together-operated serving. Serverless: **stores prompts by default** — zero retention must be org-enabled (existing wiki finding). |
| **Content / AUP** | Strict: may not communicate material that is **obscene or constitutes pornography**. Also bars sending sensitive personal data (SSN, etc.) to Services. **Hostile to unrestricted/adult**; OK for our clean policy only if we accept their filter risk. |
| **H100 pricing** | DMI: **$5.49/GPU-hr** OD; reserved DMI **contact sales**. GPU Clusters: OD **$3.99**, preemptible **$1.99**, reserved 7–30d **$3.69**, 31–90d **$3.45**, 91+ **request**. (Pricing page also shows H200/B200 cluster rates.) |
| **Differentiators** | Fast path to custom/fine-tuned endpoints without owning vLLM ops; FlashAttention lineage; HIPAA-capable reserved endpoints marketing. |
| **Fit** | **Overflow** for dedicated endpoints / burst clusters. **Avoid** as Private-mode default if serverless retention not locked; AUP limits “uncensored” positioning. |
| **Key risks** | Pornography ban; default prompt storage on serverless; DMI cost above raw GPU; not full stack control on DMI. |
| **Sources** | [together.ai/pricing](https://www.together.ai/pricing), [DMI pricing docs](https://docs.together.ai/docs/dedicated-endpoints/pricing), [ToS](https://www.together.ai/terms-of-service), [H100 page](https://www.together.ai/gpu/nvidia-h100) |

---

## Indicative H100 on-demand snapshot (15 Nov 2026)

| Provider | ~$/GPU-hr OD | Notes |
|---|---|---|
| Seeweb | ~2.09 (€1.89) | EU |
| Vultr | 2.30 | HGX list |
| Denvr | 2.45 | 8× SXM |
| NexGen Hyperstack | 2.50–3.20 | PCIe→SXM |
| GMI | from 2.60 | “from” |
| RunPod Secure PCIe | 2.89 | not Community |
| Bitdeer | ~2.90 | tracker; confirm |
| Gcore | ~2.61–3.12 | SKU-dependent |
| Scaleway PCIe | ~3.15 (€2.86) | PAR-2 |
| Crusoe | 3.90 → **4.50** (1 Dec) | |
| Lambda 8× SXM | 4.59 (from 16 Nov) | |
| Nebius | 4.50 | eu-north1 |
| DigitalOcean | 4.41 | reserved 3.26 |
| Verda | 5.24 | spot 2.62 |
| Together DMI | 5.49 | clusters 3.99 |
| CoreWeave | 6.16 | commit up to −60% |
| AWS SageMaker p5 | ~7.9 | Capacity Block ~5.97 |

---

## Implications for our self-host phase

1. **Primary reserved shortlist:** CoreWeave (ops/K8s) + Nebius (EU/price) remain valid; add **Vultr** and **Denvr** on raw $/hr, **Seeweb** for EU GDPR slice.
2. **AUP:** CoreWeave and Denvr/Crusoe are clearest “illegal porn only.” RunPod, Together, Lambda, Nebius, Vultr, Bitdeer use **obscene / pornography** language — acceptable under our clean policy but raise suspension risk if users slip past filters.
3. **Never** put production prompts on RunPod Community or Vast-style marketplaces.
4. **Together** dedicated is overflow/ops shortcut, not a substitute for owning vLLM on reserved GPUs for Private mode.
5. Re-check Lambda (16 Nov) and Crusoe (1 Dec) list prices before any board pack that quotes $/hr.

---

## Still incomplete / counsel

- GMI Cloud full AUP English text (page did not return body).
- Seeweb explicit adult clause in Italian general conditions.
- Reserved quotes: CoreWeave −60%, Nebius commitments, Crusoe reservations, Together DMI reserved, AWS Savings Plans / Capacity Blocks for our exact Region.
- Zero-retention / no-training contractual addenda for each Primary shortlist (infra IaaS usually means *we* never send prompts to the vendor’s model API — but support access and abuse monitoring still need DPA language).
