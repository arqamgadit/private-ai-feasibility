# 7. Open-weight model licences

[Back to wiki home](README.md)

**This is not legal advice.** It summarises licence types for open-weight models we may serve or fine-tune, and what they mean for product and hosting choices. Upstream terms change; keep a **licence register** (model checkpoint → LICENSE URL → date reviewed) and re-read files before shipping.

Licence text on weights governs **use of the model**; it does not resolve training-data copyright, output ownership in every jurisdiction, or provider terms of service. See also [Legal risks](06-legal-risks.md) and [Provider comparison](04-provider-comparison.md).

**Licences were read from upstream Hugging Face / vendor repositories in November 2026.** Same model family can use different licences per variant (for example GLM-5.3 custom licence vs GLM-5.3-Flash MIT; Qwen3.8-27B Apache-2.0 vs Qwen3.8-Flash-Next Qwen Community).

---

## Why this matters for our platform

We may **self-host weights**, **offer inference APIs**, **embed** models in chat/agent products, **fine-tune**, or **relay** requests to third-party hosts. Vendor licences treat those paths differently:

| Deployment pattern | Typical licence question |
|---|---|
| **Embedded feature** (user talks to our app; we run the model) | Often *not* "Model as a Service" (MaaS) under Chinese community licences |
| **MaaS** (customers get inference or fine-tuning with control over inputs, params, or training data) | Often triggers **separate commercial agreements** or revenue gates |
| **Pure relay** (forward requests to someone else's hosted model) | Usually **excluded** from MaaS in Z.ai, Moonshot, and Qwen definitions |
| **Internal-only** (no third party gets model, outputs, or capabilities) | Often **exempt** from MaaS gates (Kimi K3, Qwen Community, StepFun) |
| **Fine-tune / distill / merge** | Always check **derivative-work** rules (StepFun is explicit on output-based training) |

If we grow into a **hosted inference business** or a **coding/office copilot**, custom licences bite before standard MIT/Apache models do.

---

## Standard permissive licences

### MIT

**Examples in our model set:** MiMo-V2.6-Pro/Flash, DeepSeek V4.x Flash/Pro, GLM-5.3-Flash, Ling 3.1 Flash, LongCat 2.0, and many others.

**Grant:** Use, modify, distribute, sublicense, and sell copies; deploy and fine-tune; create derivatives. Commercial use is allowed without a separate vendor contract.

**Obligations:** Include the copyright and licence notice in redistributions of the software or substantial portions (including weight bundles if treated as the "Software").

**Implications:**

- Lowest friction for **commercial hosting**, **APIs**, and **closed-source products**.
- **No patent grant** (unlike Apache-2.0); no acceptable-use schedule in the licence itself (other laws and our [content policy](05-content-policy-and-trust-safety.md) still apply).
- **No MAU or revenue thresholds** in the licence.

### Apache-2.0

**Examples:** Qwen3.8-27B (dense), Mistral Large 3, Hy3, gpt-oss-120b, Gemma 4 31B.

**Grant:** Same broad permissions as MIT, plus an **explicit patent licence** from contributors.

**Obligations:** Preserve licence, copyright, patent, trademark, and attribution notices; include NOTICE file if present; mark modified files; on redistribution, pass on the licence.

**Patent retaliation:** If you sue claiming the model infringes your patents, your patent licence from contributors can terminate.

**Implications:**

- Preferred by many legal teams for **commercial redistribution** and **enterprise** deals because of the patent clause.
- **No trademark licence** — do not imply vendor endorsement.
- Still no MaaS revenue gates in the licence text (Meta **Llama** and others may add **separate** acceptable-use policies — track those outside the Apache file).

---

## Modified standard licences

### Modified MIT (example: Kimi K2.6)

Full **MIT** text plus one commercial-scale rule:

- If the software or derivatives power a **commercial** product or service with **more than 100 million monthly active users** or **more than USD 20 million monthly revenue**, the UI must **prominently display "Kimi K2.6"**.

**Implications:**

- Behaves like MIT for almost all realistic launch scales.
- **No MaaS-specific contract** in the licence (unlike Kimi K3).
- Plan UI/branding only if we approach hyperscale consumer products.

---

## Custom vendor licences (by family)

Several Chinese labs and some US vendors use **custom "community" or model licences**: MIT-like grants plus **MaaS definitions**, **revenue or MAU gates**, **attribution**, or **restricted commercial grants**. Definitions of **Model as a Service** are aligned across Z.ai, Moonshot, and Qwen: hosted inference or fine-tuning where a third party has meaningful control over inputs, parameters, or training data; **not** mere relay to another host; **not** capabilities embedded only in specific product features.

### Z.ai — GLM-5.3 License

**Applies to:** GLM-5.3 (not GLM-5.3-Flash, which remains **MIT**).

**Grant:** Broad — use, copy, modify, distribute, **sublicense, sell**, deploy, fine-tune, derivatives. Notice + compliance with law.

**Extra condition:** If we **operate MaaS** and **we plus affiliates** exceed **USD 10 billion** aggregate revenue in **any consecutive 12 months**, we must pass **Z.AI's security review** before **any commercial use** of the software or derivatives. Scope and method are determined by Z.AI.

**Implications:**

- **Neoclouds and most enterprises:** licence behaves like a strong permissive grant.
- **Hyperscale MaaS providers:** contractual uncertainty (review outcome, timing, conditions).
- No UI attribution threshold; no separate licence for all MaaS at lower revenue.

**Contact:** `glmlicense@z.ai` — [upstream LICENSE](https://huggingface.co/zai-org/GLM-5.3/raw/main/LICENSE).

### StepFun — StepFun Model License 1.0

**Applies to:** Step 5 Preview and other StepFun models using this licence.

**Grant:** Apache-2.0-style — patent grant, redistribution conditions, **sublicence** allowed.

**Derivative works:** Fine-tunes, distillation, merge, quantisation, continual pre-training, etc. Apps that **only call via API** are not derivatives **solely** for that reason. A model trained **to a material extent on this model's outputs** is **deemed** a derivative.

**Conditions:**

| Trigger | Obligation |
|---|---|
| Redistribute model or derivative | Pass licence, notices, NOTICE file, modifications marked, model card or link |
| Commercial product **> 100M active users/month** or **> USD 20M revenue/month** | Prominently display **"Powered by StepFun AI"** (or name StepFun designates) on UI, About, agreements, docs |
| **Hardware OEM** first shipping model on phones, vehicles, wearables, robots, smart home, etc. | **Separate commercial licence** before launch |
| **MaaS** + commercial purpose when **we plus affiliates > USD 20M** revenue in **12 months** | **Separate commercial licence** |

**Exemptions:** Internal use (no third-party access to model, outputs, or capabilities); use via **StepFun-certified** distribution within certification scope.

**Termination:** Material breach ends rights; possible reinstatement within **30 days** after written notice if cured.

**Implications:**

- Strongest **patent** clarity among custom licences here.
- **Output distillation** explicitly pulls new models into licence conditions.
- **Device manufacturers** and **MaaS businesses above $20M/yr** need StepFun deals early.

**Contact:** `license@stepfun.ai` — [upstream LICENSE](https://huggingface.co/stepfun-ai/Step-5-Preview/raw/main/LICENSE.txt).

### Moonshot — Kimi K3 License

**Grant:** MIT-like bundle including sublicense, sell, deploy, fine-tune, derivatives.

**Section 2 — MaaS gate:** MaaS operator and **affiliates > USD 20M** in **12 months** → **separate agreement with Moonshot** before any **commercial** use of software or derivatives.

**Section 3 — Large product:** **> 100M MAU** or **> USD 20M monthly revenue** → prominently display **"Kimi K3"** on the UI.

**Exemptions:** **Internal use**; use through **Moonshot official products or certified inference partners** (sections 2 and 3 do not apply).

**Implications:**

- **API/inference startups** above **$20M/yr** must sign with Moonshot for commercial MaaS — the public licence alone is insufficient.
- **Embedded chat** (not customer-controlled fine-tuning) may avoid MaaS classification; confirm with counsel.
- Partner or Moonshot-hosted routes may bypass gates if certified.

**Upstream:** [Kimi-K3 LICENSE](https://huggingface.co/moonshotai/Kimi-K3/raw/main/LICENSE).

### Qwen — Qwen Community License 1.0

**Applies to:** Qwen3.8-Flash-Next and other checkpoints tagged with this licence (not Apache-2.0 dense variants).

**Grant:** Broad — sell, deploy, host, fine-tune, derivatives ("Use").

**Section 1 — Large product:** **> 100M MAU** or **> USD 20M monthly revenue** → show **respective model name** on the UI.

**Section 2 — MaaS or AI Work Assistant:** If we run **MaaS** **or** an **AI Work Assistant** (product **primarily** for AI-assisted **coding or office productivity**, e.g. Qoder/QwenWork), we must obtain a **separate licence from Qwen** before **any commercial use** of the software or derivatives.

**AI Work Assistant excludes:** single-purpose tools (e.g. translation); domain-primary assistants (shopping, maps); AI that is only a **feature** of a product whose primary purpose is not coding/office productivity.

**Internal use exception:** Section 2 does not apply to internal use that does not expose software, outputs, or capabilities to third parties.

**Implications:**

- **Any commercial MaaS** on these weights likely needs a **Qwen commercial licence**, even at small revenue.
- **Copilot-shaped products** may trigger **AI Work Assistant** even without self-hosting — high priority for legal review.
- Dense **Apache-2.0** Qwen checkpoints avoid this file's MaaS/AWA clause but still need a register entry per checkpoint.

**Contact:** `model-business@notice.qwencloud.com` — [upstream LICENSE](https://huggingface.co/Qwen/Qwen3.8-Flash-Next/raw/main/LICENSE).

### MiniMax — MiniMax Community License (M3)

**Grant (opening text):** Deal in the software **for non-commercial purposes** with notice preserved.

**Commercial use (Section 2):** If used for **Commercial Use** — including paid products/services using the model or derivatives, **commercial APIs**, and **fine-tuned or otherwise modified** deployments for commercial purposes:

1. Prominently display **"Built with MiniMax M3"** (site, UI, blog, about, docs).
2. If **products and services built on M3** generate **> USD 20M yearly revenue**, obtain **prior written authorization** (`api@minimax.io`, subject **M3 licensing - authorization request**); otherwise send a **one-time notice** (subject **M3 licensing — notice**).

**Appendix — prohibited uses:** Includes illegal content, **military purposes**, harm to minors, intentional harmful misinformation, and discrimination/hate across listed characteristics.

**Implications:**

- **Not OSI-style open source:** commercial deployment is **conditional** (attribution + email workflow).
- **Hosted inference and fine-tunes** are explicitly commercial — plan compliance before launch.
- Prohibited-use list should align with our [content policy](05-content-policy-and-trust-safety.md) and terms of service.

**Upstream:** [MiniMax-M3 LICENSE](https://huggingface.co/MiniMaxAI/MiniMax-M3/raw/main/LICENSE).

### NVIDIA — OpenMDW-1.1 (Nemotron 3.5 Super VL)

**Note:** Nemotron 3.5 Super VL model cards point to **OpenMDW-1.1**, not the older **NVIDIA Open Model Agreement** / **Nemotron Open Model License** on nvidia.com. Other NVIDIA releases may use those older agreements — read the **LICENSE file in each repo**.

**Grant:** Deal in **Model Materials** without restriction, including **copyright, patent, database, and trade secret** rights in the materials.

**On distribution:** Include a copy of the agreement and applicable copyright/origin notices.

**Patent/copyright litigation:** Participating in suits alleging the materials infringe IP **terminates** grants (with a defensive exception if sued first).

**Outputs:** **No licence-imposed restrictions** on use, modification, or sharing of **outputs**.

**Implications:**

- Among the most **permissive** options for **commercial hosting**, fine-tuning, and output reuse — no MAU/revenue gates in the licence.
- We remain responsible for **third-party IP** in materials and outputs (licence states this explicitly).

**Upstream:** [OpenMDW-1.1](https://openmdw.ai/license/1-1/).

### Other vendor-specific terms (reference)

| Family | Licence label | One-line implication |
|---|---|---|
| **Llama** (if used) | Custom / acceptable use | Commercial use with policy constraints; **> 700M MAU** needs separate Meta licence |
| **Flux dev** (images) | Non-commercial | Not for commercial serving without a different licence |
| **Older NVIDIA models** | NVIDIA Open Model / Nemotron Open Model | Apache-like + NOTICE attribution + litigation termination; confirm guardrail-related clauses per version |

---

## Comparison: gates and obligations

| Licence | Separate deal or review | Typical threshold | UI / branding | Notable extra |
|---|---|---|---|---|
| **MIT** | None | — | Notice on redistribution | No patent grant |
| **Apache-2.0** | None | — | NOTICE + attribution | Patent grant + retaliation |
| **Modified MIT (K2.6)** | None | **100M MAU** or **$20M/mo** | **Kimi K2.6** on UI | Otherwise MIT |
| **GLM-5.3 (Z.ai)** | Security review | MaaS + **$10B / 12 mo** | None in licence | Flash variant = MIT |
| **StepFun 1.0** | Commercial licence | MaaS + **$20M / 12 mo**; all **hardware OEM** | **Powered by StepFun** at mega scale | Output training = derivative; termination |
| **Kimi K3** | Moonshot agreement | MaaS + **$20M / 12 mo** | **Kimi K3** at mega scale | Internal + certified partner exempt |
| **Qwen Community 1.0** | Qwen licence | **Any commercial MaaS or AI Work Assistant** | Model name at mega scale | Internal exempt; AWA catches copilots |
| **MiniMax M3** | Written auth | M3 product revenue **> $20M / yr** | **Built with MiniMax M3** | Non-commercial framing; prohibited uses |
| **OpenMDW-1.1** | None in licence | — | On redistribution only | Outputs unrestricted |

---

## Operational checklist

1. **One row per served checkpoint** in the licence register: name, HF repo, licence name, URL, review date, owner.
2. **Classify our architecture** (embed vs MaaS vs relay vs internal) before adding a custom-licence model to the default route.
3. **Flag copilot/agent products** for Qwen Community **AI Work Assistant** and StepFun **derivative** rules if we train on vendor outputs.
4. **Email workflows** (MiniMax notice/authorization; vendor commercial teams for Qwen, Moonshot, StepFun) before GA on those weights.
5. **Re-check licences** when swapping Flash vs Pro vs dense variants — filenames differ within the same brand.
6. **Counsel review** before claiming "open source" in marketing; several custom licences are **source-available** or **community** terms, not OSI-approved.

---

## Related pages

- [Legal risks](06-legal-risks.md) — jurisdiction, content law, and "keep a licence register"
- [Hosting strategy](03-hosting-strategy.md) — when we self-host vs use managed APIs
- [Provider comparison](04-provider-comparison.md) — inference provider **terms** (separate from weight licences)
