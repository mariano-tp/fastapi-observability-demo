import re
from fastapi.testclient import TestClient

from app.main import app


def test_metrics_endpoint_exposes_prometheus_format_and_http_metrics():
    client = TestClient(app)

    # Generar tráfico para que haya métricas de requests
    r = client.get("/health")
    assert r.status_code == 200

    r = client.get("/predict", params={"x": 1.0, "y": 2.0})
    assert r.status_code == 200

    # Pedir métricas
    r = client.get("/metrics")
    assert r.status_code == 200

    body = r.text

    # 1) Formato Prometheus (al menos HELP/TYPE)
    assert "# HELP" in body or "# TYPE" in body

    # 2) Métricas HTTP típicas del instrumentator (nombres pueden variar por versión/config)
    # Buscamos alguna señal robusta de métricas de request/latencia.
    patterns = [
        r"\bhttp_.*requests.*\b",          # http_requests_total, http_server_requests_seconds_count, etc.
        r"\bhttp_.*duration.*\b",          # http_request_duration_seconds, etc.
        r"\bhttp_.*latenc.*\b",            # latency
        r"\brequest.*duration.*\b",
    ]

    assert any(re.search(p, body) for p in patterns), (
        "No se encontraron métricas HTTP en /metrics. "
        "Puede faltar instrumentación o cambiar nombres por versión."
    )
