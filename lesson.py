# json
import json

# робота з файлами
data = {
    "name": "Антон",
    "age": 24,
}

# # запис
# with open("data.txt", "w", encoding="utf-8") as file:
#     print(str(data), file=file)
#
# # читання
# with open("data.txt", "r", encoding="utf-8") as file:
#     new_data = file.read()
#
# print(type(new_data))
# print(new_data)

data = {
    "name": "Антон",
    "age": 24,
    "items": ["bread", "apple", "milk", "butter"],
    "is_good": True,
    "salary": 500.25,
    "data": None,
}

# # дозволені типи даних
# # dict, int, float, bool, None, str, list
#
# # збережання даних у файл з json
# with open("data.json", "w", encoding="utf-8") as file:
#     # json.dump(data, file)
#     # стандартне кодування -- ascii
#     # ensure_ascii=False -- дозволити інші кодування також
#     # indent -- відступи
#     json.dump(data, file, indent=2, ensure_ascii=False)
#
#
# # читання даних
# with open("data.json", "r", encoding="utf-8") as file:
#     # json.load(file)
#     new_data = json.load(file)
#
#
# print(type(new_data))
# print(new_data)
# print(new_data["name"])

# # json переводить дані в байти(str але не зовсім)
#
# # переведення даних в байти
# raw_bytes = json.dumps(data, ensure_ascii=False)
# print(type(raw_bytes))
# print(raw_bytes)
# print(repr(raw_bytes)) # так як це виглядало б в коді
#
#
# # перевести байти в нормальних тип даних
# new_data = json.loads(raw_bytes)
# print(type(new_data))
# print(new_data)
# print(new_data["name"])


# Користувач вводить назву та ціну продукту. Добавте їх у кошик
# Також збережіть дані у файл

FILENAME = "cart.json"


def add_new_item(cart: dict):
    item = input("Enter item name: ")
    price = float(input("Enter price: "))

    cart[item] = price


def save_cart(cart: dict):
    with open(FILENAME, "w", encoding="utf-8") as file:
        json.dump(cart, file, indent=2)


def load_cart():
    with open(FILENAME, encoding="utf-8") as file:
        cart = json.load(file)

    return cart


if __name__ == "__main__":
    cart = load_cart()

    while True:
        commad = int(input("enter command: "))

        if commad == 1:
            add_new_item(cart)

        elif commad == 2:
            save_cart(cart)
