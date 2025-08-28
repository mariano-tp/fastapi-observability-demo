# Guía de Contribución

Gracias por tu interés 🙌. Este repo está pensado para ser simple y reproducible.

## Flujo de trabajo
1. **Abrí un issue** si el cambio afecta API o métricas.
2. **Creá una rama** desde `main` (`feat/...`, `fix/...`, `docs/...`, `ci/...`).
3. **Commits** estilo *Conventional Commits*.
4. **Pull Request**:
   - Un tema por PR
   - Link al issue
   - Pasar todos los checks de CI
   - Documentar cambios en `/metrics` si aplica

## Estilo / calidad
- Código con tipado claro.
- Tests para nuevas métricas.
- Actualizar README si se agregan endpoints o métricas.

## CI
Los PRs deben quedar en **verde**:
- `pytest -q`
- `docker build .`

## Licencia
Al contribuir aceptás que tu aporte se publica bajo **MIT** (ver `LICENSE`).
