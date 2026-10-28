# 5. Content policy and trust & safety

[Back to wiki home](README.md)

## Principle

We can keep a strong privacy promise and still block illegal use. The promise is **"nobody stores or reads your conversations"**, not "nothing ever checks them". Automated checks that run in memory and keep nothing are compatible with that promise, as long as we disclose them. Venice and end-to-end encrypted messaging apps work the same way.

Suggested privacy wording:

> We never store your conversations, and no human ever reads them. Automated safety checks run in real time and keep nothing.

Avoid "we see nothing and check nothing". It is not true of a responsible service and creates legal exposure later (see [page 6](06-legal-risks.md)).

## Sexual and obscene content

We will not market or design for sexual use cases. We can't see conversations, so we can't police every one. What we can do is show that the product was designed to discourage that use and that we don't profit from it.

| Control | Detail |
|---|---|
| Model defaults | System prompts and model choices decline explicit sexual content. Don't serve erotica-tuned models. Some explicit text will slip through on open models; that's acceptable if the default product doesn't produce it and our terms ban it |
| Image output filter | Block **all** nudity in generated images with an in-memory nudity classifier. Reliable and cheap, and it removes most of the child abuse risk |
| Risky features removed | No "undress" or image editing of uploaded photos of real people. No user-uploaded LoRAs or custom checkpoints. No public galleries or sharing at launch |
| Age gate | 18+ with an age check at signup |
| Account-level enforcement | Suspend accounts that keep triggering blocks. Store a counter, not the conversation, and disclose this |
| Clean marketing | No "NSFW" or "no limits" anywhere. Payment processors, app stores and regulators judge us mainly by marketing and default behaviour. This is also what gets us a normal merchant account |

## Blocking child sexual abuse material (CSAM)

This is achievable to a high standard with layers that all run in memory.

| Layer | What it does | Privacy impact |
|---|---|---|
| Prompt classifier | Blocks requests combining minors with sexual content, in text and image prompts | None; nothing stored |
| Output image classifiers | Nudity detector plus age estimator on every generated image; flagged images discarded | None |
| Hash matching on uploads | Compares uploaded images with databases of known abuse material (Microsoft PhotoDNA, Thorn Safer, NCMEC hash list, Internet Watch Foundation list) | Only an image fingerprint is compared |
| Model choice | Base image models trained on filtered data; never community models tuned for explicit content | None |
| Agent browsing blocklist | Blocks the agent from known abuse URLs (Internet Watch Foundation and Thorn URL lists) | None |
| Account enforcement | Suspend repeat offenders; store only a flag | Minimal, disclosed |

### Two design points

1. **Classifiers run inside the encrypted enclave too.** In TEE and E2EE modes, the safety classifiers sit inside the same hardware-sealed enclave as the model. Requests are checked without us or the GPU provider seeing them, so even the strongest privacy tier is not an unmoderated space.
2. **Disclose the one exception.** If someone uploads an image matching *known* abuse material, we are likely legally required to block it, keep minimal evidence and report it. US providers must report to NCMEC. UAE child protection law (Federal Law No. 3 of 2016, "Wadeema's Law") imposes reporting duties; counsel to confirm how they apply. State this exception in the privacy policy, as encrypted messaging apps do.

### Honest limits

Text-only abuse roleplay can't be blocked 100% on open models. Classifiers reduce it heavily, and fine-tuning the main model to refuse helps more. Legally, what matters is documented, reasonable safeguards and a fast response to reports, so provide a user-facing "report a problem" channel.

## Organisations and tools

| Organisation / tool | Provides |
|---|---|
| Thorn | Safer (hash matching) and Safer Predict (classifiers for new material) |
| Internet Watch Foundation | Hash and URL lists; accepts non-UK members |
| Microsoft PhotoDNA | Hash matching |
| Google Content Safety API | Classifier for previously unseen material; available to qualifying organisations |
| NCMEC | Hash lists and the US reporting channel |
| StopNCII.org | Hashes for non-consensual intimate imagery |
| Hive | Commercial moderation API |

At our scale the cost is small and fits inside the $15–25k/month legal and compliance line in the [financial model](02-financial-model.md).

## Hard refusals regardless of privacy mode

"Uncensored" does not cover:

- Sexual content involving minors.
- Non-consensual intimate imagery and sexual deepfakes of real people.
- Meaningful help with weapons, especially chemical, biological, radiological or nuclear weapons.
- Malware and attacks on systems the user doesn't own.
