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

