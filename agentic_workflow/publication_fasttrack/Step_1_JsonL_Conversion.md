# Step 1 — JSONL Conversion (Implementation Record)

## Purpose
This document records the full execution of **requirements/regulations to machine-readable JSONL conversion** for publication evidence and implementation traceability.

Use this as the authoritative log for:
- what was converted,
- how conversion was performed,
- which AI/tools/configs were used,
- what quality gates passed/failed,
- what outputs were approved.

This Step 1 record also documents explicit alignment with the **MHI framework**:
- multi-hypothesis extraction and comparison,
- confidence calibration and uncertainty handling,
- risk-tiered abstention/escalation policy,
- auditable decision package outputs.

---

## 1) Run Metadata
- Run ID:
- Date/Time (start):
- Date/Time (end):
- Operator(s):
- Reviewer(s):
- Project/Repo:
- Branch + Commit Hash:
- Environment (local/cloud):
- Supabase project/table target:

---

## 2) Source Inputs
### 2.1 Documents
| Doc ID | File Name | Version | Jurisdiction | Domain | Pages Used | Notes |
|---|---|---|---|---|---|---|
| | | | | | | |

### 2.2 Scope for this run
- Clause families included:
- Clause IDs included:
- Exclusions (if any):
- Reason for exclusions:

### 2.3 Ground-truth/Reference material
- Existing checklists used:
- Prior approved JSONL version (if any):
- Reviewer reference links:

---

## 3) Conversion Configuration
### 3.1 Canonical schema
- Schema file:
- Schema version:
- Required fields:

### 3.2 Extraction approach
- Segmentation method (rule-based/AI/hybrid):
- Extraction method (NLP/LLM/combined):
- Verification method (single-pass/two-pass/critic):
- Orchestration framework (none/LangChain/LangGraph/custom):
- Agent-role design used (extractor/critic/calibrator/safety-gate/reviewer):
- Fallback strategy (deterministic parser when LLM fails):

### 3.3 AI model settings
| Stage | Provider | Model | Temperature | Max tokens | Prompt version |
|---|---|---|---:|---:|---|
| Clause segmentation | | | | | |
| Clause extraction | | | | | |
| Critic/verification | | | | | |

### 3.4 Token + cost tracking
| Stage | Input tokens | Output tokens | Total tokens | Estimated cost |
|---|---:|---:|---:|---:|
| Segmentation | | | | |
| Extraction | | | | |
| Verification | | | | |
| **Total** | | | | |

### 3.4a Token efficiency controls
- Clause-level chunking enabled (Y/N):
- Prompt compression enabled (Y/N):
- Caching enabled (Y/N):
- Parallel execution enabled (Y/N):
- Retry policy (max retries / triggers):
- Budget guardrail (max total tokens per run):
- Budget guardrail action on exceed (stop/escalate/degrade model):

### 3.5 MHI/CCS alignment settings
- Multi-hypothesis enabled (Y/N):
- Max hypotheses per clause (`k`):
- Hypothesis ranking method:
- Confidence calibration method (e.g., temperature scaling):
- CCS/decision confidence definition used:
- ECE target threshold:
- Epistemic uncertainty metric used (entropy/variance):
- Epistemic uncertainty threshold:
- Risk tier policy used (A/B/C):
- Auto-approve thresholds by tier:
- Abstention/escalation policy trigger:

### 3.6 Implementation stack choices
- Programming language used (recommended: Python):
- NLP libraries used (regex/spaCy/custom parser):
- LLM framework used (LangChain/LangGraph/custom):
- Schema validation library (jsonschema/pydantic):
- Storage/logging backend (Supabase/local files):
- Why this stack was selected (speed/cost/privacy/reproducibility):

### 3.7 Alternative methods considered
- NLP-only pipeline considered (Y/N), decision:
- LLM-only pipeline considered (Y/N), decision:
- Hybrid NLP+LLM selected (Y/N), rationale:
- Local model option assessed (e.g., Ollama) (Y/N), rationale:

---

## 4) Pipeline Steps Executed
## Step A — Ingestion & normalisation
- Tooling used:
- OCR needed (Y/N):
- Output artefact(s):

## Step B — Clause segmentation
- Clause detection strategy:
- Parent-child clause mapping method:
- Output artefact(s):

## Step C — Structured extraction to JSONL
- Field mapping strategy:
- Unit normalization strategy:
- Ambiguity tagging strategy:
- Output artefact(s):

