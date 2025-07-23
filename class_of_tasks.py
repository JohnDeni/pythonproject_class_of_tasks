from datetime import datetime
class Task():
    def __init__(self, name, description, deadline):
        self.name = name
        self.description = description
        self.deadline = datetime.strptime(deadline, "%Y-%m-%d").date()
        self.is_completed = False

    def mark_as_done(self):
        self.is_completed = True

    def __str__(self):
        status = "Завершено" if self.is_completed else "Не завершено"
        return (
            f"Назва: {self.name}\n"
            f"Опис: {self.description}\n"
            f"Дедлайн: {self.deadline}\n"
            f"Статус: {status}"
        )

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

    def mark_task_done(self, index):
        try:
            task = self.tasks[index]
            task.mark_as_done()
            print(f"Завдання {task.name} виконано")
        except IndexError:
            print("Неправильний індекс завдання")

    def delete_task(self, index):
        try:
            task = self.tasks.pop(index)
            print(f"Завдання {task.name} видалено")
        except IndexError:
            print("Невірний індекс")

task_manager = TaskManager()

task_manager.create_task("Прибрати кімнату", "Позамітати та протерти пилюку", "2025-07-30")
task_manager.create_task("Купити продукти", "Молоко, хліб, яйця", "2025-07-25")
task_manager.create_task("Вивчити Python", "Закінчити тему", "2025-08-05")

print("\nСписок завдань після створення:")
task_manager.list_tasks()

task_manager.mark_task_done(1)

print("\nСписок завдань після виконання другого:")
task_manager.list_tasks()

task_manager.delete_task(0)

print("\nСписок завдань після видалення першого:")
task_manager.list_tasks()
