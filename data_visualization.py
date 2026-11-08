import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print("All libraries imported successfully!")
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("tips.csv")

# Display first 5 rows
print(df.head())
# Dataset information

print("\nDataset Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns)

print("\nDataset Information:")
df.info()

print("\nStatistical Summary:")
print(df.describe())
# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())
# Check duplicate records
print("\nDuplicate Records:")
print(df.duplicated().sum())
# Remove duplicate records
df = df.drop_duplicates()

print("\nDataset Shape After Removing Duplicates:")
print(df.shape)
# Average tip by day
avg_tip = df.groupby("day")["tip"].mean()

plt.figure(figsize=(8, 5))
avg_tip.plot(kind="bar")

plt.title("Average Tip by Day")
plt.xlabel("Day")
plt.ylabel("Average Tip")
plt.xticks(rotation=0)

plt.tight_layout()
plt.savefig("average_tip_by_day.png")
plt.show()
# Scatter plot: Total bill vs Tip
plt.figure(figsize=(8, 5))

sns.scatterplot(data=df, x="total_bill", y="tip")

plt.title("Total Bill vs Tip")
plt.xlabel("Total Bill")
plt.ylabel("Tip")

plt.tight_layout()

# Save chart
plt.savefig("total_bill_vs_tip.png")

# Display chart
plt.show()
# Histogram: Distribution of total bills
plt.figure(figsize=(8, 5))

sns.histplot(data=df, x="total_bill", bins=15, kde=True)

plt.title("Distribution of Total Bills")
plt.xlabel("Total Bill")
plt.ylabel("Frequency")

plt.tight_layout()

# Save chart
plt.savefig("total_bill_distribution.png")

# Display chart
plt.show()
# Box plot: Tip distribution by day
plt.figure(figsize=(8, 5))

sns.boxplot(data=df, x="day", y="tip")

plt.title("Tip Distribution by Day")
plt.xlabel("Day")
plt.ylabel("Tip")

plt.tight_layout()

# Save chart
plt.savefig("tip_distribution_by_day.png")

# Display chart
plt.show()
# Heatmap: Correlation between numerical columns
plt.figure(figsize=(8, 5))

correlation = df[["total_bill", "tip", "size"]].corr()

sns.heatmap(correlation, annot=True, cmap="coolwarm", fmt=".2f")

plt.title("Correlation Heatmap")

plt.tight_layout()

# Save chart
plt.savefig("correlation_heatmap.png")

# Display chart
plt.show()
# Final Data Analysis Summary
print("\n========== DATA VISUALIZATION SUMMARY ==========")

print("Total Records:", len(df))

print("Average Total Bill:", round(df["total_bill"].mean(), 2))

print("Average Tip:", round(df["tip"].mean(), 2))

print("Average Group Size:", round(df["size"].mean(), 2))

print("\nAverage Tip by Day:")
print(df.groupby("day")["tip"].mean().round(2))

print("\nHighest Average Tip Day:")
print(df.groupby("day")["tip"].mean().idxmax())