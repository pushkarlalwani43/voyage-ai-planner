-- Run in Supabase SQL Editor when you are ready to add persistence.
create table if not exists public.trips (
  id uuid primary key default gen_random_uuid(),
  user_id uuid references auth.users(id) on delete cascade,
  destination text not null,
  start_date date not null,
  end_date date not null,
  budget integer not null check (budget > 0),
  travelers integer not null default 1 check (travelers > 0),
  preferences jsonb not null default '{}'::jsonb,
  itinerary jsonb not null default '{}'::jsonb,
  created_at timestamptz not null default now()
);

alter table public.trips enable row level security;
create policy "Users manage their own trips" on public.trips
  for all using (auth.uid() = user_id) with check (auth.uid() = user_id);
