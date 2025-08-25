[![tests](https://img.shields.io/github/actions/workflow/status/mariano-tp/fastapi-observability-demo/ci.yml?branch=main&label=tests&style=flat-square)](https://github.com/mariano-tp/fastapi-observability-demo/actions/workflows/ci.yml)
[![docker-build](https://img.shields.io/github/actions/workflow/status/mariano-tp/fastapi-observability-demo/docker-ci.yml?branch=main&label=docker-build&style=flat-square)](https://github.com/mariano-tp/fastapi-observability-demo/actions/workflows/docker-ci.yml)
[![CodeQL](https://img.shields.io/github/actions/workflow/status/mariano-tp/fastapi-observability-demo/codeql.yml?branch=main&label=codeql&style=flat-square)](https://github.com/mariano-tp/fastapi-observability-demo/actions/workflows/codeql.yml)
[![release](https://img.shields.io/github/v/release/mariano-tp/fastapi-observability-demo?display_name=tag&style=flat-square)](https://github.com/mariano-tp/fastapi-observability-demo/releases)
[![license: MIT](https://img.shields.io/badge/license-MIT-green?style=flat-square)](./LICENSE)
[![last commit](https://img.shields.io/github/last-commit/mariano-tp/fastapi-observability-demo?style=flat-square)](https://github.com/mariano-tp/fastapi-observability-demo/commits/main)
[![stars](https://img.shields.io/github/stars/mariano-tp/fastapi-observability-demo?style=flat-square)](https://github.com/mariano-tp/fastapi-observability-demo/stargazers)

# fastapi-observability-demo

API mínima con **FastAPI** que expone métricas **/metrics** vía `prometheus-fastapi-instrumentator`.  
Pensado para portfolio: **tests con pytest** y **CI en GitHub Actions** (tests + build de imagen, sin push).

> 100% web: no hace falta instalar nada. Subí este repo y ejecutá los workflows en **Actions**.

## Endpoints
- `GET /health` → `{"status":"ok"}`
- `GET /predict?x=<float>&y=<float>` → suma simple
- `GET /metrics` → métricas Prometheus

## Cómo probar (CI)
- **Actions → Run workflow** en: `ci.yml` (tests) y `docker-ci.yml` (build sin push).

## Estructura
```text
.
├── app/
│   └── main.py
├── tests/
│   └── test_app.py
├── Dockerfile
├── requirements.txt
├── pytest.ini
└── .github/workflows/
    ├── ci.yml
    └── docker-ci.yml
```

## Créditos
Repositorio de portfolio por @mariano-tp. Licencia MIT.

Ver también: [Código de Conducta](./CODE_OF_CONDUCT.md) · [Contribuir](./CONTRIBUTING.md) · [Seguridad](./SECURITY.md)
