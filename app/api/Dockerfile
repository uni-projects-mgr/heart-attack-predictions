FROM python:3.10.0-alpine
RUN apk add --no-cache openjdk11-jre bash

ENV JAVA_HOME=/usr/lib/jvm/java-11-openjdk
ENV PATH=$PATH:$JAVA_HOME/bin

COPY . /app/
WORKDIR /app
EXPOSE 5000
RUN pip install --no-cache-dir --upgrade pip && pip install --no-cache-dir apscheduler flask pyspark numpy findspark

CMD ["python", "./app_controller.py"]