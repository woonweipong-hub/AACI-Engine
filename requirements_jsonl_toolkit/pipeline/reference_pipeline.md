# Generic Regulation-to-JSONL Pipeline (Reusable)

## Stage 0 — Ingestion
Input formats:
- PDF, DOCX, HTML, TXT

Outputs:
- normalized text blocks with page/section anchors

## Stage 1 — Clause segmentation
- detect clause IDs (e.g., 2.4.3(c), 4.2(b))
- split into atomic obligation statements
- preserve parent-child references

## Stage 2 — Semantic extraction
For each atomic clause:
- requirement_type
- constraints (field/operator/value/unit)
- applicability conditions
- evidence requirements
- ambiguity flags
- review policy

## Stage 3 — Validation
- schema validation
- contradiction detection
- cross-clause consistency checks
- low-confidence extraction routing to human review

## Stage 4 — Approval workflow
- reviewer edits and final approval
- versioning of clause records
- changelog with reason and author

## Stage 5 — Publication/use
- export JSONL for check engine
- optional SQL/Supabase sync for audit and analytics

## Accuracy strategy (key)
1. Constrain output via strict schema
2. Use two-pass extraction:
   - Pass A: raw clause structuring
   - Pass B: independent verifier pass
3. Compute disagreement and escalate
4. Keep gold-set benchmark and run regression tests after every prompt or parser change
