from fastapi import FastAPI
from app.core.config import settings
from app.api.health import router as health_router

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    description="Microservice template pour architecture ETL avec documentation Swagger auto-générée.",
    openapi_url="/openapi.json",
    docs_url="/docs",      # Swagger UI
    redoc_url="/redoc"     # ReDoc alternative
)

# Enregistrement des routes
app.include_router(health_router, tags=["Health"])

if __name__ == "__main__":
    import uvicorn
    # Permet de lancer et déboguer directement le script Python
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
