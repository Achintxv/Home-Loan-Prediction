from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import joblib
import numpy as np

app = Flask(__name__)
CORS(app)

# Load model
model = joblib.load('home_loan_model.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    print("📦 Incoming data:", data)

    try:
        gross_income = float(data.get('gross_income', 0))
        tenure = float(data.get('tenure', 0))
        interest_rate = float(data.get('interest_rate', 0))
        other_emis = float(data.get('other_emis', 0))
        credit_score = float(data.get('credit_score', 0))
        age = float(data.get('age', 0))
        employment_type_str = data.get('employment_type', 'Salaried').lower()
        employment_type = 0 if employment_type_str == 'salaried' else 1

        # Features for prediction
        features = np.array([[gross_income, tenure, interest_rate, other_emis, credit_score, age, employment_type]])
        predicted_loan_amount = model.predict(features)[0]

        # EMI Calculation
        def calculate_emi(principal, rate_of_interest, years):
            monthly_interest = rate_of_interest / (12 * 100)
            months = years * 12
            if monthly_interest == 0:
                return principal / months
            emi = (principal * monthly_interest * (1 + monthly_interest) ** months) / ((1 + monthly_interest) ** months - 1)
            return emi

        emi = calculate_emi(predicted_loan_amount, interest_rate, tenure)

        response = {
            'loan_amount': round(predicted_loan_amount, 2),
            'emi': round(emi, 2)
        }

        print("✅ Prediction:", response)
        return jsonify(response)

    except Exception as e:
        print("❌ Error:", str(e))
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
