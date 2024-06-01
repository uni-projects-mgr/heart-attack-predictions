import time
import json

from kafka import KafkaProducer

class Producer:
    def __init__(self, bootstrap_servers: list, topic_name: str, api_version: tuple):
        self.topic_name = topic_name
        self.producer = KafkaProducer(bootstrap_servers=bootstrap_servers, api_version=api_version)
        print("Producer initialized")

    def generate_data(self) -> list:
        with open('./input/data.csv', 'r') as f:
            data = f.readlines()
        return data
    
    def send_sample(self, sample: str) -> None:
        self.producer.send(self.topic_name, value=json.dumps(sample).encode('utf-8'))

    def shutdown(self) -> None:
        self.producer.close()

if __name__ == '__main__':
    BOOTSTRAP_SERVERS = ['broker:29092']
    TOPIC_NAME = 'heart-attack-predictions'
    API_VERSION = (0, 0, 1)

    producer = Producer(BOOTSTRAP_SERVERS, TOPIC_NAME, API_VERSION)

    data = producer.generate_data()

    for sample in data:
        print(f"Sample in Produer queue: {sample}", flush=True)
        producer.send_sample(sample)
        time.sleep(10)
    producer.shutdown()