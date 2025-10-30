import pytest
from src.task import Task, Priority, Status
from src.task_manager import TaskManager, TaskNotFoundError


@pytest.fixture
def manager():
    return TaskManager()


def test_add_and_get_by_id(manager):
    task = manager.add_task(Task(id=None, title="Comprar pan"))
    found = manager.get_by_id(task.id)
    assert found.title == "Comprar pan"


def test_update_task(manager):
    task = manager.add_task(Task(id=None, title="Estudiar"))
    updated = manager.update_task(task.id, status=Status.IN_PROGRESS)
    assert updated.status == Status.IN_PROGRESS


def test_remove_task(manager):
    task = manager.add_task(Task(id=None, title="Eliminarme"))
    manager.remove_task(task.id)
    with pytest.raises(TaskNotFoundError):
        manager.get_by_id(task.id)


def test_get_by_status_and_find(manager):
    a = manager.add_task(Task(id=None, title="Escribir informe", priority=Priority.HIGH))
    b = manager.add_task(Task(id=None, title="Leer documentación", priority=Priority.LOW))
    manager.update_task(a.id, status=Status.DONE)
    done = manager.get_by_status(Status.DONE)
    assert len(done) == 1
    found = manager.find(title_contains="docu")
    assert len(found) == 1
