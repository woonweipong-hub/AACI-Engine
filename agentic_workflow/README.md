# Agentic Workflow Sandbox (Research Folder)

This folder is a standalone sandbox for developing your agentic AI compliance workflow without touching AECOA production code.

## Files
- `safety_gate.py` - Risk-tier decision policy (`auto_approve` vs `abstain_escalate`)
- `workflow_orchestrator.py` - Minimal orchestration and trace generation
- `example_run.py` - Pilot-style sample run for TRHS clauses
- `supabase_store.py` - Optional Supabase persistence client (REST)
- `supabase_schema.sql` - SQL schema for `workflow_runs` and `clause_traces`
- `supabase_dashboard_queries.sql` - Ready-to-run KPI and monitoring queries
- `.env.example` - Environment variables template for Supabase

## Quick run
From the workspace root:

```powershell
c:/2026_Research/.venv/Scripts/python.exe c:/2026_Research/agentic_workflow/example_run.py
```

### Multi-clause run (recommended)

```powershell
c:/2026_Research/.venv/Scripts/python.exe c:/2026_Research/AACI-Engine/agentic_workflow/batch_run.py
```

With Supabase upload:

```powershell
c:/2026_Research/.venv/Scripts/python.exe c:/2026_Research/AACI-Engine/agentic_workflow/batch_run.py --upload
```

Output file:
- `agentic_workflow/outputs/pilot_run_trace.json`
- `agentic_workflow/outputs/multi_clause_run_trace.json`

Input example for multiple clauses:
- `agentic_workflow/inputs/clauses_input_example.json`
- Includes `TRHS-2.1` and additional clauses for batch execution.

## Supabase integration (optional)
1. In your Supabase SQL Editor, run:
	- `agentic_workflow/supabase_schema.sql`
2. Copy `.env.example` to `.env` and set:
	- `SUPABASE_URL`
	- `SUPABASE_SERVICE_ROLE_KEY`
3. In PowerShell before running:

```powershell
$env:SUPABASE_URL="https://mevfmqbrtovdmzmbaals.supabase.co"
$env:SUPABASE_SERVICE_ROLE_KEY="<your-service-role-key>"
$env:WORKFLOW_SOURCE="agentic_workflow_example"
```

4. Run `example_run.py` again. It will:
	- save local JSON trace, and
	- upload `workflow_runs` + `clause_traces` to Supabase.

## Dashboard queries
- Open Supabase SQL Editor and run queries from:
	- `agentic_workflow/supabase_dashboard_queries.sql`
- Included analytics:
	- run-level auto-approval trend,
	- escalation hotspots by clause,
	- confidence bucket distribution,
	- risk-tier behavior,
	- latest run trace breakdown.

## Publication fast-track kit (72h)
- For urgent submission preparation, use:
	- `agentic_workflow/publication_fasttrack/72h_execution_plan.md`
	- `agentic_workflow/publication_fasttrack/FRAMEWORK_SCOPE_CLAUSE_REQUIREMENTS.md`
	- `agentic_workflow/publication_fasttrack/TRHS_THREE_PHASE_CLAUSE_EXTRACTS.md`
	- `agentic_workflow/publication_fasttrack/results_table_template.csv`
	- `agentic_workflow/publication_fasttrack/manuscript_patch_checklist.md`

## How to extend next
1. Replace `sample` in `example_run.py` with real clause outputs from your parser/analyzer.
2. Add per-clause metadata: model, provider, prompt version, source page/sheet.
3. Add calibration post-processing to convert raw scores into calibrated confidence.
4. Add a reviewer feedback file and update thresholds per risk tier.

For multiple-clause scaling, prefer `batch_run.py` with JSON/CSV inputs rather than editing `example_run.py`.
