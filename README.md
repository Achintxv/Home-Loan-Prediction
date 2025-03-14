# 🏡 Home Loan Eligibility Calculator
An **AI-powered web application** to predict home loan eligibility and calculate estimated EMIs based on user inputs like gross income, tenure, credit score, age, and more. This project combines **Machine Learning (Linear Regression)** with a simple **Flask backend** and **interactive frontend (HTML/CSS/JS)**.

> ⚡ **Accuracy**: ~85% based on our testing dataset.  
> 📂 **Model**: Linear Regression  
> 📝 **Dataset**: `loan_data.csv` (cleaned and preprocessed)

---

## 🚀 Features

✅ Predict home loan eligibility instantly  
✅ Calculate EMI based on predicted loan amount and interest rate  
✅ Interactive sliders and inputs for real-time feedback  
✅ Clean and responsive UI  
✅ Credit Score, Age, and Employment Type integrated into prediction  
✅ Built with Python, Flask, and Scikit-learn

---

## 📊 Tech Stack

- **Frontend**: HTML, CSS, JavaScript  
- **Backend**: Python Flask  
- **ML Model**: Scikit-learn (Linear Regression)  
- **Model Serving**: joblib  
- **API**: RESTful (Flask)  
- **Extras**: CORS enabled for smooth interaction

---

## 🔧 How It Works

1. **Frontend (HTML/CSS/JS)** collects inputs like:
   - Gross Income (Monthly)
   - Tenure (Years)
   - Interest Rate (% P.A.)
   - Other EMIs (Monthly)
   - Credit Score
   - Age
   - Employment Type

2. Inputs are sent to the Flask backend `/predict` endpoint.

3. **Flask** loads the trained Linear Regression model (`home_loan_model.pkl`).

4. Prediction of **eligible loan amount** is done on the backend.

5. EMI is calculated using the standard **EMI formula**:
   ```
   EMI = [P × r × (1 + r)^n] / [(1 + r)^n – 1]
   ```

6. Results (Loan Eligibility and EMI) are returned to the frontend and displayed in real-time.

---

## 📂 Project Structure

```
├── static/
│   ├── style.css
│   └── script.js
├── templates/
│   └── index.html
├── loan_data.csv
├── train.py
├── app.py
├── home_loan_model.pkl
└── README.md
```

---

## ⚙️ Installation & Running Locally

### Prerequisites:
- Python 3.8+
- pip
- Flask, Scikit-learn, joblib

### Steps:

```bash
# Clone the repository
git clone https://github.com/your-username/home-loan-eligibility-calculator.git
cd home-loan-eligibility-calculator

# Install dependencies
pip install flask scikit-learn joblib flask-cors pandas numpy

# Train the model (if needed)
python train.py

# Start Flask server
python app.py
```

👉 Open your browser and visit:  
`http://127.0.0.1:5000`

---

## 🎯 Accuracy & Model Performance

| Metric      | Value  |
|-------------|--------|
| Model       | Linear Regression |
| Accuracy    | ~85% (on test data) |
| Dataset     | Custom (cleaned) |
| Features    | 7 (Gross Income, Tenure, Interest Rate, Other EMIs, Credit Score, Age, Employment Type) |

---

## ⚠️ Disclaimer

> This **Home Loan Eligibility Calculator** is developed **for demonstration and educational purposes** only.  
> Different banks and financial institutions use **proprietary algorithms and policies** to assess home loan eligibility. Factors such as risk profiling, customer relationship, income verification, and legal checks may significantly affect the loan offer.  
> **We do not guarantee** accuracy in real-world financial decisions based on this application.

---

## 👥 Contributors

Thanks to these wonderful people for their contributions! 🎉

| Name            | GitHub Profile                    | Contribution                |
|-----------------|----------------------------------|-----------------------------|
| **Achint Verma**  | (https://github.com/Achintxv) | Backend Development UI/UX Backend API |
| **Khushi Dhruw**  | (https://github.com/kdhruw05) | Machine Learning Model |
| **Nikhil Kumar**  | (https://github.com/nikhil0019) | Backend Development |
| **Gayathri Devdas**  | (https://github.com/Gayathrid04) | Frontend Development |
| **Laxmirlola Behera**    | (https://github.com/Laxmirlola)   | Frontend Development |

---

Feel free to connect and contribute!

## 🌟 Support

If you find this project helpful, please ⭐ **star** the repo to support the project!

---
