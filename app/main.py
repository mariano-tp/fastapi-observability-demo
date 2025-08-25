from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI(title="fastapi-observability-demo")

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/predict")
def predict(x: float = 0.0, y: float = 0.0):
    return {"prediction": x + y}

# Exponer /metrics
Instrumentator().instrument(app).expose(app)
