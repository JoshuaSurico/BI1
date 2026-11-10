from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health_check_returns_200():
    response = client.get("/health")
    assert response.status_code == 200
    
    data = response.json()
    assert data["status"] == "UP"
    assert data["version"] == "1.0.0"
    assert "timestamp" in data
