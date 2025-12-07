from fastapi import FastAPI, HTTPException
from models import FareRequest, FareResponse

app = FastAPI()

BASE_FARE = 20
PER_KM = 7
PER_MIN = 1

@app.post("/estimate_fare", response_model=FareResponse)
def estimate_fare(data: FareRequest):
    fare = BASE_FARE + (PER_KM * data.distance_km) + (PER_MIN * data.duration_min)
    return FareResponse(estimated_fare=int(round(fare)))
