# 90-second demo script

1. Open the home page. Explain that VoyageAI turns a few personal preferences into a practical itinerary.
2. Point out destination, dates, budget, group size, pace, and interest chips.
3. Select a different interest, for example **Adventure**, and click **Generate my itinerary**.
4. Explain the result: every day has a theme, timed activities, travel estimates, and individual estimated costs.
5. Mention that the API is structured as JSON, so itineraries can be saved to Supabase and edited or regenerated per day in the next iteration.

## Judge-friendly talking points

- **Problem:** Planning across multiple websites causes decision fatigue and makes group coordination difficult.
- **Solution:** One guided form produces a tailored, budget-aware, day-wise plan.
- **Technology:** React/Vite, FastAPI, REST API, and Supabase-ready database schema.
- **Reliability:** The submitted demo uses a deterministic generator; it works without exposing an AI key. The backend’s generator is intentionally isolated so an LLM can replace it without changing the UI.
