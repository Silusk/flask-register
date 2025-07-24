import numpy as np
import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder

# ------------------------------
# Create a dummy dataset
# ------------------------------
# Features: [days_of_symptoms, age, gender(0=Male,1=Female)]
# Labels: Disease (Common Cold, Flu, Pneumonia)
data = {
    "days": [1, 3, 5, 2, 6, 4, 7, 3, 5, 8],
    "age": [10, 25, 60, 15, 70, 50, 30, 40, 65, 55],
    "gender": ["Male", "Female", "Male", "Male", "Female", "Female", "Male", "Female", "Male", "Female"],
    "disease": ["Cold", "Flu", "Pneumonia", "Cold", "Pneumonia", "Flu", "Cold", "Flu", "Pneumonia", "Flu"]
}

df = pd.DataFrame(data)

# Encode gender
df["gender"] = df["gender"].map({"Male": 0, "Female": 1})

# Encode labels
label_encoder = LabelEncoder()
df["disease"] = label_encoder.fit_transform(df["disease"])  # 0=Cold, 1=Flu, 2=Pneumonia

X = df[["days", "age", "gender"]]
y = df["disease"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a simple Logistic Regression model
model = LogisticRegression()
model.fit(X_train, y_train)

# Save model and label encoder
with open("disease_model.pkl", "wb") as f:
    pickle.dump((model, label_encoder), f)

print("Model trained and saved as disease_model.pkl")
