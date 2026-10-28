from datetime import date, timedelta
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

app = FastAPI(title="VoyageAI Planner API")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

class TripRequest(BaseModel):
    destination: str
    start_date: date
    end_date: date
    budget: int = Field(gt=0)
    travelers: int = Field(gt=0)
    travel_style: str = "Balanced"
    interests: list[str] = []
    notes: str = ""

def activity(time, title, description, duration, travel, cost):
    return {"time":time,"title":title,"description":description,"duration":duration,"travel":travel,"cost":cost}

@app.get("/health")
def health(): return {"status":"ok"}

@app.post("/api/itineraries/generate")
def generate_trip(req: TripRequest):
    duration = max(1, (req.end_date - req.start_date).days + 1)
    interests = ", ".join(req.interests[:3]) or "local highlights"
    themes = ["A warm welcome", "Flavours & hidden stories", "A beautiful farewell", "Explore at your own pace"]
    days=[]
    for n in range(duration):
        day_date = req.start_date + timedelta(days=n)
        daytime = "unhurried" if req.travel_style.lower() == "relaxed" else "well-paced"
        activities = [
          activity("9:00 AM", f"Discover {req.destination}", f"Begin with an easy orientation walk and a curated local landmark, tailored around {interests}.", "2 hours", "Walk / short ride", "₹400"),
          activity("1:00 PM", "Taste the local table", "A hand-picked lunch stop known for regional flavours and a welcoming atmosphere.", "1.5 hours", "10 min ride", "₹900"),
          activity("4:00 PM", "Golden-hour experience", f"Enjoy a {daytime} afternoon at a scenic local favourite. Leave time for spontaneous discoveries.", "2 hours", "15 min ride", "₹600")]
        days.append({"day":n+1,"date":day_date.strftime("%d %b"),"theme":themes[n%len(themes)],"activities":activities})
    estimated = min(req.budget, max(3000*req.travelers*duration, int(req.budget*.78)))
    return {"title":f"{req.destination} in {duration} day{'s' if duration>1 else ''}","date_range":f"{req.start_date.strftime('%d %b')} – {req.end_date.strftime('%d %b %Y')}","estimated_total":estimated,"summary":f"A {req.travel_style.lower()} journey created for {req.travelers} traveler(s), with a focus on {interests}. This plan balances memorable experiences with breathing room and stays conscious of your budget.","itinerary":{"days":days},"travel_tip":"Keep your first and final activity flexible. The best travel memories often come from the detours you didn’t plan."}
