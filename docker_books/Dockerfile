FROM python:3.11-slim

WORKDIR /app

COPY ./requirements.txt ./requirements.txt

RUN pip install -r requirements.txt

COPY ./ ./

# вказати хост порт
ENV HOST="0.0.0.0"
ENV PORT=8080

# відкрити порт
EXPOSE 8080

# команда запуску
CMD ["python", "main.py"]
