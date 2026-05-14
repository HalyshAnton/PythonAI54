# версія пайтона
FROM python:3.11-slim

# створення папки для файлів
WORKDIR /app

# копіємо requirements.txt і встановлюємо біліотеки
COPY ./requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

# копіюємо решту файлів
COPY ./ ./

# запуск
CMD ["python", "-u", "main.py"]
