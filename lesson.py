# наслідування(спадковість)


class Parent:
    def __init__(self, name, age):
        print("parent hello from __init__")

        self._name = name
        self._age = age

    def display_info(self):
        print("parent hello from display_info ")
        print(f"Parent {self._name}, {self._age} yr")

    def grow(self):
        self._age += 1


class Child(Parent):  # Child успадковує методи класу Parent
    def __init__(self, name, age, grade):
        # в дочірній клас(Child) часто з'являються додаткові атрибути
        # добавляємо через super().__init__
        super().__init__(name, age)

        # ваша додаткова логіка
        print("child hello from __init__")
        self._grade = grade

    # перевантажити(замінити на свій) батьківський метод
    def display_info(self):
        # якщо потрбно виклаеати батьківський варіант методу

        # print("перед super")
        # super().display_info()
        # print("після super")

        print("child hello from display_info ")
        print(f"Child {self._name}, grade №{self._grade}")


# parent = Parent("John", 48)
# parent.display_info()
# parent.grow()


child = Child("Max", 12, 6)
child.display_info()
child.grow()
# child.display_info()


# круті програмісти часто пишуть власні помилки для відслідковування
# проблкм в коді


class WorkerNumParamError(Exception):
    pass


class WorkerTextParamError(Exception):
    pass


class Worker:
    def __init__(self, name: str, salary: int, exp: float):
        # перевірка значень
        self._check_text(name)
        self._check_num(salary)
        self._check_num(exp)

        self._name = name
        self._salary = salary
        self._exp = exp

    # методи для перевірки даних(використовуються лише всередині класу
    # тому їх варто приховати)

    # якщо в методі не потрібно використовувати self
    # тоді цей метод називають статичним
    # щоб вказати що метод є статичним використовують декоратор

    @staticmethod
    def _check_num(num):
        if num < 0:
            raise WorkerNumParamError("worker num param < 0")

    @staticmethod
    def _check_text(text):
        if text == "":
            raise WorkerTextParamError("worker name is empty")

    def increase_salary(self, amount: int):
        self._salary += amount

    def set_exp(self, new_exp: float):
        """
        Встановити новий досвід роботи
        :param new_exp:
        """

        self._check_num(new_exp)
        self._exp = new_exp

    def show_info(self):
        print(f"Name {self._name}, {self._salary}$, exp:{self._exp}")

    # в батьківських класах пишуть методи які будуть пізніше
    # імплементовані в дочірніх класах для кращого розуміння структури
    # цих класів
    def do_work(self):
        """
        Виводить піводомлення що робить працівник
        має бути імплементований в дочірніх класах
        :return:
        """
        pass


class Administrator(Worker):
    def do_work(self):
        print(f"{self._name} перевіряє роботу працівників")


class Developer(Worker):
    def do_work(self):
        print(f"{self._name} пише код програми")


class Intern(Worker):
    def do_work(self):
        print(f"{self._name} вчиться писати код програми")


try:
    developer = Developer("Mary", salary=1000, exp=5)
    developer.increase_salary(200)
    developer.set_exp(4.5)

    developer.show_info()

    developer.do_work()

except WorkerTextParamError:
    print("ім'я не може бути порожнім")
except WorkerNumParamError:
    print("від'ємне число")

#
#
#
# class GrandMa:
#     pass
#
#
# class Parent(GrandMa):
#     pass
#
#
# class Child(Parent):
#     pass