### MHI-specific extraction checks (required)
- Are alternative interpretations captured for ambiguous clauses? (Y/N)
- Are assumptions recorded per hypothesis? (Y/N)
- Are clause-path justifications recorded? (Y/N)
- Are ambiguity classes tagged per clause (`intentional`, `linguistic`, `tacit_knowledge`, `representational`)? (Y/N)

## Step D — Quality gates
- Schema validation pass rate:
- Contradiction checks:
- Missing field checks:
- Low-confidence/escalation count:

## Step F — Efficiency and model routing
- Tiered model routing enabled (cheap-first, strong-model-on-escalation) (Y/N):
- Routing rules:
- Clauses routed to higher model count:
- Latency per stage (p50/p95):
- Cost per stage and per accepted clause:

## Step G — Governance, security, and compliance
- Data classification of source docs:
- Any sensitive data redaction applied (Y/N):
- API key handling method:
- Prompt/output logging policy:
- Human reviewer accountability fields recorded (Y/N):
- Regulatory/legal review checkpoints included (Y/N):

## Step E — Human review & approval
- Clauses sent to review:
- Clauses approved without edits:
- Clauses edited:
- Clauses rejected:

---

## 5) Quality Results (for publication)
### 5.1 Structural quality
| Metric | Value |
|---|---:|
| Total clause records | |
| Valid JSON lines | |
| Schema-pass records | |
| Schema-fail records | |

### 5.2 Semantic quality
| Metric | Value |
|---|---:|
| Exact clause ID match rate | |
| Numeric threshold extraction accuracy | |
| Unit extraction accuracy | |
| Applicability extraction accuracy | |

### 5.3 Safety/ambiguity handling
| Metric | Value |
|---|---:|
| Records with ambiguity flags | |
| Escalated records (`abstain_escalate`) | |
| Auto-approved records | |
| Reviewer override count | |

### 5.4 MHI/CCS metrics (framework-critical)
| Metric | Value |
|---|---:|
| Avg hypotheses per clause | |
| Clauses with `k>1` hypotheses | |
| Hypothesis agreement rate | |
| Expected Calibration Error (ECE) | |
| Avg epistemic uncertainty | |
| Risk-coverage (accepted coverage) | |
| False negative rate (Tier A clauses) | |

### 5.5 Efficiency metrics (engineering-critical)
| Metric | Value |
|---|---:|
| Total run time | |
| Cost per run | |
| Cost per clause | |
| Clauses/hour throughput | |
| Escalation-to-approval turnaround | |
| Cache hit rate | |

### 5.6 Error taxonomy
| Error type | Count | Example clause IDs | Fix applied |
|---|---:|---|---|
| Clause segmentation error | | | |
| Numeric parsing error | | | |
| Unit normalization error | | | |
| Applicability misread | | | |
| Hallucinated constraint | | | |

---

## 6) Output Artefacts
### 6.1 Files produced
| Artefact | Path | Version | Notes |
|---|---|---|---|
| Raw segmented clauses | | | |
| JSONL draft | | | |
| JSONL verified | | | |
| Review log | | | |
| Hypothesis trace log | | | |
| Decision package log (clause path/assumptions/confidence/escalation) | | | |
| Final approved JSONL | | | |

### 6.2 Supabase persistence
- workflow_runs run_id:
- clause_traces count:
- Upload timestamp:
- Source tag (`WORKFLOW_SOURCE`):

---

## 7) Reproducibility Checklist
- [ ] Source documents/version fixed
- [ ] Clause scope fixed
- [ ] Prompt versions fixed
- [ ] Model/provider fixed
- [ ] Schema version fixed
- [ ] MHI settings fixed (`k`, thresholds, calibration method)
- [ ] Model routing rules fixed
- [ ] Seed/settings fixed for deterministic replay where possible
- [ ] Validation scripts archived
- [ ] Output JSONL checksum recorded
- [ ] Commit hash recorded

Checksum(s):
- final_jsonl_sha256:

---

## 8) Publication-ready Summary (copy to manuscript)
### 8.1 Implementation statement (draft)
> We implemented a regulation-to-JSONL conversion pipeline using a hybrid deterministic/agentic extraction workflow with schema-constrained outputs, verifier pass, and human review for low-stability records.

