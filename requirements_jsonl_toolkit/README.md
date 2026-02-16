# Requirements-to-JSONL Toolkit (Generic, Reusable)

This toolkit defines how to build a reusable product that converts regulations/requirements into machine-readable JSONL accurately.

## What this gives you
- Canonical clause schema
- JSONL examples
- Extraction prompt baseline
- Quality gate checklist
- Reference pipeline
- Web UI architecture blueprint

## Files
- config/canonical_clause_schema.json
- config/jsonl_record_examples.jsonl
- prompts/clause_extraction_system_prompt.txt
- prompts/quality_gate_checklist.md
- pipeline/reference_pipeline.md
- ui/web_ui_blueprint.md

## How to use now
1. Start with your TRHS clause set as test corpus.
2. Map extracted records into canonical_clause_schema.json.
3. Run quality_gate_checklist.md before accepting any JSONL release.
4. Publish approved JSONL to your check engine and Supabase.

## Why this is generic
The schema and workflow are domain-agnostic. You can apply the same process to other technical regulations by only changing:
- field dictionary
- extraction prompts
- domain-specific evidence requirements
