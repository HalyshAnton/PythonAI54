# # магічні методи
#
# nums = [1, 2, 3, 4]
#
# # явний метод
# nums.append(5)
#
# # неявні методи(магічні)
# nums[0]   # __getitem__
# nums + [1, 2, 3, 4]  # __add__
#
# num = 10
# num + 5
# res = num.__add__(5)
# print(res)


class Person:
    def __init__(self, name, age):
        print("hello from __init__")
        self._name = name
        self._age = age

    def __str__(self):  # str(person)
        print("hello from __str__")
        return f"Person named {self._name}, {self._age} yr"

    def __eq__(self, other):
        print("hello from __eq__")
        # other може бути будя-якого типу даних
        if isinstance(other, Person):
            return self._name == other._name and self._age == other._age

        elif isinstance(other, str):
            # вважаємо other ім'ям
            return self._name == other

        return False

    def __gt__(self, other):  # self > other
        print("hello from __gt__")

        if isinstance(other, Person):
            return self._age > other._age

        # якщо other не Person
        raise TypeError(f"не можна порівнювати Person та {type(other)}")


# # метод __init__
# person1 = Person("John", 37)
# person2 = Person("Mary", 28)
# person3 = Person("Max", 16)
#
# # __str__
# print(person1)
#
# # __eq__
# print(person1 == person3)  # self=person1, other=person2
# print(person1 == "John")
# print(person1 == [1, 2, 3, 4])
#
# num = 10
#
# # __gt__
# # print(10 > "hello")
# print(person1 > person2)
# # print(person1 > "Mary")
#
# people = [person1, person2, person3]
# people = sorted(people)
#
# for person in people:
#     print(person)


class Cart:
    def __init__(self, items: list):
        self._items = items

    def __str__(self):
        return f"Cart: {self._items}"

    def __contains__(self, item):
        return item in self._items

    def __getitem__(self, index):
        return self._items[index]

    def __setitem__(self, index, new_item):
        self._items[index] = new_item

    def __iter__(self):
        print("hello from __iter__")
        return iter(self._items)

    def generator(self):
        # for item in self._items:
        #     yield item
        yield from self._items


cart = Cart(["milk", "butter", "bread"])
print(cart)
#
# # __contains__

print("milk" in cart)  # item = "milk"
# print("banana" in cart)
#
# # __getitem__
# print(cart[-1])
#
# # __setitem__
# cart[0] = "avocado"
# print(cart)

# # __iter__
# for i in range(1, 5):
#     print(f"Ітерація циклу з {i = }")
#     print("hello")
#
#
# for item in cart:
#     print(item)

for item in cart.generator():
    print(item)


# генератори
def my_range(start, stop, scale=2):
    num = start

    while num <= stop:
        yield num  # як return тільки не зупиняє функцію
        num *= scale


# ступені двійки(1 2 4 8 16 32 ..)
for num in my_range(1, 100, 2):
    print(num)
