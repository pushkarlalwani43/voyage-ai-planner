# VoyageAI — Personalized Travel Itinerary Planner

An AI-inspired full-stack travel planner built for a college project. It creates structured, day-by-day itineraries from destination, dates, budget, group size, travel style, and interests.

![React](https://img.shields.io/badge/Frontend-React-61DAFB) ![FastAPI](https://img.shields.io/badge/Backend-FastAPI-009688) ![Python](https://img.shields.io/badge/Language-Python-3776AB)

## Features

- Modern SaaS-style responsive dashboard
- Smart trip builder: dates, budget, travelers, travel style, interests, notes
- Day-wise itinerary with activity times, travel time, duration, and estimated cost
- Dynamic backend generator that works without API keys (ideal for a reliable demo)
- Clear upgrade path for OpenAI/Gemini and Supabase persistence

## Architecture

```
React + Vite UI  →  FastAPI REST API  →  itinerary generator
                                      ↘ Supabase (optional: users/trips)
                                      ↘ Generative AI (optional: richer text)
```

## Run locally

Prerequisites: Node.js 18+ and Python 3.10+.

### 1. Start the API

```bash
cd backend
python -m venv .venv
# Windows PowerShell
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn main:app --reload --port 8000
```

Visit `http://localhost:8000/docs` to see the automatic API documentation.

### 2. Start the frontend (in a second terminal)

```bash
npm install
npm run dev
```

Open the URL printed by Vite (usually `http://localhost:5173`).

## Deploy for free

1. Create a GitHub repository and push this project (commands below).
2. Deploy `backend/` on [Render](https://render.com): create a **Web Service**, set root directory to `backend`, build command `pip install -r requirements.txt`, and start command `uvicorn main:app --host 0.0.0.0 --port $PORT`.
3. Deploy the root folder on [Vercel](https://vercel.com): import the same GitHub repository, use Vite settings, and add environment variable `VITE_API_URL` set to your Render URL (no trailing slash). Redeploy.
4. Your Vercel deployment URL is the demo link for submission.

## GitHub commands

```bash
git init
git add .
git commit -m "Build VoyageAI travel itinerary planner"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/voyage-ai-planner.git
git push -u origin main
```

## Recommended next improvements

- Add Supabase Auth and tables for saving users and itineraries.
- Replace the deterministic `generate_trip` function in `backend/main.py` with a generative AI call after validating returned JSON.
- Add map and weather APIs with server-side secrets only.

## Do not commit

Never commit `.env`, API keys, Supabase service-role keys, or virtual environments. Use deployment environment variables for credentials.