### 8.2 Pilot scope statement (draft)
> The preliminary conversion covered [N] clauses across [phase families], producing [N] machine-readable records with a schema pass rate of [X]%, and [Y] records escalated for manual confirmation.

### 8.3 Limitation statement (draft)
> This preliminary implementation is scoped to [domain/jurisdiction] and does not yet generalize across all clause families or document formats.

---

## 9) Sign-off
- Engineering lead:
- Domain reviewer:
- QA reviewer:
- Date:

---

## 10) Method Decision Matrix (fill once per project)
| Option | Accuracy on ambiguous clauses | Cost | Speed | Explainability | Recommended use |
|---|---|---|---|---|---|
| NLP-only | | | | | |
| LLM-only | | | | | |
| Hybrid NLP + Agentic LLM + Validation | | | | | |

Decision taken:
- Selected approach:
- Why selected for this project:

### 10.0 Comparison criteria (use for formal justification)
Evaluate each method on a 1-5 scale:
1. Ambiguity handling quality
2. Numerical/units extraction reliability
3. Hallucination risk control
4. Reproducibility and auditability
5. Human-review efficiency
6. Cost efficiency at scale
7. Time-to-first-results
8. Safety suitability (Tier A false-negative control)

Record scoring:
| Criterion | NLP-only | LLM-only | Hybrid |
|---|---:|---:|---:|
| Ambiguity handling quality | | | |
| Numerical/units reliability | | | |
| Hallucination risk control | | | |
| Reproducibility/auditability | | | |
| Human-review efficiency | | | |
| Cost efficiency at scale | | | |
| Time-to-first-results | | | |
| Safety suitability (Tier A) | | | |
| **Total** | | | |

## 10.1 Practical options (pre-filled)

### Option A — NLP-only deterministic pipeline
- Description: regex/rule parser + deterministic field extraction without LLM reasoning.
- Strengths: low cost, fast, stable on strict numeric clauses.
- Limits: weak on ambiguity, cross-references, and contextual interpretation.
- Best for: low-ambiguity clauses and high-throughput first-pass filtering.

Comparison notes:
- Better than LLM-only for deterministic numeric extraction consistency.
- Worse than Hybrid for ambiguity-heavy clauses and contextual applicability.
- Strong baseline for ablation and first-pass routing.

### Option B — LLM-only direct extraction
- Description: single-pass or multi-pass LLM converts raw clause text directly to JSONL.
- Strengths: flexible interpretation and faster prototyping.
- Limits: hallucination risk, inconsistency, weaker repeatability without strict guards.
- Best for: early exploration and low-volume experiments.

Comparison notes:
- Faster setup than Hybrid, but weakest governance and repeatability under strict safety requirements.
- Higher rework risk due to output inconsistency and hallucinations without deterministic guards.

### Option C — Hybrid NLP + Agentic LLM + Validation (**Recommended**) 
- Description: deterministic segmentation + agentic extraction/verification + schema and safety gates.
- Strengths: best balance of accuracy, scalability, auditability, and safety.
- Limits: moderate complexity and orchestration overhead.
- Best for: publication-grade implementation and production-oriented ACC workflows.

Comparison notes:
- Outperforms NLP-only on ambiguous/contextual clauses.
- Outperforms LLM-only on reliability, explainability, and release confidence.
- Most aligned with MHI novelty because it operationalizes multi-hypothesis + uncertainty + abstention.

## 10.2 Best recommendation (default)
- **Recommended default:** Option C (Hybrid NLP + Agentic LLM + Validation).
- **Why:** It aligns with MHI novelty (multi-hypothesis + CCS + abstention), supports reproducibility, and reduces false confidence on ambiguous clauses.
- **Execution policy:**
	1. Run deterministic/NLP first-pass on all clauses.
	2. Route ambiguous or low-confidence clauses to agentic extraction + critic.
	3. Enforce schema/consistency/safety gates before JSONL acceptance.
	4. Escalate unresolved clauses to human review.

### 10.2b Justification summary (publication-ready)
Use this wording in methods/discussion:
> We selected a hybrid deterministic-agentic pipeline because it provides the strongest combined performance on ambiguity handling, safety-governed decision quality, and auditability. Compared with NLP-only approaches, it better captures context-dependent and linguistically ambiguous requirements through controlled multi-hypothesis extraction. Compared with LLM-only extraction, it reduces hallucination and inconsistency via schema constraints, independent critic verification, and risk-tiered abstention rules. This directly supports the MHI objective of reliable automation with explicit uncertainty management in safety-critical compliance checking.

