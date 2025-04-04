from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# Load trained model
model = joblib.load("home_loan_model.pkl")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Get user input
        gross_income = float(request.form["gross_income"])
        tenure = int(request.form["tenure"])
        interest_rate = float(request.form["interest_rate"])
        other_emis = float(request.form["other_emis"])
        credit_score = int(request.form["credit_score"])
        age = int(request.form["age"])
        employment_type = int(request.form["employment_type"])
        loan_amount = float(request.form["loan_amount"])

        # Create input array
        input_data = np.array([[gross_income, tenure, interest_rate, other_emis, credit_score, age, employment_type, loan_amount]])

        # Predict
        prediction = model.predict(input_data)

        # Convert prediction to text
        result_text = "✅ Loan Approved" if prediction[0] == 1 else "❌ Loan Not Approved"

        return render_template("index.html", prediction=result_text)

    except Exception as e:
        return render_template("index.html", prediction="Error in prediction: " + str(e))

if __name__ == "__main__":
    app.run(debug=True)
