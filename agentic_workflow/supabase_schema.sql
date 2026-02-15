-- Run this in Supabase SQL editor
-- Creates tables for workflow-level and clause-level trace persistence.

create extension if not exists pgcrypto;

create table if not exists public.workflow_runs (
    id uuid primary key default gen_random_uuid(),
    created_at timestamptz not null default now(),
    run_timestamp timestamptz,
    source text,
    total_clauses integer not null default 0,
    auto_approved integer not null default 0,
    abstain_escalate integer not null default 0,
    raw_json jsonb not null
);

create table if not exists public.clause_traces (
    id uuid primary key default gen_random_uuid(),
    created_at timestamptz not null default now(),
    run_id uuid not null references public.workflow_runs(id) on delete cascade,
    clause_id text not null,
    compliance_label text,
    confidence double precision,
    uncertainty double precision,
    risk_tier text,
    gate_action text,
    gate_reason text,
    trace_json jsonb not null
);

create index if not exists idx_clause_traces_run_id on public.clause_traces(run_id);
create index if not exists idx_clause_traces_clause_id on public.clause_traces(clause_id);
create index if not exists idx_workflow_runs_created_at on public.workflow_runs(created_at desc);
