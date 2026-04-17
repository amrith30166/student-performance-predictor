import joblib
import numpy as np
import os

# Load model safely
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(BASE_DIR, "model1.pkl")

model = joblib.load(model_path)

def predict_score(hours, attendance, previous):
    features = np.array([[hours, attendance, previous]])
    return model.predict(features)[0]