# Framework, Scope, and Clause Requirements (Implementation Spec)

## Purpose
This document defines the **implementation-ready baseline** for the paper’s preliminary results section:
1) framework definition,
2) scope boundaries,
3) clause-level requirement catalogue for multi-clause runs.

This is the reference for moving from a single completed clause (Cl. 2.1) to a reproducible multi-clause pilot.

---

## 1) Framework Definition (What the system is)

### 1.1 Core paradigm
The system treats compliance checking as a **Multi-Hypothesis Inference (MHI)** process over 2D CAD evidence:
- generate plausible interpretations of clause requirements,
- evaluate compliance under each interpretation,
- quantify confidence/uncertainty,
- decide auto-approve vs abstain/escalate.

### 1.2 Operational pipeline
1. Input normalisation (DWG → DXF + evidence bundle)
2. Requirement structuring (TRHS clauses → JSONL rule artefacts)
3. Rule extraction and hypothesis generation
4. Fact extraction from drawings
5. Clause-level compliance evaluation
6. Stability/risk gating (SafetyGate)
7. Decision package output (verdict + confidence + assumptions + escalation reason)

### 1.3 Safety policy
- Use risk-tiered gating (`A` for life-safety critical, stricter thresholds).
- For low stability/high uncertainty cases, output `abstain_escalate` (not forced pass/fail).
- Persist complete decision trace for auditability (Supabase + JSON output).

---

## 2) Scope Boundaries (What is in / out for prelim publication)

### 2.1 In-scope (preliminary implementation)
- Domain: Household Shelter (HS) requirements (TRHS)
- Evidence mode: drawing/document-centric (2D CAD and related sheets)
- Workflow: three-phase HS checking
- Multi-clause pilot: clause set across measurement, setback, and components/M&E
- Outputs: clause-level compliance labels + gate decisions + trace logs

### 2.2 Out-of-scope (for this submission)
- Full BIM/IFC end-to-end deployment
- Large-scale cross-jurisdiction generalization
- Full production hardening and broad benchmark breadth

### 2.3 Publication-safe claim boundary
Position as:
- **Framework + preliminary implementation + pilot evidence**
- Not yet full-scale validation across all clause families and project types.

---

## 3) Three-Phase Checking Scope

## Phase 1 — Measurement (numeric geometry checks)
Focus: deterministic extraction and threshold checks from plans/sections/tables.

### Primary clause family
- Cl. 2.2.x, 2.3.x

### Typical checks
- HS width/length
- HS area/volume
- HS clear height
- HS wall thickness
- HS floor slab and top-most slab thickness

### Example clause details
- Cl. 2.2.1: minimum internal width (1.2m), maximum HS length (4m), area/volume constraints
- Cl. 2.2.2(a): HS clear height range (2.4m to 3.9m)
- Cl. 2.3.1: wall thickness requirements by HS clear height
- Cl. 2.3.2: slab thickness requirements (top-most slab and floor slab)

---

## Phase 2 — Spatial & Setback (context-conditioned checks)
Focus: clause applicability and geometric context (landed/basement/adjacency/setback envelopes).

### Primary clause family
- Cl. 2.4.x

### Typical checks
- Setback envelope compliance
- Air-well adjacency limits
- Trellis/setback relationship
- Shielding wall offset logic
- Basement HS conditions
- HS-lift common wall conditions

### Example clause details
- Cl. 2.4.1: HS position + air-well context
- Cl. 2.4.3 / 2.4.4: setback distance envelope requirements
- Cl. 2.4.3(c): trellis setback (e.g., 1m from nearest HS wall without door)
- Cl. 2.4.5: full-height shielding wall requirements (thickness/air-gap configurations)
- Cl. 2.4.6: HS in basement conditions
- Cl. 2.4.7: common wall with lift shaft (HS wall + additional thickness conditions)

---

## Phase 3 — Components & M&E
Focus: HS components, service provisions, dimensional clearances, and targeted escalation for ambiguous labels.

### Primary clause family
- Cl. 2.5, 2.7, 3.6, 4.2, 4.3, 2.13

### Typical checks
- Blast door opening and nib details
- Power/lighting/telephony outlet provisions and heights
- Conduit sealing depth
- Ventilation sleeve location and clearances
- False ceiling access panel
- HS wall recess for door handle

### Example clause details
- Cl. 2.5: blast door opening dimensions
- Cl. 2.5.2: nib/frame panel requirements
- Cl. 2.7.1–2.7.4: electrical services and installation height requirements
- Cl. 3.6.1(e): conduit sealing depth (e.g., minimum 100mm)
- Cl. 4.2(b): ventilation sleeves not located in toilets/bathrooms etc. (high ambiguity if room labels incomplete)
- Cl. 4.3: access panel requirements for external ventilation sleeve area
- Cl. 2.13: HS wall recess for door handle

---

## 4) Multi-Clause Pilot Set (Immediate)
Use this as minimum publishable pilot scope:

1. **Cl. 2.1** (completed) — include as already-implemented anchor clause
2. **Cl. 2.2.2(a)** — clear-height measurement check
3. **Cl. 2.4.3(c)** — trellis/setback (ambiguity-prone spatial check)
4. **Cl. 2.10** — multi-condition clause (existing PoC focus)
5. **Cl. 4.2(b)** — ventilation sleeve location with room-use label ambiguity

Optional 6th clause if time permits:
- Cl. 2.5 or Cl. 3.6.1(e)

---

## 5) Clause Record Contract (for batch runs)
Each clause entry should include:
- `clause_id`
- `compliance_label` (`pass`, `fail`, `conditional_pass`)
- `confidence` (0–1)
- `uncertainty` (0–1)
- `risk_tier` (`A`/`B`)
- `evidence_refs` (list)
- `assumptions` (list)

Use:
- `agentic_workflow/inputs/clauses_input_example.json`
- `agentic_workflow/batch_run.py`

---

## 6) Required Outputs for Paper Tables
For each run, capture:
- total clauses,
- auto-approved count,
- abstain/escalate count,
- per-clause gate action and reason,
- confidence/uncertainty distributions.

Persist to:
- local JSON trace (`agentic_workflow/outputs/*.json`)
- Supabase tables (`workflow_runs`, `clause_traces`)

---

## 7) Source Basis (where this spec was derived)
- `00_Papers/2025_MHI_Framework_for_automated_compliance_checking_arxiv_ready.txt`
- `00_Papers/_pdf_extract/HS_Checks_Scope.txt`
- `00_Papers/_pdf_extract/TRHS_requirements.txt`
- `AACI-Engine/agentic_workflow` implementation artifacts

---

## 8) Decision Rule for this submission
If deadline pressure increases:
- Keep only 5 clauses listed above,
- run baseline vs proposed + one ablation (without SafetyGate),
- prioritize false-negative reduction and explainable escalations over broad coverage.
