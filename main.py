import pandas as pd
from sklearn.ensemble import RandomForestClassifier

# Dummy example (since we don't load full dataset here)
def predict_transaction(amount):
    if amount > 2000:
        return "High Risk (Possible Fraud)"
    else:
        return "Normal Transaction"

if __name__ == "__main__":
    amt = float(input("Enter transaction amount: "))
    result = predict_transaction(amt)
    print("Prediction:", result)
