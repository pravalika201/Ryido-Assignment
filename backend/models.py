from pydantic import BaseModel, Field

class FareRequest(BaseModel):
    distance_km: float = Field(..., ge=0)
    duration_min: int = Field(..., ge=0)

class FareResponse(BaseModel):
    estimated_fare: int
