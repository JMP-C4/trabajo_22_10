from dataclasses import dataclass
from enum import Enum, auto
from typing import Optional


class Priority(Enum):
    LOW = auto()
    MEDIUM = auto()
    HIGH = auto()


class Status(Enum):
    TODO = auto()
    IN_PROGRESS = auto()
    DONE = auto()


@dataclass(frozen=True)
class Task:
    """
    Clase que representa una tarea individual.
    Inmutable para garantizar seguridad en actualizaciones.
    """
    id: Optional[int]
    title: str
    priority: Priority = Priority.MEDIUM
    status: Status = Status.TODO
    description: Optional[str] = None

    def __post_init__(self):
        if not isinstance(self.title, str) or not self.title.strip():
            raise ValueError("El título no puede estar vacío")
        if not isinstance(self.priority, Priority):
            raise TypeError("priority debe ser de tipo Priority")
        if not isinstance(self.status, Status):
            raise TypeError("status debe ser de tipo Status")

    def with_updates(self, **kwargs) -> "Task":
        """Devuelve una nueva Task con campos actualizados."""
        allowed = {"id", "title", "priority", "status", "description"}
        for k in kwargs.keys():
            if k not in allowed:
                raise KeyError(f"Campo no permitido: {k}")

        data = {
            "id": kwargs.get("id", self.id),
            "title": kwargs.get("title", self.title),
            "priority": kwargs.get("priority", self.priority),
            "status": kwargs.get("status", self.status),
            "description": kwargs.get("description", self.description),
        }
        return Task(**data)

    def to_dict(self) -> dict:
        """Convierte la tarea a un diccionario (útil para guardar o mostrar)."""
        return {
            "id": self.id,
            "title": self.title,
            "priority": self.priority.name,
            "status": self.status.name,
            "description": self.description,
        }
