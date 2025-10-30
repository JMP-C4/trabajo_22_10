from typing import List, Dict, Optional
from .task import Task, Priority, Status


class TaskNotFoundError(Exception):
    pass


class TaskManager:
    def __init__(self, initial: Optional[List[Task]] = None):
        self._tasks: Dict[int, Task] = {}
        self._next_id = 1
        if initial:
            for task in initial:
                self.add_task(task)

    def _generate_id(self) -> int:
        current = self._next_id
        self._next_id += 1
        return current

    def add_task(self, task: Task) -> Task:
        if task.id is None:
            task = task.with_updates(id=self._generate_id())
        elif task.id in self._tasks:
            raise ValueError(f"Ya existe una tarea con id {task.id}")
        self._tasks[task.id] = task
        return task

    def get_by_id(self, task_id: int) -> Task:
        if task_id not in self._tasks:
            raise TaskNotFoundError(f"Tarea con id {task_id} no encontrada")
        return self._tasks[task_id]

    def update_task(self, task_id: int, **updates) -> Task:
        old_task = self.get_by_id(task_id)
        new_task = old_task.with_updates(**updates)
        self._tasks[task_id] = new_task
        return new_task

    def remove_task(self, task_id: int) -> None:
        if task_id not in self._tasks:
            raise TaskNotFoundError(f"Tarea con id {task_id} no encontrada")
        del self._tasks[task_id]

    def get_all(self) -> List[Task]:
        return list(self._tasks.values())

    def get_by_status(self, status: Status) -> List[Task]:
        return [t for t in self._tasks.values() if t.status == status]

    def find(self, *, title_contains: Optional[str] = None, priority: Optional[Priority] = None) -> List[Task]:
        results = list(self._tasks.values())
        if title_contains:
            results = [t for t in results if title_contains.lower() in t.title.lower()]
        if priority:
            results = [t for t in results if t.priority == priority]
        return results
