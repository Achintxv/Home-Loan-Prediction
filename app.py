from flask import Flask, render_template, request
import numpy as np
import joblib

app = Flask(__name__)

# Load trained model
model = joblib.load("home_loan_model.pkl")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Collecting form data
        gross_income = float(request.form['gross_income'])
        tenure = int(request.form['tenure'])
        interest_rate = float(request.form['interest_rate'])
        other_emis = float(request.form['other_emis'])
        credit_score = int(request.form['credit_score'])
        age = int(request.form['age'])
        employment_type = int(request.form['employment_type'])  # Ensure employment type is stored correctly
        loan_amount = float(request.form['loan_amount'])

        # Create feature array
        features = np.array([[gross_income, tenure, interest_rate, other_emis, credit_score, age, employment_type, loan_amount]])

        # Print for debugging
        print(f"Received Input Data: {features}")

        # Predict loan approval
        prediction = model.predict(features)[0]
        result = "Approved" if prediction == 1 else "Not Approved"

        return render_template('index.html', prediction_result=result)

    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)
