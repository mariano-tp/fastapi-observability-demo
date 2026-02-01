> Available languages / Idiomas disponibles: [*English*](README.md) / [*Español*](README.ES.md)

Volver al repositorio: [Home](https://github.com/metorresponce/metorresponce/blob/main/README.ES.md)

[![tests](https://img.shields.io/github/actions/workflow/status/metorresponce/fastapi-observability-demo/ci.yml?branch=main&label=tests&style=flat-square)](https://github.com/metorresponce/fastapi-observability-demo/actions/workflows/ci.yml)
[![docker-build](https://img.shields.io/github/actions/workflow/status/metorresponce/fastapi-observability-demo/docker-ci.yml?branch=main&label=docker-build&style=flat-square)](https://github.com/metorresponce/fastapi-observability-demo/actions/workflows/docker-ci.yml)
[![CodeQL](https://img.shields.io/github/actions/workflow/status/metorresponce/fastapi-observability-demo/codeql.yml?branch=main&label=codeql&style=flat-square)](https://github.com/metorresponce/fastapi-observability-demo/actions/workflows/codeql.yml)
[![last commit](https://img.shields.io/github/last-commit/metorresponce/fastapi-observability-demo?style=flat-square)](https://github.com/metorresponce/fastapi-observability-demo/commits/main)
[![release](https://img.shields.io/github/v/release/metorresponce/fastapi-observability-demo?display_name=tag&style=flat-square)](https://github.com/metorresponce/fastapi-observability-demo/releases)
[![license: MIT](https://img.shields.io/badge/license-MIT-green?style=flat-square)](./LICENSE)
[![stars](https://img.shields.io/github/stars/metorresponce/fastapi-observability-demo?style=flat-square)](https://github.com/metorresponce/fastapi-observability-demo/stargazers)

# FastAPI Observability Demo

API mínima en FastAPI que expone `/metrics` mediante `prometheus-fastapi-instrumentator`.

Este repositorio está pensado para validarse completamente dentro de GitHub:
tests, análisis de seguridad y build de la imagen Docker se ejecutan en GitHub Actions.

No hace falta instalar nada en local para evaluarlo.

## Endpoints
- GET `/health` -> `{"status":"ok"}`
- GET `/predict?x=<float>&y=<float>` -> suma simple
- GET `/metrics` -> métricas para Prometheus

## Cómo validarlo (GitHub Actions)
Entrá en la pestaña Actions y ejecutá los workflows (o empujá un commit).

- tests (ci.yml)  
  Ejecuta pytest en CI.  
  Evidencia: logs del workflow y, si están habilitados, artifacts descargables como reportes de tests/coverage.

- docker-build (docker-ci.yml)  
  Construye la imagen Docker sin publicarla (sin push).

- codeql (codeql.yml)  
  Ejecuta análisis estático orientado a seguridad.

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
    ├── docker-ci.yml
    └── codeql.yml
```

## Créditos
Repositorio de portfolio por @metorresponce. Licencia MIT.

Ver también: [Code of Conduct](./CODE_OF_CONDUCT.md) · [Contributing](./CONTRIBUTING.md) · [Security](./SECURITY.md)
