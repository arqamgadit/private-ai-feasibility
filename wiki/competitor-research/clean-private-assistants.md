# Clean private assistants: ExpressAI, Lumo, Duck.ai, Brave Leo

[Back to wiki home](../README.md)

Feature comparison of the four clean private consumer assistants named in [page 7](../07-market-research.md). Compiled **24 November 2026** from vendor product, pricing, and privacy pages.

Interactive version: [Private AI feature comparison](https://cursor.com/canvas/store-6d9201ae-7bc3-4f73-868f-a4721e776fc1/dd669d8c-f469-4218-8b1d-81cc2bd1c24f).

## The binding difference

Who can read the prompt **while the model is running**:

| Product | Inference privacy |
|---|---|
| **ExpressAI** | Confidential-computing enclaves for **all** models. Cure53 audited (Feb–Mar 2026). |
| **Brave Leo** | Default: Brave-hosted, no cloud chat retention. **GLM** path: client E2EE + attested TEE (NEAR AI), browser verifies attestation. |
| **Duck.ai** | Most models: anonymized proxy + contractual ZDR (provider still sees cleartext). **gpt-oss-120b** and **Gemma 4 31B**: TEE via Tinfoil (“zero provider visibility”). |
| **Lumo** | Stored history is zero-access encrypted. During inference, prompts are decrypted on **Proton-controlled GPUs** (user-to-Lumo crypto in transit). Not TEE today. |

Policy claims all four share: no training on chats, no ad profiling, history either local or zero-access encrypted.

## At a glance

| Dimension | ExpressAI | Lumo | Duck.ai | Brave Leo |
|---|---|---|---|---|
| Vendor | ExpressVPN | Proton | DuckDuckGo | Brave |
| Primary surface | Browser web app | Web + iOS/Android | Web + DuckDuckGo apps | Brave browser only |
| Free access | No | Yes (guest + Free) | Yes (no account) | Yes (no account) |
| Standalone AI SKU | No (VPN bundle) | Yes (Plus / Business) | No (Privacy Pro bundle) | Yes (Leo Premium) |
| Paid signal (USD) | Included; Pro ~$6.99/mo on 2-yr promo | $12.99/mo or $9.99/mo yearly | Plus $9.99 · Pro $19.99 | $14.99/mo or $149.99/yr |
| Business / teams | Positioned for sensitive work; no seats SKU | Lumo Professional / Workspace | No | No |
| Distribution | ExpressVPN base | Proton suite | Search + Privacy Pro | ~128M browser users (Brave claim) |

## ExpressAI (ExpressVPN)

**Positioning.** Private-by-design AI workspace on confidential computing. Included with Basic, Advanced, and Express Pro.

**Models (Pro).** GPT OSS 120B, Nemotron 12B, DeepSeek R1 Distill 32B, Qwen2.5-VL 32B, Qwen3.5/3.8 class, Gemma 4 31B. Basic/Advanced: GPT OSS 120B only.

**Limits.** Basic 50 credits/day · Advanced 100 · Pro/VIP 500. Pro: 50 MB uploads, 200 files, 2 GB vault. Multi-model compare costs one credit per model.

**Features.** Web search, file/image/video analysis (model-dependent), side-by-side model compare, Ghost Mode (auto-delete), zero-access encrypted vault, personalization. No image generation. No native mobile app yet (mobile web). No BYOM. No free tier.

**Privacy.** NVIDIA confidential enclaves; Cure53 pentest + crypto/infra audit. Prompts not used for training; not human-reviewed. Works without an active VPN connection.

## Proton Lumo

**Positioning.** Privacy-first assistant with Proton Mail–style zero-access history on European / Swiss infrastructure. Lumo 2.0 (Jun 2026) added Fast/Thinking modes, multimodal, stronger search, Memory, Projects, Custom Lumos/Skills.

**Models.** Lumo 2.0 Lite, Lumo 2.0 Max, Apertus 1.5. Proton lists underlying open models including Qwen 3.5, GLM 5.3, Image-Turbo, FireRed-Image-Edit-1.1.

**Limits.** Free: capped Max usage, messages, images, 1 Project, 7-day history, small single-file uploads. Plus: higher Max, unlimited chats/Projects/Skills, multi large uploads. Exact free caps unpublished.

**Features.** Web search with citations, image gen + edit, file uploads, Memory, Projects, Custom Lumos/Skills, Creations canvas, dictation on web, Business admin. Client apps open source; server routing not published.

**Privacy.** No logs after response; zero-access encrypted synced history; no training (opt-in anonymized Apertus feedback only). Inference cleartext on Proton GPUs — trust-based, not enclave-based.

**Price.** Free / Guest $0. Plus $12.99/mo or $119.88/yr ($9.99/mo). Professional ~$14.99/user/mo.

## Duck.ai (DuckDuckGo)

**Positioning.** Anonymized access to third-party chat models. Free frontier models; paid advanced models inside DuckDuckGo Plus/Pro (cannot buy AI alone).

**Models.** Free: Claude Haiku 5.5, Mistral Small 4, GPT-6 Luna, GPT-5.4 mini, gpt-oss-120b + Gemma 4 31B (TEE). Plus: + GPT-5.6 Terra, Claude Sonnet 5.5. Pro: + Claude Opus 5.5, GPT-5.6 Sol, higher reasoning, 2× limits.

**Limits.** Daily usage caps; subscribers get higher weekly extend. PDF pages: Free 15 · Plus 35 · Pro 50. No spreadsheet uploads.

**Features.** Chat, web search, image + PDF upload, image generation + refine, voice chat, local recent chats (pin up to 5), Fire Button delete, optional E2EE Sync & Backup. No Projects/Memory suite. No API. Personal use only.

**Privacy.** IP stripped before providers. ZDR + no-training agreements with providers (documented exceptions: prompt caching ≤1 hour; Anthropic abuse/law retention). TEE technical guarantee only on the two Tinfoil models.

**Price.** Free $0. Plus $9.99/mo or $99.99/yr (includes VPN + US PIR + ID restoration). Pro $19.99/mo or $199.99/yr.

## Brave Leo

**Positioning.** Browser-native assistant: summarize the current tab / PDF / Docs / Sheets / video without leaving Brave.

**Models.** Free: Qwen 3.6 35B, GPT 6 Luna, Nemotron Nano 3 30B, GLM 4.7 Flash, Claude Haiku 4.5 (+ Automatic). Premium adds DeepSeek v3.2, Claude Sonnet/Opus 5.5, Mistral Large 3, Grok 4.7, GPT 5.6 Terra, Kimi K2.5, and more. Separate GLM TEE / E2EE path. **BYOM**: local Ollama or remote third-party APIs (third-party privacy is the provider’s).

**Limits.** Free “reasonable” rate limits; Premium higher. One Premium covers up to 5 devices. 7-day free trial.

**Features.** Page-aware chat, Brave Search, temporary chats, local history, preferences, Automatic model selection, BYOM. Image generation on roadmap, not shipping. Requires Brave browser.

**Privacy.** No cloud chat retention after response; no training; free needs no account. Premium uses unlinkable tokens. GLM path: Oblivious HTTP + attested Nvidia TEE operated by NEAR AI; Brave gateway strips IP but does not see plaintext.

**Price.** Free $0. Premium $14.99/mo or $149.99/yr.

## Capability matrix (summary)

| Capability | ExpressAI | Lumo | Duck.ai | Brave Leo |
|---|---|---|---|---|
| Multi-model picker | Yes (Pro: 6) | Yes (3 branded) | Yes (many) | Yes (+ Automatic) |
| Side-by-side compare | Yes | No | No | No |
| Web search | Yes | Yes | Yes | Yes (Brave Search) |
| File upload | Yes (rich on Pro) | Yes (plan-capped) | Images + PDF only | PDF / Docs / Sheets / page |
| Image understanding | Yes | Yes | Yes | Yes |
| Image generation | No | Yes (+ edit) | Yes | No (roadmap) |
| Voice | No | Dictation (web) | Yes | iOS voice-to-text |
| Memory / Projects / Skills | Personalization only | Yes | Customization only | Preferences |
| BYOM | No (stated future) | No | No | Yes |
| Business seats | No | Yes | No | No |
| Developer API | No | No | No | No |

## Where each wins

| Job | Winner |
|---|---|
| Strongest default cryptographic privacy | **ExpressAI** (TEE everywhere + Cure53). Brave GLM path is comparable but optional. |
| Best free product surface | **Lumo** (features) / **Duck.ai** (Claude/GPT quality) |
| Best frontier models | **Duck.ai** free + Pro; **Brave Premium** also hosts Claude/GPT/Grok |
| Best browser workflow | **Brave Leo** |
| Best productivity / suite | **Lumo** |
| Best VPN attach | **ExpressAI** (privacy story) and **Duck.ai** (free frontier hook) |

## Implications for our product

Aligned with [page 7](../07-market-research.md):

1. **“No training” is table stakes** at $10–15. Lumo, Duck.ai, and Leo already sell that shelf.
2. **The $11 human-review / no-operator-read promise** is where ExpressAI (and Brave’s attested GLM path) differentiate. An $18 plan needs TEE + attestation + a published audit, not only a privacy policy.
3. **Product depth gap:** ExpressAI is thinner than Lumo on projects, memory, image gen, and mobile. Matching ExpressAI’s privacy *and* Lumo’s surface is an open space.
4. **Frontier vs enclave trade-off:** Duck.ai’s free Claude/GPT quality comes from letting the provider see text (except two TEE models). Full-enclave products stay on open weights.

## Sources

| Source | Used for |
|---|---|
| [ExpressAI product](https://www.expressvpn.com/expressai), [launch PR](https://www.expressvpn.com/news-pr/expressai-private-ai-platform), [cost](https://www.expressvpn.com/support/knowledge-hub/expressai-cost/), [privacy](https://www.expressvpn.com/support/knowledge-hub/expressai-privacy-protections/), [pricing](https://www.expressvpn.com/pricing), [Cure53 report](https://cure53.de/pentest-report_expressvpn-ai_2026.pdf) | ExpressAI features, limits, audit |
| [Lumo](https://proton.me/lumo), [pricing](https://proton.me/lumo/pricing), [models](https://proton.me/support/lumo-models), [privacy](https://proton.me/support/lumo-privacy), [security model](https://proton.me/blog/lumo-security-model), [Lumo 2.0](https://proton.me/blog/lumo-2) | Lumo features and architecture |
| [Duck.ai help](https://duckduckgo.com/duckduckgo-help-pages/duckai), [privacy](https://duckduckgo.com/duckduckgo-help-pages/duckai/ai-chat-privacy), [cost](https://duckduckgo.com/duckduckgo-help-pages/get-duckduckgo/how-much-does-duckduckgo-cost), [Plus vs Pro](https://duckduckgo.com/duckduckgo-help-pages/privacy-pro/plus-and-pro-plan-differences), [uploads](https://duckduckgo.com/duckduckgo-help-pages/privacy-pro/duck-ai/does-duckai-support-file-uploads), [image creation](https://duckduckgo.com/duckduckgo-help-pages/duckai/image-creation) | Duck.ai models and packaging |
| [Brave Leo](https://brave.com/leo/), [models help](https://support.brave.app/hc/en-us/articles/26727364100493-What-are-the-differences-between-Leo-s-AI-Models), [how to use](https://support.brave.app/hc/en-us/articles/20958609786637-How-do-I-use-Brave-Leo), [Premium](https://brave.com/premium/), [E2EE / TEE blog](https://brave.com/blog/browser-ai-e2ee/), [BYOM](https://support.brave.app/hc/en-us/articles/34070140231821-How-do-I-use-the-Bring-Your-Own-Model-BYOM-with-Brave-Leo) | Leo features and TEE path |

Model catalogs and promo VPN prices change often; re-check order pages before board packs.
