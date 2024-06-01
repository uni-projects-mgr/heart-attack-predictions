from flask import Flask, request
from apscheduler.schedulers.background import BackgroundScheduler

from model_service import ModelService

app = Flask(__name__)
model = ModelService("./input/heart.csv")

def create_scheduler():
    with app.app_context():
        model.build_and_evaluate()
        scheduler = BackgroundScheduler()
        scheduler.add_job(model.build_and_evaluate, 'cron', minute='*/15')
        scheduler.start()

@app.get('/')
def build_model():
    return model.build_and_evaluate()

@app.post('/classify')
def classify_stream_data():
    response = model.classify(request.json)
    print("Prediction: ", response, flush=True)
    return response

if __name__ == '__main__':
    create_scheduler()
    app.run(host='0.0.0.0', port=5000)
