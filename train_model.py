import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score
import pickle

# Load dataset
df = pd.read_csv("Folds5x2_pp.csv")  # Update with actual dataset path

# Independent and dependent variables
X = df.drop(columns=['PE'])  # Features
y = df['PE']  # Target variable

# Train-test split (80-20)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train models
linear_model = LinearRegression().fit(X_train, y_train)
decision_tree = DecisionTreeRegressor(random_state=42).fit(X_train, y_train)
random_forest = RandomForestRegressor(n_estimators=100, random_state=42).fit(X_train, y_train)

# Function to evaluate models
def evaluate_model(model, X_test, y_test):
    y_pred = model.predict(X_test)
    print(f"Model: {model.__class__.__name__}")
    print(f"R2 Score: {r2_score(y_test, y_pred)}")
    print("-" * 50)

# Evaluate models
evaluate_model(linear_model, X_test, y_test)
evaluate_model(decision_tree, X_test, y_test)
evaluate_model(random_forest, X_test, y_test)

# Save the best model (Random Forest)
pickle.dump(random_forest, open("CCPP.pkl", "wb"))
print("Model saved successfully!")
