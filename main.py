# redis в python
from redis import Redis

# підключення
host = "localhost"
port = 6379

server = Redis(
    host="localhost",
    port=6379,
    db=0,  # індекс бази даних
    decode_responses=True,  # щоб повертало не сирі байти
)


# отримати значення ключа
user_name = server.get("name")
print(user_name)


# добавити новий ключ
server.set("name", "Alice")
