from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


# Модель даних
class User(BaseModel):
    name: str
    age: int
    email: str


# Endpoint приймає JSON
@app.post("/users")
def create_user(user: User):
    return {"message": "Користувача створено", "user": user}


# Приклад JSON для відправки:
# {"name": "Іван", "age": 25, "email": "ivan@example.com"}
