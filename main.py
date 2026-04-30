# паралельне програмування(потокове)
#
#
# Кухар
# Задачі де потрбна увага кухаря
# - нарізати овочі
# - смажити стейк
# - перевірка смаку(добавляння спецій)
#
# Задачі які виконуються без кухаря
# - закипить вода
# - щось випікається
# - маринується стейк

# в програмуванні є схожі задачі
# CPU(процесор) - задачі
# - рахується сума чисел
# - відтворюєте відео
# - відобразити вміст сайту

# I\O(input output) задачі -- це коли процесор чекає на відповідь сервера
# - очікування коли прогрузиться сайт
# - очікування коли чат гпт дасть відповість
# - очуківання коли завантажиться відео на ютуб


# name = input()
# result = func(name)
# print(result)

# асинхронність
# один кухар на одній кухні працює розумно(
# поки закіпає вода і маринується стейк він ріже овочі)

# в програмуванні -- асинхронні функції

# багато процесорність
# багато кухарів на багатьох кухня
#
# "кухні" -- це ядра процесора

# multiprocessing

# багато потоковість
# багато кухарів на одній кухні, але вони виконують задачі почерзі
# поки один смажить за плитою інші чекають
#
# потоки -- thread

# import multiprocessing
# import thread
# import asyncio


# потоки
import threading
import time

# def long_func():
#     total = 0
#     for i in range(50_000_000):
#         total += i
#     print("finish")
#
#
# start = time.time()
# long_func()
# end = time.time()
# print(f"Час виконання: {end - start}")
#
# # # код звичайний
# # start = time.time()
# # long_func()
# # long_func()
# # end = time.time()
# # print(f"Час виконання: {end - start}")
#
# # потоки
# thread1 = threading.Thread(
#     target=long_func,  # функція яка виконується під час потоку
# )
#
# thread2 = threading.Thread(
#     target=long_func,  # функція яка виконується під час потоку
# )
#
# start = time.time()
#
# # запускаємо потоки
# thread1.start()  # запускається потік
# thread2.start()  # не чекає завершення thread1
#
# print("hi")  # виконується паралельно з потоками
#
# # чекаємо поки потоки закінчаться
# thread1.join()
# thread2.join()
# # ось тут гарантується що потоки закінчили роботу
#
# end = time.time()
# print(f"Час виконання: {end - start}")


# # параметри для функцій
#
# def print_text(text):
#     for _ in range(20):
#         print(text+"\n", end="")
#
#
# thread1 = threading.Thread(
#     target=print_text,   # функція
#     #args=("hello1",),   # параметри функції
#     kwargs={"text": "hello1"}  # теж  параметри тільки словником
# )
#
# thread2 = threading.Thread(
#     target=print_text,
#     #args=("hello1",),   # параметри функції
#     kwargs={"text": "hello2"}  # теж  параметри тільки словником
# )
#
#
# thread1.start()
# thread2.start()
#
#
# thread1.join()
# thread2.join()
#
# print("END")


# результат функції


def add(num1: int, num2: int, res: dict[str, int]):
    time.sleep(2)
    res["res"] = num1 + num2


res: dict[str, int] = {}
thread = threading.Thread(
    target=add,
    args=(2, 3, res),
)

thread.start()
print(res)  # результату ще нема
thread.join()
print(res)
