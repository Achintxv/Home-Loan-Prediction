import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import joblib

# Load dataset
df = pd.read_csv('loan_data_corrected.csv')

# Clean column names
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

# Convert 'yes'/'no' to 1/0
df['prediction'] = df['prediction'].map({'yes': 1, 'no': 0})


# Encode employment_type
df['employment_type'] = df['employment_type'].map({'salaried': 0, 'self-employed': 1})

# Define features and target
X = df[['gross_income', 'tenure', 'interest_rate', 'other_emis', 'credit_score', 'age', 'employment_type', 'loan_amount']]
y = df['prediction']

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = LogisticRegression()
model.fit(X_train, y_train)

# Save trained model
joblib.dump(model, 'home_loan_model.pkl')

print("✅ Model trained and saved as home_loan_model.pkl")
