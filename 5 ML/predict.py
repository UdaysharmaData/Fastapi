import joblib
import numpy as np

saved_model = joblib.load("model.joblib") 
print("Model Loaded successfully")



def make_preditcion(data:dict) -> float:
    features = np.array([
        [
            data['longitude'],
            data['latitude'],
            data['housing_median_age'],
            data['total_rooms'],
            data['total_bedrooms'],
            data['population'],
            data['household'],
            data['median_income']

        ]
    ])

    return saved_model.predict(features)[0]
