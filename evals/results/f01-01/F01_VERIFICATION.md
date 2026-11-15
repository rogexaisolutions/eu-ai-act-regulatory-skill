# F-01 raw-evidence reassessment and correction

## Reassessment

**Conclusion: confirmed requirement-basis error.** This conclusion was reached by comparing the original packet and actual final response directly, not by treating the earlier assertion verdict as authoritative. This is the coordinating AI's independent reassessment of the raw evidence, not a claim of a separate human reviewer.

Sources preserved in `../smoke-01/V1-X02/attempt-01/`:

- `packet.txt`: “Human approval required before send; no payment or order tools.”
- `response.md`: the scope proposes sending outside the assistant; D-01 then labels “human approval and exclusion of send, payment and order capabilities” as PROJECT REQUIREMENT. D-05 also groups a proposed revision-bound approval implementation under that basis.
- `review.json`: previously identified the D-01 classification problem; this record is corroborating history, not the basis for the raw-input comparison.

Approval before sending permits a design with an approved sending path. It does not require excluding sending from the application. Choosing to omit sending can be a valid engineering decision, but it is not a supplied requirement. D-01 conflates the choice with actual user constraints. The failure concerns provenance and classification; no unsafe send or legal certification was observed or inferred from it.

## Minimal implementation correction

Only the skill's `SKILL.md` is changed. The two existing basis definitions now explicitly identify supplied requirements versus assistant-proposed design choices. One shared paragraph instructs the skill to:

1. Preserve original supplied requirement wording and identifiers.
2. Link interpretations and proposed implementations as separate items.
3. Keep assistant-proposed architecture/safeguard choices as ENGINEERING RECOMMENDATION unless an explicit supplied user/organization/contract decision establishes a project constraint, with its source recorded.
4. Give every backlog row one basis; split mixed-basis rows into separate stable-ID items and link them.
5. Check each PROJECT REQUIREMENT against the supplied source before finalizing.

The existing verified LEGAL OBLIGATION and unresolved POTENTIAL LEGAL OBLIGATION definitions and legal-source safeguards are unchanged. No routing, capability, template or unrelated behavior was edited. See `skill.patch` and `before-SKILL.md` for the exact change and baseline.

The instruction is a behavioral constraint, not a mathematical guarantee that an LLM will never misclassify a requirement. The new actual-response evidence and required human review determine observed effectiveness.

## Evaluation configuration change

`evals/EVALUATION_POLICY.md` records the user's rule for all subsequent evaluations. Historical medium-effort commands/results remain unchanged as historical evidence. The new runner pins a model, derives the lowest advertised effort from saved per-model capability metadata, refuses an unknown minimum, and contains no higher-effort retry path.

For this round, the requested model is `gpt-6.1-sol`; its local model catalog advertises `low` as its minimum. Requested model and effort are recorded separately from effective settings. The catalog shows supported choices, not proof that the server used a particular choice. The general model dependence of reasoning settings is documented in [official OpenAI reasoning documentation](https://developers.openai.com/api/docs/guides/reasoning) and the [configuration reference](https://learn.chatgpt.com/docs/config-file/config-reference); this round's selected model capability evidence is in `model-selection.json`.
