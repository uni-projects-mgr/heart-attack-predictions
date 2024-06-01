FROM python:3.10.0-alpine
COPY . /app/
WORKDIR /app
RUN pip install --no-cache-dir --upgrade pip && pip install --no-cache-dir kafka-python requests
CMD ["python", "./consumer.py"]