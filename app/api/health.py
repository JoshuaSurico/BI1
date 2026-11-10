from fastapi import APIRouter, status
from pydantic import BaseModel, Field
from datetime import datetime, timezone

router = APIRouter()

class HealthResponse(BaseModel):
    status: str = Field(..., examples=["UP"], description="État général du service")
    timestamp: datetime = Field(..., description="Horodatage ISO de la vérification")
    version: str = Field(..., examples=["1.0.0"], description="Version de l'API")

@router.get(
    "/health",
    response_model=HealthResponse,
    status_code=status.HTTP_200_OK,
    summary="Health Check",
    description="Retourne l'état de fonctionnement du microservice pour l'orchestrateur ou la gateway."
)
def get_health() -> HealthResponse:
    return HealthResponse(
        status="UP",
        timestamp=datetime.now(timezone.utc),
        version="1.0.0"
    )