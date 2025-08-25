from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health_ok():
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json()["status"] == "ok"

def test_predict_sum():
    r = client.get("/predict", params={"x": 2.5, "y": 7.5})
    assert r.status_code == 200
    assert r.json()["prediction"] == 10.0
