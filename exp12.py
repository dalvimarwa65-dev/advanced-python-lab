import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Create a sample customer churn dataset
np.random.seed(42)
n = 200

df = pd.DataFrame({
    "CustomerID": range(1, n + 1),
    "Age": np.random.randint(18, 70, n),
    "Tenure": np.random.randint(1, 72, n),
    "MonthlyCharges": np.random.uniform(20, 120, n).round(2),
    "TotalCharges": np.random.uniform(100, 8000, n).round(2),
    "Contract": np.random.choice(["Month-to-month", "One year", "Two year"], n),
    "InternetService": np.random.choice(["DSL", "Fiber optic", "No"], n),
    "Churn": np.random.choice(["Yes", "No"], n, p=[0.30, 0.70])
})

# Introduce some missing values for demonstration
df.loc[[5, 15, 25], "Age"] = np.nan
df.loc[[10, 20], "MonthlyCharges"] = np.nan

print("Original Dataset Head:")
print(df.head())

# 2. Handle missing values
df["Age"] = df["Age"].fillna(df["Age"].median())
df["MonthlyCharges"] = df["MonthlyCharges"].fillna(df["MonthlyCharges"].median())

print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

# 3. Generate summary statistics
print("\nNumerical Summary:")
print(df.describe().round(2))

# 4. Calculate overall churn rate
churn_rate = (df["Churn"].eq("Yes").mean() * 100)
print(f"\nOverall Churn Rate: {churn_rate:.2f}%")

# 5. Analyze patterns by churn
print("\nAverage Customer Details by Churn:")
print(df.groupby("Churn")[["Age", "Tenure", "MonthlyCharges"]].mean().round(2))

# 6. Visualizations
# Churn Distribution
sns.countplot(data=df, x="Churn")
plt.title("Customer Churn Distribution")
plt.show()

# Churn by Contract
sns.countplot(data=df, x="Contract", hue="Churn")
plt.title("Customer Churn by Contract")
plt.show()

# Correlation Heatmap
plt.figure(figsize=(6, 4))
corr = df[["Age", "Tenure", "MonthlyCharges", "TotalCharges"]].corr()
sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Heatmap")
plt.show()

# 7. Save cleaned dataset
df.to_csv("cleaned_customer_churn.csv", index=False)
print("\nCleaned dataset saved successfully as 'cleaned_customer_churn.csv'.")