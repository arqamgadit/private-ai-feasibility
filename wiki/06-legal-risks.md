# 6. Legal risks

[Back to wiki home](README.md)

**This is not legal advice.** The business needs a UAE counsel plus someone covering the US, EU and UK. These are the risks to put in front of them, roughly in order of severity.

## UAE-specific

| Risk | Why it matters | Mitigation |
|---|---|---|
| Content laws | The UAE cybercrime law (Federal Decree-Law 34 of 2021) and media regulation law (Federal Decree-Law 55 of 2023) criminalise obscene content, insults to religion, content harming national unity, and "rumours". An "uncensored" AI is directly exposed, even when content is generated privately. Pornography is illegal in the UAE | Run the company from a free zone such as DIFC or ADGM; ask counsel whether to geo-restrict some markets; keep model defaults conservative; never market "no limits" |
| Data protection | The UAE PDPL (Federal Decree-Law 45 of 2021), or DIFC/ADGM data rules, still applies to accounts, emails and payment data | Privacy policy, data processing agreements with every provider, cross-border transfer rules |
| Crypto token (if copying Venice's VVV) | Dubai's Virtual Assets Regulatory Authority (VARA) regulates tokens, with licensing requirements | Leave out unless prepared for that regime |

## International (users will come from everywhere)

| Risk | Why it matters | Mitigation |
|---|---|---|
| EU AI Act transparency rules | Users must be told they're talking to an AI; AI-generated images must be labelled, including machine-readable watermarks | Add watermarking to the image pipeline; AI disclosure in the UI |
| UK Online Safety Act | AI chatbots are in scope once users can share content or the product works like search. Strict age checks for services producing pornographic content | Block explicit images; no sharing features at launch |
| US AI companion, self-harm and minors laws | California's companion-chatbot law (SB 243) and similar state laws impose duties on self-harm handling and minors. Wrongful-death suits against chatbot companies (for example Character.AI) show the risk is live | 18+ age gate, crisis-resource responses, no romantic companion features aimed at minors |
| US non-consensual imagery and deepfake laws | The federal Take It Down Act and state deepfake laws bite mostly if we host or share images | Block real-person sexual edits; no public gallery |
| GDPR (EU users) | Applies to account and payment data | EU representative, data processing agreements, transfer mechanisms |

## Built into the product

| Risk | Why it matters | Mitigation |
|---|---|---|
| Privacy claims are a legal promise | If we say "we can't see your prompts" and a provider logs them, that's a deceptive claim under consumer protection law (US FTC, UAE consumer law, EU law) | Every claim must match the real setup: zero-retention settings on and contracts signed. Use the wording in [page 5](05-content-policy-and-trust-safety.md) |
| Law enforcement requests | We can only hand over what we hold: mostly account and payment data | Publish a request-handling policy; consider a transparency report; don't promise to resist lawful orders |
| Agent mode action liability | An agent that browses, fills forms or buys things can break website terms, scrape illegally (US CFAA), or be used for fraud and spam | Confirmation steps before purchases and logins, rate limits, domain blocklist, terms making users responsible for their instructions |
| Dangerous instructions | Regulators care most about weapons (especially CBRN) and malware | Narrow set of hard refusals in every privacy mode |
| Model licences | Some weights ban certain uses or commercial use (Flux "dev" is non-commercial; Llama's acceptable-use policy bans some uses and needs a separate licence above 700M monthly users) | Keep a licence register for every model served |
| Copyright and likeness | Images of real people or trademarked characters create claims | Block named real people in image prompts; takedown process |
| Payment processors | Card network rules let processors shut accounts that generate prohibited content | Clean marketing plus the image controls in [page 5](05-content-policy-and-trust-safety.md) |
| Sanctions | Serving sanctioned countries breaches US OFAC and UN rules, and our providers will require compliance | Block sanctioned countries at signup and payment |

## Pre-launch checklist for counsel

1. Company structure and free zone (DIFC versus ADGM versus mainland).
2. Content policy and terms of service, including the 18+ requirement.
3. Privacy policy describing in-memory checks and the abuse-material reporting exception.
4. Data processing agreements with every inference provider.
5. Written trust and safety procedure: detection, blocking, reporting and appeals.

## Budget

The legal line in the [financial model](02-financial-model.md) starts at $15k/month, about right for Year 1. Expect a one-time $30–60k on top for initial multi-country setup.
