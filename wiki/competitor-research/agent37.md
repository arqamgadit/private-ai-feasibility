# 8. Agent37 competitor analysis

[Back to wiki home](../README.md)

Research compiled **28 October 2026** from Agent37's website, documentation, terms of service (updated 4 August 2026) and privacy policy (updated 1 September 2026). Their pricing and policies changed substantially in August–September 2026, so re-check before relying on them.

## Framing

Agent37 (Agent 37 Inc., [agent37.com](https://www.agent37.com)) is **not a direct consumer competitor**. It sells cloud sandboxes and hosted agent "harnesses" to companies building agent products. It matters to us in two ways:

1. **Enabler of competitors.** Its templates and white-label dashboard let anyone launch per-user AI agents (personal assistants, proactive agents, texting agents) in days. That lowers the barrier for rivals to our agent mode.
2. **Possible supplier.** It is a much cheaper alternative to E2B for the code and browser sandboxes behind our agent mode (see [page 3](../03-hosting-strategy.md) and [page 4](../04-provider-comparison.md)).

How to read the numbers:

- **Sourced** figures come from Agent37's own pages, listed in Sources. Most are vendor claims, not independently verified.
- **Estimate** means our own calculation, with the assumption stated.

## Key facts

| Item | Value | Source |
|---|---|---|
| What it sells | Persistent Linux sandboxes and full VMs for AI agents, plus hosted agent harnesses | Docs home |
| Customers | "Powering agents for over 200 companies" (vendor claim) | Homepage |
| Named customers | Vision, LeniHealth, Lionox, Future Bridge Solutions, FlyHermes, Agentastic, GetOpenClaw; testimonials from Boon, ETEC+ and Perflo | Homepage |
| Billing | Prepaid wallet, metered per minute; no subscription, plan fee or minimum | Homepage FAQ |
| Compliance | SOC 2 Type I (report under NDA); Type II in progress | Privacy policy |
| EU/UK representative | DataRep (also its EU Digital Services Act representative) | Privacy policy |
| Funding, team size, revenue | Not found | – |

## 1. Product

### Core platform

- **Instances:** persistent Linux sandboxes isolated with gVisor, or full VMs with their own kernel. Full VMs support Docker-in-Docker, Compose, Kubernetes and a hardware-accelerated Android 14 emulator.
- **Lifecycle:** stop, restart, resize, fork, and auto-sleep when idle, waking on the next request. Files and agent memory survive restarts.
- **Backups:** automatic backups and restore points.
- **Networking:** authenticated HTTPS URL per instance, public ports, custom domains, SSH, and per-instance egress controls (internet only, an allowlist, or cut off).
- **Operations:** logs, CPU/memory/disk metrics, cron schedules that wake an agent, run a turn and let it sleep again.
- **Custom images:** build from a Dockerfile or import from a registry.
- **Self-serve onboarding:** one unauthenticated API call creates a workspace and API key, so an agent can sign itself up and start paying.

### Agent layer

| Feature | Detail |
|---|---|
| Harness templates | Hermes, OpenClaw, Claude Code, Codex, OpenCode, Grok, Pi, or your own Docker image |
| Agent API | Send messages, stream replies, manage sessions, choose models per turn, read and write files |
| Models | Managed LLM router "at OpenRouter cost with no markup", or bring your own key |
| App integrations | Composio: 1,000+ apps per the homepage (250+ per the API docs), with OAuth handled |
| Paid tools | Web scraping, social data, people and company data, image and video, email and calls via Perflo, about a cent per call |
| Search | Managed Brave Search |
| Browser and desktop | Headless browser, full desktop you can watch live and take over, Browser Use Cloud integration (stealth, proxies, CAPTCHA solving) |
| Messaging channels | Telegram, WhatsApp, Slack, Discord and about two dozen more; iMessage, email and phone calls through Inkbox |
| Works as sandbox for | Claude Managed Agents, OpenAI Agents API and SDK, Cursor self-hosted cloud agents, LangChain Deep Agents |

### Ready-made product patterns (from the docs)

These are the direct signal of competition for our agent mode. Each is documented as a forkable build:

- Chat app giving every user their own always-on agent.
- Website builder returning a live public URL.
- White-label, multi-tenant agent dashboard ("fork it, rebrand it, ship it").
- Proactive agent "like Dots" that keeps its own schedule and messages the user first.
- Texting assistant "like Instinct" with its own iMessage line.
- Agent team "like Grok Bot" with named bots sharing one computer.
- Personal assistant "like Muse" with persona, memory, goals and check-ins.

## 2. Pricing

| Unit | Rate |
|---|---|
| vCPU | $0.0011 per vCPU-hour |
| Memory | $0.00096 per GB-hour |
| Disk | About $0.09 per GB-month ($0.36/month for 4 GB) |
| 2 vCPU / 4 GB running all month | $4.76 |
| Idle (stopped or sleeping) | Disk only |
| Starter credit | $5 once a card is on file |
| Startup programme | Up to $10,000: $1,000 to start, then matched against spend |
| Price guarantee | Refunds the difference if you find a cheaper sandbox |

Managed models, search and integrations are metered separately from the same wallet, with a spend cap per instance.

### Vendor's own comparison (2 vCPU / 4 GB, 57 hours a month)

| Provider | Monthly cost | Multiple of Agent37 |
|---|---|---|
| Agent37 | $0.37 | 1x |
| AWS EC2 c6a.large | $4.36 | 11.7x |
| Hetzner CX23 | $6.49 | 17.5x |
| Daytona | $9.44 | 25.4x |
| E2B | $9.44 | 25.4x |
| Cloudflare Sandbox | $11.34 | 30.5x |
| Modal | $13.56 | 36.5x |
| Vercel Sandbox | $19.43 | 52.3x |

**Estimate:** a 2 vCPU / 4 GB sandbox costs about **$0.006 an hour** on Agent37 versus about $0.17 on E2B, roughly 27x cheaper. A 4-minute agent task would cost about $0.0004 in sandbox compute, against $0.04 in our [financial model](../02-financial-model.md). The rates are unusually low; we have not tested performance or how far a vCPU is shared.

## 3. Privacy and security

### What it says it does

- Does **not collect** prompts, AI responses, tool-call contents, terminal output, desktop or file-browser sessions, or integration payloads into its own systems, and does not train on customer data.
- API keys configured inside an instance stay in that instance; its own issued keys are stored only as hashes.
- With your own model keys, Agent37 is **not in the conversation path**. With its managed credentials, model calls go through its proxy to providers such as OpenRouter, recording tokens, model and cost but not content.
- Isolation through gVisor with a hard disk quota per sandbox; hosts have no public hostname; all traffic enters through Cloudflare's edge over TLS with an API key.
- Encryption: TLS 1.2+ in transit; AES-256 volume encryption for instance storage; AES-256 for backups, account and billing data.

### What it keeps

| Data | Retention |
|---|---|
| Instance files, agent memory and their encrypted backups | As long as the instance exists; a recovery copy for 7 days after deletion |
| Request and operational logs (metadata only, no bodies) | Rolling window, currently up to 30 days |
| Usage and managed-model metadata | While the instance exists, then as part of billing history |
| Account data | Until 30 days after a deletion request |
| Billing records | Typically 7 years |

### Caveats for a privacy-first product

- **Data at rest by design.** Persistent disks and backups hold whatever the agent writes. That conflicts with our "nothing stored" promise unless we use short-lived sandboxes, delete them after each task, or encrypt workspaces with keys only the user holds.
- **Operator access.** The policy says it keeps "infrastructure-level access" to host servers for provisioning, updates, security and support.
- **Sub-processors in the path:** Cloudflare (routing and backup storage), Firebase, Vercel, Grafana Cloud (metrics and request logs), PostHog, Composio, Daytona (template builds), and OpenRouter and Brave if using managed credentials.
- **No hardware-sealed (TEE) option**, unlike Phala or NEAR AI for inference.
- **Data location not stated.**

## 4. Content policy

The acceptable-use policy bans:

- illegal use and infringing others' rights;
- malware, phishing, spam, fraud, harassment, and "content designed to harm others";
- attacks on its or anyone's infrastructure, or interfering with other customers;
- cryptocurrency mining;
- circumventing metering, resource limits or isolation;
- reselling bare access to the service.

There is **no explicit adult-content clause**; only illegal content is banned. The customer is responsible for everything its agents do, including on third-party platforms, and for its own end users. Abuse reports go to info@agent37.com; violating workloads are suspended or removed, and repeat offenders lose their accounts.

## 5. Strengths and weaknesses

| Strengths | Weaknesses and unknowns |
|---|---|
| Very low per-minute pricing with true scale-to-zero | Young company; funding, team size and revenue not found |
| Persistent per-user "agent computers" with sleep and wake | SOC 2 Type I only; Type II still in progress |
| Broad harness support, including Claude Code, Codex and OpenClaw | Stores data at rest, with operator infrastructure access |
| Rich integrations: messaging channels, iMessage, Composio, paid tools | Data location not published |
| White-label dashboard and copyable product patterns | Rates this low may not last; performance untested |
| No explicit adult-content ban (lower account-shutdown risk) | Terms and privacy policy both rewritten in August–September 2026 |
| Clear, detailed privacy policy | Managed model router depends on OpenRouter |

## 6. Threat assessment

| Dimension | Rating | Why |
|---|---|---|
| Direct competitor for consumers | Low | Sells to builders, not end users |
| Enabler of agent-mode rivals | **High** | Copyable patterns for personal, proactive and texting agents cut launch time to days |
| Competitor for our developer API | Low | Offers no inference of its own; its router resells OpenRouter |
| Value as a supplier | **High** | Could cut agent sandbox cost by an order of magnitude |

**Takeaway:** agent infrastructure is becoming a cheap commodity. Our agent mode can't win on infrastructure. It has to win on privacy guarantees, the quality of the agent itself, user experience and distribution.

## 7. Implications for our product

1. **Pilot Agent37 against E2B** for the agent-mode sandboxes. If the rates and performance hold, cut the sandbox line in the [financial model](../02-financial-model.md) from $0.04 to about $0.001 per task. Search then becomes the main per-task tool cost.
2. **Bring our own model keys.** Point sandboxes at our zero-retention inference providers ([page 4](../04-provider-comparison.md)) so Agent37 stays out of the conversation path. Don't use its managed router.
3. **Keep sandboxes short-lived by default.** Create a sandbox per task and delete it afterwards, so nothing persists beyond the 7-day recovery copy. Offer persistent workspaces only as an opt-in, encrypted with user-held keys, and disclose it.
4. **Consider a "personal agent computer" for Max.** An always-on agent with scheduled routines and messaging channels. Agent37's patterns show demand and cost about $0.36 a month idle plus per-minute compute.
5. **Before signing, ask for:**
   - a data processing agreement and the list of data locations;
   - the SOC 2 Type I report and a Type II timeline;
   - written confirmation that our content policy is acceptable;
   - whether the 7-day recovery copy can be switched off for short-lived sandboxes;
   - the scope of operator "infrastructure-level access".

## Sources

| Source | Used for |
|---|---|
| [Agent37 homepage](https://www.agent37.com) | Product, pricing, vendor comparison, customers, security claims |
| [Agent37 docs](https://www.agent37.com/docs) and [docs index](https://www.agent37.com/docs/llms.txt) | Platform features, templates, product patterns, integrations |
| [Terms of service](https://www.agent37.com/terms) (4 Aug 2026) | Acceptable use, customer responsibility, data ownership |
| [Privacy policy](https://www.agent37.com/privacy) (1 Sep 2026) | Data collected, retention, sub-processors, SOC 2 status |
| [Report abuse](https://www.agent37.com/abuse) (21 Sep 2026) | Abuse handling |
| [LegitTool review](https://legittool.com/review/agent37com/) | Detection of the August–September 2026 policy rewrites |

## Open gaps

- Funding, team size, revenue and founders not found.
- Data-centre locations and underlying cloud providers not published.
- No independent benchmark of sandbox performance or cold-start times.
- Pricing of Perflo paid tools and the managed model router per call not checked in detail.
- Not tested: how the price guarantee and startup credits work in practice.
