#зроби клас завдань)))
# типу схоже на те що у джирі
# назва, опис, крайній термін, тощо
# подумай що там має бути
# якби ти давав комусь завдання або якби тобі давали завдання,
# що має мати завдання для того щоб бути повноцінним
# і ще клас який буде керувати завданнями - створювати,
# редагувати існуюче, зберігати всі завдання, видаляти якесь, завершувати якесь
# нічого через термінал робити не треба (крім запуску програми)
# все управління в коді
# типу такого
# task_manager.create_task()
# task_manager.delete_task(id=12)

class Task():
    def __init__(self, name, description, deadline):
        self.name = name
        self.description = description
        self.deadline = deadline
        self.completed = False

    def mark_as_done(self):
        self.completed = True

    def __str__(self):
        status = "Завершено" if self.completed else "Не завершено"
        return f"{self.name} — {self.description} (до {self.deadline}) | {status}"

class TaskManager():
    def __init__(self):
        self.tasks = []

    def create_task(self, name, description, deadline):
        task = Task(name, description, deadline)
        self.tasks.append(task)
        print(f"Завдання {name} створено")

    def list_tasks(self):
        if not self.tasks:
            print("Жодного завдання не має")
            return
        for i, task in enumerate(self.tasks, 1):
            print(f"{i}. {task}")