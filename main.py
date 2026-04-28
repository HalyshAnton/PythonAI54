# пакування даних

# import json
#
#
# class Person:
#     pass
#
# data = {
#     "name": "John",
#     "age": 45,
# }
#
#
# with open("user_info.json", "w", encoding="utf-8") as file:
#     json.dump(data, file, indent=2)
#
#
# with open("user_info.json", "r", encoding="utf-8") as file:
#     new_data = json.load(file)
#
# print(new_data)
# print(new_data["age"])


# У json є обмеження через те що він має бути сумісним з
# іншими мовами
#
# Чисто для Python є pickle

import pickle

data = {"name": "John", "age": 45, "items": {12, 3, 4, 5}}

# # кодування інформації
# encoded = json.dumps(data)
# print(encoded)
# print(type(encoded))
#
# encoded = pickle.dumps(data)
# print(encoded)
# print(type(encoded))

# для pickle файл треба відкривати для запису байтів

with open("user_info.pkl", "wb") as f_out:
    pickle.dump(data, f_out)


with open("user_info.pkl", "rb") as f_in:
    new_data = pickle.load(f_in)


print(new_data)
print(type(new_data))
print(new_data["age"])


class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def info(self):
        print(f"Name: {self._name}, age: {self._age}")


person = Person("Mary", 23)

# with open("person.pkl", "wb") as file:
#     pickle.dump(person, file)
#
#
# with open("person.pkl", "rb") as file:
#     new_person = pickle.load(file)
#
#
# new_person.info()
