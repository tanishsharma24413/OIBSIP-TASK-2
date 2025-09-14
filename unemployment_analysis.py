import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Create a synthetic dataset
data = {
    "State": ["Delhi", "Maharashtra", "Karnataka", "Tamil Nadu", "Uttar Pradesh"] * 6,
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"] * 5,
    "Unemployment_Rate": [7.5, 8.1, 6.9, 7.8, 8.3, 7.2,
                          9.0, 9.5, 8.2, 8.7, 9.3, 9.1,
                          6.1, 6.8, 6.5, 7.0, 7.3, 6.9,
                          5.8, 6.3, 5.9, 6.2, 6.5, 6.1,
                          10.5, 10.2, 9.8, 10.0, 10.8, 10.3]
}

df = pd.DataFrame(data)
print("Dataset sample:\n", df.head())

# Step 2: Summary statistics
print("\nAverage unemployment rate by state:\n")
print(df.groupby("State")["Unemployment_Rate"].mean())

# Step 3: Visualization

# 1. Unemployment trend by state
plt.figure(figsize=(10,6))
sns.lineplot(data=df, x="Month", y="Unemployment_Rate", hue="State", marker="o")
plt.title("Unemployment Trend in India (Synthetic Data)")
plt.ylabel("Unemployment Rate (%)")
plt.show()

# 2. Average unemployment by state (bar chart)
plt.figure(figsize=(8,5))
sns.barplot(data=df, x="State", y="Unemployment_Rate", estimator="mean", ci=None, palette="Set2")
plt.title("Average Unemployment Rate by State")
plt.ylabel("Avg. Unemployment Rate (%)")
plt.show()
