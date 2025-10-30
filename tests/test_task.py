import pytest
from src.task import Task, Priority, Status


def test_task_creation():
    task = Task(id=None, title="Estudiar Python")
    assert task.title == "Estudiar Python"
    assert task.priority == Priority.MEDIUM
    assert task.status == Status.TODO


def test_invalid_title():
    with pytest.raises(ValueError):
        Task(id=None, title="   ")


def test_with_updates_creates_new_instance():
    task = Task(id=1, title="Leer libro")
    new_task = task.with_updates(title="Leer otro libro", status=Status.DONE)
    assert new_task is not task
    assert new_task.title == "Leer otro libro"
    assert new_task.status == Status.DONE


def test_with_updates_invalid_field():
    task = Task(id=1, title="Tarea base")
    with pytest.raises(KeyError):
        task.with_updates(nuevo="no existe")
