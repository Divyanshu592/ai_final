# app.py
import random
import joblib

print("ML-Ops Assignment Script Running...")

# Dummy "training" and save model
model = {"class_A_prob": 0.5, "class_B_prob": 0.3, "class_C_prob": 0.2}
joblib.dump(model, "model.joblib")

# Dummy "prediction"
input_data = [1, 2, 3, 4]
prediction = random.choice(["Class A", "Class B", "Class C"])

print(f"Input: {input_data}")
print(f"Prediction: {prediction}")
print("Model saved as model.joblib")
