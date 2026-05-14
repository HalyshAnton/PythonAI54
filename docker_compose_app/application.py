from fastapi import FastAPI

# створення об'єкта класу FastAPI
app = FastAPI()


@app.get("/hello_endpoint")
def hello():
    return {"message": "hello", "status": "OK"}
