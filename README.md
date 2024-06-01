# Heart Attack Predictions Project
 
The created ML model will determine whether there is a high probability of a heart attack for a given sample or not.

The RandomForestClassifier model will be used.

### Data

As a historical data, the ML model will use the following [dataset](https://www.kaggle.com/datasets/rashikrahmanpritom/heart-attack-analysis-prediction-dataset/data).

That dataset describes patients dataset with predictions if the patient is vulnerable to heart attack or not.

All data are numerical and contains 14 columns described below:
- age - patient's age
- sex - patient's gender (0 or 1 - the dataset documentation does not specify which label corresponds to which gender)
- cp - chest pain type (1 - Typical angina, 2 - Atypical angina, 3 - Non-anginal pain, 4 - Asymptomatic)
- trtbps - resting blood pressure in millimeters of mercury (mm Hg)
- chol - cholesterol in milligrams per deciliter (mg/dl) obtained with a BMI sensor
- fbs - a variable indicating whether fasting blood sugar is above 120 milligrams per deciliter (1 - yes, 0 - no)
- rest_ecg - results of resting electrocardiography (0 - normal, 1 - presence of ST-T wave abnormalities, 2 - probable or definite left ventricular hypertrophy according to Estes' criteria)
- thalach - maximum heart rate
- exang - a variable indicating whether chest pain occurs during physical exertion (1 - yes, 0 - no)
- oldpeak - refers to ST segment depression and indicates the depth of change in millimeters
- slp - refers to ST segment slope (1 - upsloping, 2 - flat, 3 - downsloping)
- ca - number of major coronary arteries (0-3)
- thall - indicates blood flow through the heart muscle (1 - normal flow, 2 - fixed defect, 3 - reversible defect)
- output - a variable indicating predictions regarding heart attack (0 - lower chances, 1 - higher chances)

### Docker run

To create and run all containers: `docker-compose up -d`