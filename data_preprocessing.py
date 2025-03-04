import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split

# Load dataset
df = pd.read_csv("Folds5x2_pp.csv")  # Update with actual dataset path

# Set plot style
sns.set_style("whitegrid")

# Scatter Plots for Univariate & Bivariate Analysis
plt.figure(figsize=(8, 5))
sns.scatterplot(x=df['AT'], y=df['PE'])
plt.title("Temperature vs Power Output")
plt.xlabel("Ambient Temperature (AT)")
plt.ylabel("Power Output (PE)")
plt.show()

plt.figure(figsize=(8, 5))
sns.scatterplot(x=df['V'], y=df['PE'])
plt.title("Exhaust Vacuum vs Power Output")
plt.xlabel("Exhaust Vacuum (V)")
plt.ylabel("Power Output (PE)")
plt.show()

plt.figure(figsize=(8, 5))
sns.scatterplot(x=df['AP'], y=df['PE'])
plt.title("Ambient Pressure vs Power Output")
plt.xlabel("Ambient Pressure (AP)")
plt.ylabel("Power Output (PE)")
plt.show()

plt.figure(figsize=(8, 5))
sns.scatterplot(x=df['RH'], y=df['PE'])
plt.title("Relative Humidity vs Power Output")
plt.xlabel("Relative Humidity (RH)")
plt.ylabel("Power Output (PE)")
plt.show()

# Pair Plot - Showing relationships between all features
sns.pairplot(df)
plt.show()

# Independent and dependent variables
X = df.drop(columns=['PE'])  # Features
y = df['PE']  # Target variable

# Train-test split (80-20)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print("Training Set Size:", X_train.shape)
print("Testing Set Size:", X_test.shape)
