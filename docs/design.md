# Diseño del Sistema de Gestión de Tareas

## Estructura

- `Task`: representa una tarea individual, inmutable y validada.
- `TaskManager`: maneja una colección de tareas en memoria.

## Principios aplicados

- **SRP:** cada clase tiene una única responsabilidad.
- **OCP:** el sistema es extensible sin modificar código existente.
- **Clean Code:** nombres claros, funciones pequeñas, responsabilidades separadas.

## Testing

Se utilizan `pytest` y `coverage` para asegurar cobertura mayor al 80%.
