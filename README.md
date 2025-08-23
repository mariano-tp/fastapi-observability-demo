# fastapi-observability-demo
API mínima con métricas Prometheus y stack local con Docker Compose (Prometheus + Grafana).

## Correr local
docker compose up --build
# App:       http://localhost:8000/health  (y /metrics)
# Prometheus: http://localhost:9090
# Grafana:    http://localhost:3000  (admin / admin)

## Tests
pip install -r requirements.txt
pytest -q
