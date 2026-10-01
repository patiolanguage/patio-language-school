-- Patio Language School: Practical AI courses
-- Migration 0001: registration-of-interest table
--
-- Apply with the Supabase SQL editor, or the Supabase CLI:
--   supabase db push            (if the project is linked)
-- or paste this file into: Supabase dashboard -> SQL Editor -> New query -> Run.
--
-- Design notes
--   * One row per normalized (lower-cased, trimmed) email address.
--   * Allowed values for course_interest and preferred_slot are enforced by
--     CHECK constraints so bad data can never reach the table, even if the
--     server validation is bypassed.
--   * Row Level Security is ON with NO policies, so the anon/public API key
--     can neither read nor write. Only the service_role key (used server-side
--     by the Pages Function, and which bypasses RLS) can insert rows.

create extension if not exists "pgcrypto";  -- for gen_random_uuid()

create table if not exists public.ai_course_interest (
  id              uuid         primary key default gen_random_uuid(),
  email           text         not null,
  course_interest text         not null,
  preferred_slot  text         not null,
  created_at      timestamptz  not null default now(),

  constraint ai_course_interest_email_key unique (email),

  constraint ai_course_interest_email_check
    check (char_length(email) between 3 and 254 and position('@' in email) > 1),

  constraint ai_course_interest_course_check
    check (course_interest in ('ai_made_simple', 'ai_for_business', 'either')),

  constraint ai_course_interest_slot_check
    check (preferred_slot in ('wed_afternoon', 'wed_evening', 'fri_afternoon', 'fri_evening'))
);

-- Row Level Security: enabled, with no policies granted to anon/authenticated.
-- With RLS on and no permissive policy, PostgREST requests made with the
-- public anon key return zero rows and cannot insert. The server endpoint uses
-- the service_role key, which bypasses RLS.
alter table public.ai_course_interest enable row level security;
alter table public.ai_course_interest force row level security;

-- Explicitly ensure the exposed API roles have no table privileges either.
revoke all on table public.ai_course_interest from anon, authenticated;

comment on table public.ai_course_interest is
  'Practical AI course registrations of interest. Written only by the server-side Pages Function via the service_role key. RLS blocks all anon/public access.';
