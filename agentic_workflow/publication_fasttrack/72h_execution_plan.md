# 72-Hour Fast-Track Plan (Automation in Construction)

## Goal
Submit a **framework + preliminary implementation** paper with credible quantitative evidence in 3 days.

## Hard Scope Lock (Do not expand)
- Domain: HS/TRHS only
- Clauses: 1 completed multi-condition clause (2.10) + 4 additional clauses max
- Baseline: deterministic single-hypothesis check
- Proposed: agentic workflow + SafetyGate
- Models: keep fixed (no model sweep)
- Runs: single fixed config + one repeat run for sanity

## Deliverables by deadline
1. Reproducible experiment artifacts (inputs, outputs, run traces)
2. One core results table + one ablation table
3. One error analysis table
4. Revised manuscript section: "Preliminary Implementation and Pilot Results"

## Day 1 (Today): Dataset + Pipeline Freeze

### 1) Freeze benchmark set
- Select exactly 5 clauses:
  - include Clause 2.10 (multi-condition)
  - include at least 2 low-ambiguity clauses
  - include at least 2 ambiguity-prone clauses
- For each clause, define:
  - expected compliance label (ground truth)
  - rationale note (1-2 lines)

### 2) Freeze pipeline config
- Fix provider/model/prompt versions
- Fix SafetyGate thresholds (Tier A/Tier B)
- Record all config into a single JSON/YAML file

### 3) Execute baseline + proposed
- Run baseline once on full set
- Run proposed once on full set
- Save traces to Supabase and local JSON outputs

### Exit criteria (Day 1)
- You can compute: TP, FP, TN, FN, abstention count per clause and total

## Day 2: Metrics + Ablation + Error Analysis

### 1) Compute core metrics
- Precision, Recall, F1
- False Negative Rate (critical)
- Abstention coverage
- Auto-approval rate

### 2) Run 2 minimal ablations
- Ablation A: proposed without SafetyGate
- Ablation B: single-hypothesis only (no multi-hypothesis branch)

### 3) Build 1-page error analysis
- Top 5 failures/escalations
- Categorize: parsing ambiguity, representational ambiguity, missing evidence, threshold sensitivity

### Exit criteria (Day 2)
- Finalized results table + ablation table + error taxonomy table

## Day 3: Manuscript Patch + Final QC

### 1) Patch paper sections
- Abstract: change "future work only" language to include preliminary pilot
- Methods: add implementation subsection (actual pipeline)
- Results: add quantitative tables
- Discussion: bounded claims + limitations

### 2) Add reproducibility appendix
- Data scope, fixed config, run IDs, repo path, Supabase schema

### 3) Final checks
- Remove placeholders (author/email/funding)
- Verify references and overclaims
- Prepare cover letter positioning: "framework + preliminary implementation with pilot evidence"

### Exit criteria (Day 3)
- Submission-ready PDF + supplementary artifacts

---

## Minimum acceptable numbers (internal target)
- Proposed method should improve or match baseline on Recall
- False negatives should reduce vs baseline (especially safety-critical clauses)
- Abstentions should be explainable and not random

## If you are blocked
- Reduce scope to 3 clauses total (2.10 + 2 others)
- Keep only 1 ablation (without SafetyGate)
- Submit with explicit statement: preliminary pilot, expanded validation ongoing
