# Модель: Метод Ейлера (5 семестр)

# Автор: Самсонов Віталій, група АІ-233

FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY euler.py .

CMD ["python", "euler.py"]
