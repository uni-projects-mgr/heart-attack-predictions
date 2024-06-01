from kafka import KafkaConsumer
import requests
import json


API_URL = 'http://api:5000/classify'

class Consumer:
    def __init__(self, bootstrap_servers: list, api_version: tuple, topic_name: str):
        self.consumer = KafkaConsumer(topic_name, bootstrap_servers=bootstrap_servers, api_version=api_version, value_deserializer=lambda x: json.loads(x.decode('utf-8')))

    def receive_sample_message(self) -> list:
        for message in self.consumer:
            sample = message.value
            sample_json = self.convert_string_to_json(sample=sample)

            try:
                response = requests.post(url=API_URL, json=sample_json, headers={'Content-Type': 'application/json'})
                print("Prediction: ", response.json(), flush=True)
            except Exception as e:
                print(e)

    def convert_string_to_json(self, sample: str) -> dict:
        column_names = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal']
        values = sample.split(',')

        return {key: float(value) for key, value in zip(column_names, values)}        

if __name__ == '__main__':
    BOOTSTRAP_SERVERS = ['broker:29092']
    API_VERSION = (0, 0, 1)
    TOPIC_NAME = 'heart-attack-predictions'

    consumer = Consumer(BOOTSTRAP_SERVERS, API_VERSION, TOPIC_NAME)
    consumer.receive_sample_message()
