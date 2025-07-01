from src.main import add_task, tasks

def test_add_task():
    add_task("Entrega teste", "Normal", "Maria")
    assert len(tasks) == 1
    assert tasks[0]["description"] == "Entrega teste"
