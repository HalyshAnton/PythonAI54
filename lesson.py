# Принципи ООП

# інкапсуляція
# поліморфізм
# наслідування


# # інкапсуляція
# nums = [1, 2, 3, 4]
#
# nums.append(2)
# nums.remove(5)
# nums[0]  # тут теж метод index(0)


def show():
    greet_user()
    print("hello world")


def greet_user():
    print("hello user")


class Person:
    def __init__(self, name, age):
        self._check_str(name)
        self._check_num(age)

        self._name = name  # приховування атрибутів
        self._age = age

    def _check_str(self, text):  # прихований метод
        if text == "":
            raise ValueError("Рядок не може бути порожнім")

    def _check_num(self, num):
        if num <= 0:
            raise ValueError("Число не може бути ві'ємним")

    def show_info(self):
        print(self._name)
        print(self._age)

    def get_grade(self, grade):
        self._check_num(grade)
        print(f"Ви отримали оцінку {grade}")


# person = Person("John", 25)
# person.show_info()
#
# # до прихованих методів/атрибутів можна отримати доступ
# # але бажано так не робити
# person._check_str("")


# поліморфізм

#
# words = [1, 2, 3, 4]
# fruits = {"apple", "banana", "cherry"}
# rate_currency = {"UAH": 1, "USD": 44, "ZLT": 11}
#
# words.append()
# fruits.union()
# rate_currency.items()
#
#
# words.clear()
# fruits.clear()
# rate_currency.clear()

# поліморфізм
#
# в різних класах є методи з однаковою назвою які
# реалізовують однакову логіку


class Cat:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def make_sound(self):
        print("Мяу")

    def grow(self):
        self._age += 1


class Dog:
    def __init__(self, name, age, energy):
        self._name = name
        self._age = age
        self._energy = energy

    def make_sound(self):
        print("Гав")

    def grow(self):
        self._age += 1
        self._energy -= 1

    def play(self):
        if self._energy < 10:
            print("Песик втомлений")


class Hamster:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def make_sound(self):
        print("Пі-пі-пі")

    def grow(self):
        self._age += 1


pet = Hamster(name="Jordon", age=3)

pet.make_sound()
pet.grow()
