# Web UI Blueprint for Requirements-to-JSONL Tool

## Core modules
1. Upload & Parsing
- Upload regulation documents
- Show parsed clause tree with page links

2. Clause Workbench
- Left: source text
- Right: JSON form editor (schema-driven)
- Buttons: validate, suggest extraction, compare revisions

3. Quality Gate Panel
- schema pass/fail
- ambiguity flags
- missing fields
- contradiction alerts

4. Reviewer Workflow
- assign clauses to reviewer
- approve/reject with comments
- audit log and timestamps

5. Export & Integration
- export JSONL
- push to Supabase
- version tags and release notes

## Minimal backend API endpoints
- POST /documents
- GET /documents/{id}/clauses
- POST /clauses/{id}/extract
- POST /clauses/{id}/validate
- POST /clauses/{id}/approve
- GET /exports/{document_id}.jsonl

## Data model essentials
- documents
- clauses_raw
- clauses_canonical
- reviews
- releases

## Recommended implementation order
1. schema + validator first
2. clause editor second
3. extraction assistant third
4. review/approval workflow fourth
5. export/release controls last
