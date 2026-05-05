# # дз
#
# input_thread
#
# sum_thread
# avg_thread
#
# input_thread.start()
# input_thread.join()
#
# sum_thread.start()
# avg_thread.start()
#
# sum_thread.join()
# avg_thread.join()

# серверне програмування
from fastapi import FastAPI
from pydantic import BaseModel

# змінна для застосунку
app = FastAPI()


# запуск
# uvicorn [файл]:[змінна для застосунку] --host [ip адреса] --port [порт]

# ендроінт(функція на сервері)

# @[змінна для застосунку].[http метод]([шлях])
# def func...


@app.get("/hello_endpoint")
def hello():
    return {"message": "hello world"}


@app.post("/register/{user_name}")  # параметр як частина шляху
def register_user(user_name: str):
    return {
        "user": user_name,
        "is_registered": True,
    }


# передача параметрів

# створення схеми для даних


# дані користувача
class User(BaseModel):
    name: str
    age: int
    email: str


class UserResponse(BaseModel):
    user_name: str
    user_age: int
    user_email: str
    is_registered: bool


@app.post("/register")
def register(user: User) -> UserResponse:
    """
    Реєструє користувача
    :param user:
    :return:
    """
    return UserResponse(
        user_name=user.name,
        user_age=user.age,
        user_email=user.email,
        is_registered=True,
    )
