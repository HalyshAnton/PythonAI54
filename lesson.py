#  ## Завдання 1
#
# Створіть абстрактний клас **Employee** з атрибутами:
#
# * `name` – ім’я працівника
# * `salary` – зарплата
# * `status` – стан (`working`, `vacation`, `offline`)
#
# Методи:
#
# * `info()` – виводить інформацію
# * `start_work()` – змінює стан на `working`
# * `take_vacation()` – змінює стан на `vacation`
# * `increase_salary(amount)` – збільшує зарплату
#

from abc import ABC
from enum import Enum


# `status` – стан (`working`, `vacation`, `offline`)
class Status(Enum):
    working = "working"
    vacation = "vacation"
    offline = "offline"


class Employee(ABC):
    def __init__(
        self,
        name: str,
        salary: int,
        status: Status = Status.offline,
    ):
        self._name = name
        self._salary = salary
        self._status = status

    # * `info()` – виводить інформацію
    def info(self):
        print(f"Name: {self._name}, salary: {self._salary}")
        print(f"Status: {self._status.value}")

    # * `start_work()` – змінює стан на `working`
    def start_work(self):
        self._status = Status.working

    # * `take_vacation()` – змінює стан на `vacation`
    def take_vacation(self):
        self._status = Status.vacation

    # * `increase_salary(amount)` – збільшує зарплату
    def increase_salary(self, amount: int):
        self._salary += amount

    # @abstractmethod
    # def method(self):
    #     pass


#
# ## Завдання 2
#
# Створіть дочірній клас **Programmer**
#
# Додаткові атрибути:
#
# * `language` – основна мова програмування
# * `projects` – список проєктів
# * `bugs_fixed` – кількість виправлених помилок


class Programer(Employee):
    def __init__(
        self,
        name: str,
        salary: int,
        language: str,
        status: Status = Status.offline,
        projects: list[str] | None = None,
        bugs_fixed: int = 0,
    ):
        # викликаємо init з Employee
        super().__init__(name, salary, status)

        # додаткові атрибути
        self._language = language
        self._bugs_fixed = bugs_fixed

        # перевірка projects
        if projects is None:
            self._projects = []
        else:
            self._projects = projects

    # * `info()` – додатково виводить інформацію
    def info(self):
        super().info()
        print(f"Language: {self._language}, #fixed bugs: {self._bugs_fixed}")
        print(f"Projects: {self._projects}")

    # * `add_project(project)` – додає проєкт
    def add_project(self, project: str):
        self._projects.append(project)

    # * `fix_bug(count)` – збільшує кількість виправлених помилок
    def fix_bug(self, count: int):
        self._bugs_fixed += count

    # * `change_language(new_language)` – змінює мову програмування
    def change_language(self, new_language: str):
        self._language = new_language


pr1 = Programer(
    name="Jhon",
    salary=1000,
    language="Python",
)

pr2 = Programer(
    name="Mary",
    salary=1000,
    language="Python",
)

pr3 = Programer(
    name="Mike",
    salary=1000,
    language="Python",
)
pr1.change_language("Java")
pr2.fix_bug(3)
pr3.add_project("Text detection")
pr3.start_work()

# pr1.info()
# pr2.info()
# pr3.info()
#
# Методи:
#
# * `info()` – додатково виводить інформацію
# * `add_project(project)` – додає проєкт
# * `fix_bug(count)` – збільшує кількість виправлених помилок
# * `change_language(new_language)` – змінює мову програмування
#
# ---
#
# ## Завдання 3
#
# Створіть дочірній клас **Designer**
#
# Додаткові атрибути:
#
# * `tool` – програма для дизайну
# * `works_done` – кількість виконаних робіт
# * `style` – стиль дизайну


class Designer(Employee):
    def __init__(
        self,
        name: str,
        salary: int,
        tool: str,
        style: str,
        status: Status = Status.offline,
        works_done: int = 0,
        favourite_color: str = "red",
        password: str = ""
    ):
        super().__init__(name, salary, status)

        self._tool = tool
        self._style = style
        self._works_done = works_done


#
# Методи:
#
# * `info()` – додатково виводить інформацію
# * `create_design()` – збільшує кількість робіт
# * `change_style(new_style)` – змінює стиль
# * `change_tool(new_tool)` – змінює програму для роботи


# class Employee(ABC):
#     pass
#
#
# class Designer(Employee):
#     pass
#
#
# class Programer(Employee):
#     pass
#
#
# designer1 = Designer()
# progra = Programer()
