> Available languages / Idiomas disponibles: [*English*](README.md) / [*Español*](README.ES.md)  

[![tests](https://img.shields.io/github/actions/workflow/status/mariano-tp/fastapi-observability-demo/ci.yml?branch=main&label=tests&style=flat-square)](https://github.com/mariano-tp/fastapi-observability-demo/actions/workflows/ci.yml)
[![docker-build](https://img.shields.io/github/actions/workflow/status/mariano-tp/fastapi-observability-demo/docker-ci.yml?branch=main&label=docker-build&style=flat-square)](https://github.com/mariano-tp/fastapi-observability-demo/actions/workflows/docker-ci.yml)
[![CodeQL](https://img.shields.io/github/actions/workflow/status/mariano-tp/fastapi-observability-demo/codeql.yml?branch=main&label=codeql&style=flat-square)](https://github.com/mariano-tp/fastapi-observability-demo/actions/workflows/codeql.yml)
[![last commit](https://img.shields.io/github/last-commit/mariano-tp/fastapi-observability-demo?style=flat-square)](https://github.com/mariano-tp/fastapi-observability-demo/commits/main)
[![release](https://img.shields.io/github/v/release/mariano-tp/fastapi-observability-demo?display_name=tag&style=flat-square)](https://github.com/mariano-tp/fastapi-observability-demo/releases)
[![license: MIT](https://img.shields.io/badge/license-MIT-green?style=flat-square)](./LICENSE)
[![stars](https://img.shields.io/github/stars/mariano-tp/fastapi-observability-demo?style=flat-square)](https://github.com/mariano-tp/fastapi-observability-demo/stargazers)

# FastAPI Observability Demo

Minimal API with FastAPI exposing /metrics via `prometheus-fastapi-instrumentator`.

This repo is designed to be validated entirely in GitHub:
tests, security checks and Docker image build run in GitHub Actions.

No local setup is required to evaluate it.

## Endpoints
- GET /health -> {"status":"ok"}
- GET /predict?x=<float>&y=<float> -> simple sum
- GET /metrics -> Prometheus metrics

## How to validate (GitHub Actions)
Open the Actions tab and run the workflows (or push a commit).

- tests (ci.yml)  
  Runs pytest in CI.  
  Evidence: the workflow run logs, and (if enabled) downloadable artifacts like test reports/coverage.

- docker-build (docker-ci.yml)  
  Builds the Docker image without pushing it.

- codeql (codeql.yml)  
  Runs static analysis security scanning.

## Structure
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

## Credits
Portfolio repository by @mariano-tp. Licensed under MIT.

See also: [Code of Conduct](./CODE_OF_CONDUCT.md) · [Contributing](./CONTRIBUTING.md) · [Security](./SECURITY.md)
