# ## **Клас: КурсПрограмування**
#
# ### **Створіть клас `КурсПрограмування` з атрибутами:**
#
# *   **назва курсу**
# *   **викладач**
# *   **статус курсу** (*"неактивний"* / *"в процесі"* / *"завершений"*)
# *   **мінімальна кількість студентів**
# *   **максимальна кількість студентів**
# *   **список студентів** (список рядків)
# *   **список модулів** (список словників: `{ "назва": години, "пройдено": False }`)
# *   **поточний модуль** (індекс або None)
# *   **загальний прогрес курсу (в %)**
# *   **дата старту (за замовчуванням None)**
# *   **дата завершення (за замовчуванням None)**
#
# ***

# стилі назв в python:
# snake_case -- (малі літери, між словами _)
# *  змінні
# *  функції
# *  модулі/бібліотеки/файли
#
# CamelCase  -- (перша літера слова велика, немає нічого між словами)
# * класи
from datetime import datetime
from typing import Any


class ProgrammingCourse:
    # *   **назва курсу**
    # *   **викладач**
    # *   **статус курсу** (*"неактивний"* / *"в процесі"* / *"завершений"*)
    # *   **мінімальна кількість студентів**
    # *   **максимальна кількість студентів**
    # *   **список студентів** (список рядків)
    # *   **список модулів** (список словників:`{ назва години, пройдено}`)
    # *   **поточний модуль** (індекс або None)
    # *   **загальний прогрес курсу (в %)**
    # *   **дата старту (за замовчуванням None)**
    # *   **дата завершення (за замовчуванням None)**
    def __init__(
        self,
        name: str,
        teacher: str,
        min_students: int = 5,
        max_students: int = 20,
    ):
        self.name = name
        self.teacher = teacher
        self.min_students = min_students
        self.max_students = max_students

        self.status = "неактивний"  # (*"неактивний"* / *"в процесі"* / *"завершений"*)
        self.students: list[str] = []
        self.modules: list[
            dict[str, Any]
        ] = []  # список словників де ключ str, значення будь-яке
        self.current_model_idx: int | None = None
        self.progress: float = 0
        self.start_date: datetime | None = None
        self.end_date: datetime | None = None

        self.total_hour: int = 0

    def start(self):
        # перевірки
        if len(self.students) < self.min_students:
            print("Замало студентів")
            return

        if len(self.students) > self.max_students:
            print("Забагато студентів")
            return

        if not self.modules:  # якщо порожній
            print("Немає модулів")
            return

        if self.status != "неактивний":
            print("Курс уже почався")
            return

        # починаємо курс
        self.status = "в процесі"
        self.current_model_idx = 0
        self.start_date = datetime.now()

    def show_info(self):
        print(f"Назва курсу: {self.name}")
        print(f"Викладач: {self.teacher}")
        print(f"Статус: {self.status}")

        print(f"\nКількість студентів: {len(self.students)}")
        print(f"Мінімум / Максимум: {self.min_students} / {self.max_students}")

        print("\nСтуденти:")
        if self.students:
            for student in self.students:
                print(f" - {student}")
        else:
            print(" (немає студентів)")

        print(f"Загальна тривалість: {self.total_hour} год")
        print(f"\nКількість модулів: {len(self.modules)}")

        print(f"\nПрогрес: {self.progress * 100:.1f}%")

        print("\nПоточний модуль: ", end="")
        if self.current_model_idx is not None and 0 <= self.current_model_idx < len(
            self.modules
        ):
            module = self.modules[self.current_model_idx]
            print(module["name"])
        else:
            print("не встановлено")

        print("\nДати:")
        print(f" Початок: {self.start_date if self.start_date else 'не встановлено'}")
        print(f" Завершення: {self.end_date if self.end_date else 'не встановлено'}")

    def add_student(self, student_name: str):
        self.students.append(student_name)

    def add_module(self, name: str, duration: int):
        module = {"name": name, "duration": duration, "is_finished": False}
        self.modules.append(module)
        self.total_hour += duration

    def finish(self):
        # перевірки

        if self.progress < 1.0:
            print("Ви ще не пройшли всі модулі")
            return

        # закінчуємо курс
        self.status = "завершений"
        self.end_date = datetime.now()

    def switch_module(self):
        # change progress

        # модуль який закінчили
        module = self.modules[self.current_model_idx]
        self.progress += module["duration"] / self.total_hour

        self.current_model_idx += 1


course = ProgrammingCourse(
    name="PythonAI55",
    teacher="Anton Halysh",
    min_students=3,
)


course.add_student("John")
course.add_student("Ann")
course.add_student("Mary")
course.add_student("Mike")

course.add_module("Python", 150)
course.add_module("AI", 75)

course.start()
course.show_info()

course.switch_module()
course.switch_module()

course.finish()

course.show_info()

#
#
# ***
#
# ## ### **1. запуск курсу**
#
#
# ***
#
# ## ### **2. завершення курсу**
# ***
#
# ## ### **3. додати модуль**
#
# Передається:
#
# *   назва
# *   години
#
# ***
#
# ## ### **4. видалити модуль**
#
# ***
#
# ## ### **5. додати студента**
#
# ***
#
# ## ### **6. видалити студента**
#
# ***
#
# ## ### **7. перейти до наступного модуля**
#
# ***
#
# ## ### **8. отримати прогрес курсу**
#
# ***
#
# ## ### **9. змінити викладача**
#
# ***
#
# ## ### **10. вивести детальну інформацію про курс**
#
# ***
#
# ## ### **13. підрахувати загальні години модулів**
#
#
# ***
#
# ## ### **14. знайти модуль за назвою**
#
