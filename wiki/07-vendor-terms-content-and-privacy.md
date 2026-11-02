# 7. GPU vendor terms: uncensored content and privacy

[Back to wiki home](README.md)

Covers the 19 vendors on the **Vendors** sheet of [Private AI - Hosted Infra Cost.xlsx](Private%20AI%20-%20Hosted%20Infra%20Cost.xlsx), where we would rent GPU machines and run our own vLLM stack. Read from each vendor's public terms of service, acceptable-use policy (AUP), privacy policy and data processing agreement (DPA) on **2 November 2026**. **Not legal advice**; negotiated contracts can override public terms, so get the important points confirmed in writing.

Two questions:

1. **Uncensored content.** Do the terms let us serve a lightly filtered model, including abliterated or uncensored fine-tunes? Every vendor bans child abuse material, non-consensual imagery and illegal content, so the ratings below are about everything else.
   - **Permissive:** only illegal content is banned.
   - **Moderate:** vague clauses ("obscene", "objectionable", "harmful") or an AI-safety clause give the vendor discretion.
   - **Restrictive:** adult or sexual content is banned by name, or the terms bar bypassing AI safety filters.
2. **No logs and privacy.** Can we run with no prompt logs, and how much can the vendor see or hand over?
   - **Strong:** the vendor commits not to access our content, and pushes back on or gives notice of government requests.
   - **Adequate:** standard processor terms, but with monitoring or inspection rights.
   - **Weak:** the vendor scans content, imposes telemetry, requires end-user lists, or uses third-party hosts.

No vendor's terms stop us running our own stack with prompt logging switched off. The difference is what the vendor reserves the right to do on top.

