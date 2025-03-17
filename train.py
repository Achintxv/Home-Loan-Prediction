import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import joblib

# Load dataset
df = pd.read_csv('loan_data.csv')

# Clean column names
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

# Encode employment_type
df['employment_type'] = df['employment_type'].str.lower().map({
    'salaried': 0,
    'self-employed': 1
})

# Features & target
X = df[['gross_income', 'tenure', 'interest_rate', 'other_emis', 'credit_score', 'age', 'employment_type']]
y = df['loan_amount']

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train
model = LinearRegression()
model.fit(X_train, y_train)

# Save model
joblib.dump(model, 'home_loan_model.pkl')
print("✅ Model trained and saved as 'home_loan_model.pkl'")