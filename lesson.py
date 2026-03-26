# ООП
# Об'єкно орієнтоване програмування


# в програмі потрібно працювати з об'єктами, які:
# вони мають якусь інформацію(може змінюватись)
# можуть робити певні дії
#
#
# Приклад
# Акаунт користувача:
# інформація(атрибути)
#   ПІБ
#   логін пароль
#   посилання на зображення аватарки
#
# Дії:
#  зайти на сайт
#  пройти верифікацію
#  оформити замовлення
#  оформити підписку


# nums = [1, 2, 3, 4]
# nums.append()


# клас Dog
# загальний опис що вміють будь-який песик


class Dog:
    # опис атрибутів(інформація)
    # опис методів(дія які може робити песик)

    # для ініціалізація(створення об'єкта)
    # можна передати атрибути
    # dog = Dog(name, age, breed)
    # пишеться спеціальніий метод __init__
    def __init__(self, name, age, breed):
        # прикріпити атрибути до self
        self.name = name.capitalize()
        self.age = age
        self.breed = breed.lower()

    # метод make_voice
    # всі методи створюються як фунції
    # в методах перший параметр завжди self -- об'кт який викликав метод
    def make_voice(self):
        print(f"{self.name} каже Гав")

    def show_info(self):
        print(f"DOG {self.name} {self.age}yr {self.breed}")

    # отримати ім'я песика
    def get_name(self):
        return self.name

    def birthday(self):
        print(f"У {self.name} день народження")

        # збільшуємо вік
        self.age += 1

    def eat(self, food):
        print(f"{self.name} їсть {food}")


# створення об'єкти класу Dog(конкретні песики)

dog1 = Dog("barsik", 4, "Haski")  # формально тут запускається __init__
dog2 = Dog("beethoven", 2, "Labrador")
dog3 = Dog("john", 1, "Simple")

# другий песик гавкає
dog2.make_voice()  # self -- dog2
dog1.make_voice()  # self -- dog1

dog3.show_info()

# так краще не робити
# атрибути бажано використовувати лише в методах
# print(dog3.name, dog3.age, dog3.breed)

name1 = dog1.get_name()
print(name1)

print("Before birthday")
dog2.show_info()

dog2.birthday()
dog2.show_info()

dog2.birthday()
dog2.show_info()

dog1.eat("Кістка")
dog2.eat("корм")


nums = [1, 2, 3, 4]
nums.append(10)

text = "hello"
text.replace("l", "m")