Since we already block sexual content (see [key decisions](README.md#key-decisions-so-far)), a ban on adult content matters less to us than two other kinds of clause:

- **Bans on bypassing AI safety measures** (DigitalOcean, Novita). These could be read to cover hosting abliterated models.
- **Terms that defeat "no logs"** (GMI, Bitdeer, Nebius, Novita):
  - GMI bars disabling its telemetry.
  - Bitdeer wants a list of end users and know-your-customer (KYC) data on them.
  - Nebius can dump VM memory.
  - Novita has automated content scanning.

## Summary

| Vendor | HQ / governing law | Uncensored content | No logs and privacy |
|---|---|---|---|
| **Crusoe** | US (New York law) | Permissive | Strong |
| **Verda** | Finland | Moderate (close to permissive) | Strong; GPU confidential computing available now |
| **Seeweb** | Italy | Permissive | Strong (no public DPA) |
| **AWS** | US (Washington) | Permissive | Strong |
| **DeepInfra** | US (California) | Permissive | Adequate |
| **CoreWeave** | US (New York) | Moderate, leaning permissive | Adequate |
| **Denvr** | Canada (Alberta) | Permissive on public documents; cloud contract not public | Adequate |
| **Hyperstack (NexGen Cloud)** | UK | Moderate | Adequate |
| **Nebius** | US entity, Delaware law, for new customers | Moderate | Adequate (memory-dump right) |
| **DigitalOcean** | US (Delaware) | Moderate (clause against bypassing AI safety) | Adequate |
| **Vultr** | US (New Jersey) | Moderate, leaning restrictive | Adequate |
| **Scaleway** | France | Restrictive (pornography banned) | Strong |
| **Gcore** | Luxembourg | Restrictive (sexually explicit content banned) | Adequate |
| **Lambda** | US (California) | Restrictive ("obscene", "indecent") | Adequate, close to weak |
| **Bitdeer** | Singapore | Moderate, leaning restrictive | Weak |
| **Together AI** | US (California) | Restrictive (pornography, sensitive data) | Weak |
| **RunPod** | US (Delaware) | Restrictive (pornography, lifetime ban) | Secure Cloud adequate; Community Cloud weak |
| **GMI Cloud** | US / Taiwan | Restrictive (NSFW banned) | Weak |
| **Novita** | Unclear (Delaware law; PPIO/China links) | Restrictive (sexually explicit content; safety-filter bypass) | Weak |

**Best fits on both questions:** Crusoe, Verda, Seeweb and AWS, then DeepInfra and CoreWeave.

## Vendor notes

### Crusoe

- **Content:** the AUP names child abuse material, non-consensual explicit imagery, hate incitement, self-harm promotion and malware. There is no "obscene" or "objectionable" clause. Crusoe gives notice and asks for a fix within 24 hours before suspending.
- **Privacy:** Crusoe "will only access or use Customer Data to provide the Services". Its log and metrics agent is optional and installed by the customer. Crusoe "shall challenge any request that is not binding and valid" and notifies customers.
- **Gaps:** no GPU confidential computing; US jurisdiction.

### Verda (formerly DataCrunch)

- **Content:** the terms ban "unlawful, harmful… obscene… offensive" material. There is no adult-content clause, and suspension requires Verda to be "acting reasonably".
- **Privacy:** Verda acts as processor under a GDPR DPA built into the terms. Data stays in Helsinki. It holds ISO 27001, 27017, 27018 and 27701 plus SOC 2 Type II.
- **Confidential computing:** the only vendor here with GPU confidential computing rentable today, on B200, B300 and RTX PRO 6000. Its FAQ asks "Can Verda staff read our data? No." ExpressVPN's ExpressAI runs on it.
- **Government requests:** Verda complies "only… where strictly legally required" with notice, and reports zero requests to date.

### Seeweb

- **Content:** the Italian General Conditions require only legality. Resale is explicitly allowed.
- **Privacy:** the security whitepaper says Seeweb "does not intervene in any way" in customer content, and access requires a judge-signed order. It holds ISO 27001, 27017 and 27018, and is qualified by Italy's national cybersecurity agency (ACN). Hosting is Italy only.
- **Gaps:** no public DPA template (signed per customer), no SOC 2, no confidential computing. Ask whether Italian telecom retention laws make Seeweb keep network metadata.

### AWS

- **Content:** the AUP has no adult or "objectionable" category; it bans illegal content, child abuse material and "serious harm".
- **Responsible AI Policy:** bans non-consensual sexual imagery, deepfakes and "intentionally circumvent safety filters". It covers AI services "we provide"; whether it reaches models we load on raw EC2 is a question for counsel.
- **Privacy:** contractually, AWS will "not access or use Your Content except as necessary to maintain or provide the Services" or to comply with law. The Nitro System has "no mechanism for any AWS operator to access" instances. It has a GDPR DPA with standard contractual clauses, SOC 2 and ISO certifications, and publishes transparency reports.
- **Gaps:** US jurisdiction; no GPU confidential computing on its H100 (P5) instances; costly (see page 4).

### DeepInfra

- **Content:** illegal use only; no adult or "objectionable" wording.
- **Privacy:** zero data retention is written into the contract for the inference API and custom deployments, and overrides the privacy policy.
- **Gaps:**
  - Zero retention covers "Provider-run models", so it may not cover rented B200 containers. Confirm in writing.
  - The trust center and DPA could not be loaded.
  - US jurisdiction.

### CoreWeave

- **Content:** bans only "Unlawful Pornography" (child abuse material and non-consensual imagery). It also has a non-exhaustive clause and a "harm CoreWeave's… reputation" clause.
- **Privacy:** CoreWeave acts as processor with a DPA and standard contractual clauses. It may investigate, report, and "intercept or block" traffic on AUP violations. It holds ISO 27001 and SOC 2.
- **Gaps:** GPU confidential computing is only planned (Rubin, Q4 2026). The public policy documents are from 2021–2022, and large deals use negotiated agreements.

### Denvr

- **Content:** no public cloud AUP or services agreement, so the binding content rules are unknown. Request the real contract.
- **Privacy:**
  - Denvr may monitor use to detect violations and collects system-level metrics.
  - Its DPA covers Canadian and Californian privacy law (PIPEDA, CCPA) but has no GDPR standard contractual clauses.
  - It promises notice before complying with legal requests.
  - It holds SOC 2 Type II; it has no ISO 27001.
  - Regions are Calgary and Houston.

### Hyperstack (NexGen Cloud)

- **Content:** no adult-content clause. An AI clause bans "harmful" or "misleading" output from an "AI Model… made available on the Platform", which arguably excludes models we host ourselves. Suspension can be "with immediate effect".
- **Privacy:** "We never access, use, share your data without authorisation". It has a public UK GDPR DPA and SOC 2 Type 2.
- **Gaps:** ISO 27001 is still pending. Confidential computing is offered only to contracted customers on dedicated nodes.

### Nebius

- **Content:** content that is "obscene… or otherwise objectionable" can be deleted without notice. "Illegal pornography" is defined with a US-style obscenity test.
- **Contracting entity:** customers who signed up after 13 November 2025 contract with Nebius Inc. under Delaware law, not with the Dutch entity.
- **Privacy:** Nebius has the strongest law-enforcement clause in this list. It redirects requests to the customer first, gives notice, discloses the minimum, and challenges overbroad requests.
- **Red flag:** "Nebius may perform memory dumps of Virtual Machines" on a suspected violation. A memory dump of a running inference VM would capture live prompts.

### DigitalOcean

- **Content:**
  - Legal adult content is not banned.
  - Its 2026 AI clause bans anything that "circumvents… safety mechanisms, guardrails… implemented in artificial intelligence systems" on models run on its servers. **This is the main risk for abliterated models**; get written clarification.
  - It also bans medical, legal or financial advice without human review.
- **Privacy:** staff have no access "unless a customer grants us permission". It needs a search warrant for VM contents and notifies customers with 7 days to object. It has a public DPA and SOC 2. It can "intercept or block" traffic on violations.

### Vultr

- **Content:** "obscene", "patently offensive, or otherwise objectionable" and reputation-harm clauses; Vultr can end service over content it "considers… high risk, in its discretion".
- **Privacy:** Vultr does not access content other than "as may be required by law or for security purposes". The AUP still lets it "review any User Content". It holds ISO 27001, 27017, 27018 and SOC 2. The DPA is available on request only. It promises to "cooperate with law enforcement", with no promise of notice.

### Scaleway

- **Content:** "content… of a pornographic nature, is strictly prohibited". There are also "public decency" and "offensive" clauses. AI-specific terms ban "inappropriate" uses and require compliance with the EU AI Act.
- **Privacy:** Scaleway has "no general monitoring obligation". Data is deleted within 10 days of termination, with no copy kept. It has a GDPR DPA, ISO 27001 and HDS (French health-data hosting certification). Hosting is EU only.
- **Fit:** good for privacy, but expect takedowns of explicit text.

### Gcore

- **Content:** bans "sexually explicit or morally repugnant content", with "zero tolerance" and null-routing.
- **Abuse duties on us:**
  - We must publish content rules and give users a way to report content.
  - We must answer abuse notices within 24 hours and keep abuse logs for 2 years.
- **Privacy:** Gcore is a "mere conduit" under the EU Digital Services Act with no monitoring duty. GPU bare metal is dedicated. It has a GDPR DPA and ISO 27001, and publishes transparency reports under the Digital Services Act.

### Lambda

- **Content:** bans "obscene… illegal pornography, indecent, or hateful" material and "any obscene… purpose", enforced at its "sole discretion".
- **Restriction on users' data:** bars submitting "sensitive personal data", which chat users will inevitably type.
- **Privacy:**
  - Lambda reserves the right "to monitor the use of the Services and Customer Property".
  - It "may transfer and store Customer Property in other… jurisdictions at its sole discretion" unless an order form says otherwise.
  - No public DPA.
  - Strong certifications: SOC 2 and ISO 27001.
  - No confidential computing.

### Bitdeer

- **Content:** bans "obscene" content, plus "harm" and "bigotry" clauses. The licence is "solely for Your internal business purposes"; confirm a public chat service is allowed.
- **Privacy:**
  - Bitdeer says it does not monitor content, but may "audit Your use… through… monitoring systems".
  - **We must give Bitdeer a list of our end users and KYC information on them**, which is incompatible with anonymous users.
  - No public DPA.
  - Singapore law and Singapore International Arbitration Centre (SIAC) arbitration.

### Together AI

- **Content:** bans anything "obscene, or constitutes pornography". It also bans sending "any financial or medical information… or any sensitive personal data", and reselling the services on a standalone basis.
- **Privacy:**
  - Together "may monitor your use of the Services".
  - Its GPU clusters run a control plane that Together manages.
  - On the inference API, prompts are stored by default, and zero retention must be switched on.

### RunPod

- **Content:** bans "pornography or graphic adult content" with a "lifetime ban", plus "objectionable (as determined by us)". The same terms cover Secure Cloud and Community Cloud.
- **Privacy:**
  - RunPod "may… access, store, process, and use any of Your Content", and serverless logs are kept 90 days.
  - On Community Cloud, third-party hosts run the machines.
  - Custom DPAs need $3,000 or more of committed monthly spend.
  - Usable for privacy only on Secure Cloud pods.

### GMI Cloud

- **Content:** bans "Not Safe For Work content… sexually explicit content, pornography, graphic violence". GMI may "monitor, moderate, and remove content".
- **Privacy:**
  - Its export certification says we "will not disable… or attempt to bypass any monitoring, telemetry, logging" controls. This was seen in the console terms; confirm whether it also applies to GPU rental.
  - Inputs to its model API are classified by a hosted model.
  - Data is stored in the US and Taiwan.
  - No public DPA.

### Novita

- **Content:** bans content that "is sexually explicit" and any attempt to "circumvent the safety filters… of Novita AI or any underlying model provider, including by means of jailbreaking".
- **Privacy:**
  - Its "zero data retention" clause also reserves "automated safety screening" of content.
  - Technical data is kept 2 years.
  - GPU instances are containers.
  - Data centre partners are not disclosed.
  - Ownership is unclear, with links to PPIO (China) and a Hong Kong region.

## Get in writing before signing

- DigitalOcean: whether abliterated models break the clause against bypassing AI safety measures.
- AWS: whether the Responsible AI Policy reaches models we host ourselves on EC2.
- DeepInfra: whether zero data retention covers rented GPU containers.
- Denvr: the actual cloud services agreement and AUP.
- Seeweb: the DPA, and whether it keeps network metadata.
- For every vendor in the launch stack:
  - network and flow-log retention periods (not published by most);
  - whether staff can access running instances.
