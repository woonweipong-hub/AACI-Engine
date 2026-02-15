# Manuscript Patch Checklist (Fast)

## Abstract
- [ ] Replace "full implementation in future work" with: "preliminary pilot implementation completed"
- [ ] Mention pilot scope explicitly (number of clauses, HS/TRHS context)
- [ ] Add 1 sentence on key quantitative outcome (e.g., reduced false negatives / calibrated abstention)

## Method Section
- [ ] Add subsection: Preliminary Implementation Pipeline
- [ ] Include actual pipeline stages executed in code
- [ ] Include SafetyGate decision policy and thresholds

## Results Section
- [ ] Table 1: Baseline vs Agentic core metrics
- [ ] Table 2: Ablation results
- [ ] Table 3: Error analysis categories
- [ ] Include 1 short paragraph on practical significance

## Discussion/Limitations
- [ ] State pilot scale limitations clearly
- [ ] Explain why abstentions are safety-aligned, not failures
- [ ] Avoid claims of broad generalization beyond HS/TRHS

## Reproducibility
- [ ] GitHub repo path and commit hash
- [ ] Supabase schema/tables used
- [ ] Fixed config (model, prompts, thresholds)
- [ ] Run IDs listed in appendix

## Submission hygiene
- [ ] Remove placeholders (name, affiliation, email, funding)
- [ ] Check references for consistency and formatting
- [ ] Ensure highlights match actual pilot evidence
