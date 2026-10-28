# 1. Product overview

[Back to wiki home](README.md)

## What we are building

A private AI platform in the style of Venice.ai:

- **Chat, image generation and code** on open-weight models.
- **No server-side conversation storage.** Conversation history lives in the user's browser. Requests pass through our proxy without being stored.
- **Low refusal rates** on lawful topics, within the limits in [page 5](05-content-policy-and-trust-safety.md).

On top of that sits **agent mode**, a Tab-style agentic chat that:

- plans multi-step tasks,
- browses the web in a sandboxed browser,
- calls tools (search, fetch, extract),
- runs code in a sandboxed environment.

## Tiers

| Tier | Price | What it includes |
|---|---|---|
| Free | $0 | Rate-limited chat, about 30 images a month, no agent |
| Pro | $18/month | Higher limits, 300 images a month, 10 agent tasks a month |
| Max | $49/month | 60 agent tasks a month, premium models, credit top-ups |
| API | Usage-based | OpenAI-compatible endpoints, priced as a markup on inference |
| Teams | $40/seat/month | Shared workspaces, SSO, admin controls, private deployments |

Annual plans are discounted about 31%, matching Venice Pro's annual pricing.

## Privacy modes

Copied from Venice's published architecture. Each model is labelled with one mode so users know what protection they get.

| Mode | How it works | Trust required |
|---|---|---|
| Anonymous | Request is relayed to a frontier provider (OpenAI, Anthropic, Google) without the user's identity | The provider sees and may keep the prompt |
| Private (default) | Runs on our GPUs or on zero-data-retention partners | Contractual: relies on us and partners honouring no-retention terms |
| TEE (Pro) | Runs inside a hardware-isolated confidential-computing enclave with remote attestation | GPU operator cannot see prompts; users still trust our proxy |
| E2EE (Pro) | Prompt is encrypted on the device and only decrypted inside a verified enclave | Nobody, including us, can see the prompt. No web search or memory |

Safety classifiers run inside every mode, including inside the enclave for TEE and E2EE. See [page 5](05-content-policy-and-trust-safety.md).

## Launch timeline (model assumptions)

| Month | Milestone |
|---|---|
| 1–4 | Build phase |
| 5 | Public launch (Free and Pro) |
| 7 | Agent mode and Max tier |
| 9 | Developer API |
| 15 | Teams and enterprise |
