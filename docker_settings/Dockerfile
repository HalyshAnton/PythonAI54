# версія пайтон

FROM python:3.11-slim

# базова папка(куди копіювати файли)
WORKDIR /app

# скопіювати файли
COPY ./ ./

# встановити бібліотеки
RUN pip install -r requirements.txt

# вказати налаштування(змінну середовища)
ENV MIN_NUM=0

# команда для запуску
CMD ["python", "-u", "main.py"]
