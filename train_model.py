# train_model.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle

# Load dataset
data = pd.read_csv("employee_data.csv")
# data = pd.read_csv()

# Encode categorical data (Department)
data['Department'] = data['Department'].map({"Sales": 0, "Research & Development": 1, "Human Resources": 2})

# Define features and target
X = data[['Age', 'Department', 'MonthlyIncome', 'JobSatisfaction', 'YearsAtCompany']]
y = data['Attrition']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a model 
model = RandomForestClassifier(n_estimators=100, random_state=42)   
model.fit(X_train, y_train)

# Save the trained model
with open("employee_attrition_model.pkl", "wb") as file:
    pickle.dump(model, file)

print("Model trained and saved as employee_attrition_model.pkl")