### 10.2c Decision evidence checklist
- [ ] Scoring table completed with evidence notes
- [ ] At least one ambiguous clause compared across all three methods
- [ ] Tier A false-negative behavior compared across methods
- [ ] Cost/time comparison recorded (per clause and per run)
- [ ] Final recommendation signed off by engineering + domain reviewer

## 10.2a Detailed implementation method (recommended)

### A) Agent roles (minimum viable)
1. **Segmentation Agent (deterministic-first)**
	- Input: normalized document text
	- Output: clause blocks with `clause_id`, heading, source anchors
	- Method: regex/rule parser; fallback to LLM only for malformed layouts

2. **Extraction Agent (structured output)**
	- Input: one clause block
	- Output: JSON object conforming to canonical schema
	- Method: schema-constrained generation (strict JSON mode)

3. **Hypothesis Agent (MHI branch)**
	- Trigger: ambiguity-prone clauses or low-confidence extraction
	- Output: `k` candidate interpretations with assumptions and confidence priors
	- Method: generate alternatives only where ambiguity flags apply

4. **Critic/Verifier Agent**
	- Input: extracted record(s) + source text
	- Output: pass/fail checks and correction proposals
	- Checks: contradiction, unit mismatch, missing constraints, clause-path mismatch

5. **SafetyGate Agent**
	- Input: confidence + uncertainty + risk tier
	- Output: `auto_approve` or `abstain_escalate`
	- Policy: stricter thresholds for Tier A

6. **Reviewer-in-the-loop**
	- Trigger: `abstain_escalate`, unresolved critic conflicts, policy exceptions
	- Output: approved/edited record with reviewer sign-off

### B) Step-by-step flow
1. Ingest and normalize document.
2. Deterministically segment clauses and store anchors.
3. For each clause, run extraction in strict schema mode.
4. Compute extraction confidence and ambiguity flags.
5. If ambiguous/low-confidence, run MHI hypothesis branch (`k=2..3` for pilot).
6. Run critic verification pass (independent prompt).
7. Apply SafetyGate thresholds and decide auto-approve vs escalate.
8. Persist outputs and traces (local JSONL + Supabase).
9. Generate release JSONL only from approved records.

### C) Practical routing rules
- **Route to MHI branch when any is true:**
  - ambiguity flag present,
  - critic detects contradiction,
  - confidence below threshold,
  - clause is Tier A and involves qualitative terms.

- **Tier policy (initial):**
  - Tier A: require high confidence and low uncertainty; otherwise escalate.
  - Tier B/C: allow broader auto-approval envelope.

### D) Prompt and output controls
- Use versioned prompt IDs per stage.
- Force canonical field names and units.
- Disallow empty required fields.
- Require explicit `escalation_trigger` for non-auto decisions.

### E) Acceptance criteria for each clause record
- Schema valid = true
- Source anchor present (`file`, `page`, optional line range)
- No unresolved critic errors
- SafetyGate decision recorded
- Reviewer sign-off for escalated records

### F) Pilot defaults (for fast execution)
- Hypotheses per ambiguous clause: `k=2`
- Max retries per stage: `2`
- Critic pass required: `yes`
- Escalation on unresolved conflict: `mandatory`
- Release condition: `100% schema pass` + `0 unresolved Tier A critic issues`

### G) Common failure modes and fixes
- **Missing units** → enforce unit dictionary + critic unit check
- **Clause merge/split errors** → lock deterministic clause splitter and compare against clause index
- **Hallucinated constraints** → require source quote span for each new constraint
- **Overconfident wrong extraction** → calibrate confidence and enforce Tier A abstention

## 10.3 Fast fallback recommendation (deadline mode)
- If time-critical, use **A + selective C**:
	- NLP-only for straightforward clauses,
	- Hybrid path only for high-risk or ambiguity-prone clauses.
- This preserves quality where it matters while controlling cost/time.

---

## 11) Improvement Backlog (future runs)
- [ ] Add retrieval-augmented clause context (cross-reference handling)
- [ ] Add automatic contradiction graph across clauses
- [ ] Add calibration post-processing job for confidence scores
- [ ] Add active-learning loop from reviewer corrections
- [ ] Add benchmark suite across multiple regulation families
- [ ] Add release-quality score threshold before JSONL publication
