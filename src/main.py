tasks = []

def add_task(description, priority, assignee):
    tasks.append({
        "id": len(tasks) + 1,
        "description": description,
        "priority": priority,
        "assignee": assignee,
        "status": "A Fazer"
    })

# Teste manual
add_task("Entrega para cliente X", "Urgente", "João")
print(tasks)
