FROM python:3.10.0-alpine
COPY . /app/
WORKDIR /app
RUN pip install --no-cache-dir --upgrade pip && pip install --no-cache-dir kafka-python
CMD ["python", "./producer.py"]