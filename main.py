import os  # біліотека для роботи з операціфною системою

import dotenv
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

# параметри підклбчення до бази даних

# краще це зберігати в .env
# host = "localhost"   # ір адркса
# port = 5432          # порт
# user = "postgres"    # користувач
# password = "qwerty"  # пароль
# db = "people"        # назва бази даних


# читаємо .env
dotenv.load_dotenv()

# отримуємо потрібні змінні з .env
host = os.getenv("HOST")
port = os.getenv("PORT")
user = os.getenv("DB_USER")
password = os.getenv("PASSWORD")
db = os.getenv("DB")

# шлях(uri) до бази даних
db_uri = f"postgresql+pg8000://{user}:{password}@{host}/{db}"

# створення підключення(engine)
engine = create_engine(db_uri)

# створення сесії(session) на основі підключення(engine)
Session = sessionmaker(bind=engine)  # клас з можливістю підключення до бази даних
session = Session()  # конкретна сесія

# # отримання таблиць з бази даних
#
# metadata = MetaData()
# metadata.reflect(bind=engine)
#
# tables = metadata.tables
# print(list(tables.keys()))


# запуск sql запиту(дані про конткретного студента)
student_name = input("Введіит ім'я студента")

query = f"""
    SELECT *
    FROM STUDENTS
    where name = '{student_name}'
"""

#  підправити текст
query = text(query)

# запуск
result = session.execute(query)

# виведення результатів(рядків)
for row in result:
    print(row)
