# app.py
from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np
import pandas as pd

# Load the saved model
with open("employee_attrition_model.pkl", "rb") as file:
    model = pickle.load(file)

app = Flask(__name__)

# Load and process employee data for summary statistics
data = pd.read_csv("employee_data.csv")

# Calculate statistics
total_employees = len(data)
attrition_count = data['Attrition'].sum()
attrition_rate = (attrition_count / total_employees) * 100

@app.route('/')
def home():
    return render_template("index1.html")

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    features = np.array([[data['Age'], data['Department'], data['MonthlyIncome'], data['JobSatisfaction'], data['YearsAtCompany']]])
    prediction = model.predict(features)
    return jsonify({'attrition_risk': bool(prediction[0])})

@app.route('/employee_summary', methods=['GET'])
def employee_summary():
    summary = {
        "total_employees": total_employees,
        "employees_left": attrition_count,
        "attrition_rate": round(attrition_rate, 2)
    }
    summary = {k: int(v) if isinstance(v, np.integer) else v for k, v in summary.items()}

    return jsonify(summary)

if __name__ == '__main__':
    app.run(debug=True)

