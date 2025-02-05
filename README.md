# Home Loan Prediction using Flask & Machine Learning

## Overview
This project is a *Home Loan Prediction System* built using *Flask, Machine Learning, MongoDB, and JavaScript. It helps determine whether a loan application should be **approved or rejected* based on user input.

## Features
- *Machine Learning Model* trained using Logistic Regression
- *Flask API* for handling predictions and storing applications
- *MongoDB Integration* for storing loan applications
- *User-Friendly Web Interface* using HTML, CSS, and JavaScript

## Tech Stack
- *Backend:* Flask, Scikit-learn, Pandas, NumPy
- *Database:* MongoDB
- *Frontend:* HTML, CSS, JavaScript

## Installation & Setup
### 1. Clone the Repository
bash
git clone https://github.com/your-username/home-loan-prediction.git
cd home-loan-prediction


### 2. Install Dependencies
bash
pip install flask flask-pymongo pandas numpy scikit-learn


### 3. Set Up MongoDB
Ensure you have MongoDB installed and running locally.
bash
mongod --dbpath /path/to/your/mongodb/data


### 4. Train the Model
Ensure loan_data.csv exists in the project directory, then run:
python
python train_model.py


### 5. Start the Flask Server
bash
python app.py

The application will be available at *http://127.0.0.1:5000/*.

## API Endpoints
| Endpoint | Method | Description |
|----------|--------|-------------|
| / | GET | Renders the home page |
| /predict | POST | Predicts loan approval based on user input |
| /submit | POST | Stores user application in MongoDB |

## Usage
1. *Enter loan details* on the web page.
2. *Click "Predict"* to check loan approval status.
3. *Submit application* to store it in the database.

## Sample Dataset (loan_data.csv)
csv
ApplicantIncome,CoapplicantIncome,LoanAmount,Loan_Amount_Term,Credit_History,Loan_Status
5000,0,200,360,1,1
3000,1500,100,360,1,1
4000,0,150,360,1,1
6000,2000,250,360,1,1
2500,1800,120,180,0,0
4500,1200,130,360,1,1


## Contributing
1. *Fork* the repository.
2. *Create a new branch:* git checkout -b feature-name
3. *Commit changes:* git commit -m 'Add new feature'
4. *Push to branch:* git push origin feature-name
5. *Create Pull Request*
