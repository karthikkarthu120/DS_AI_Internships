import pandas as pd
import numpy as np
data = {
    'value': [45, 50, 52, 47, 49, 51, 53, 46, 48, 200]
}
df = pd.DataFrame(data)
print("Original Dataset:\n")
print(df)
mean = df['value'].mean()
std_dev = df['value'].std()
print("\nMean (μ):", mean)
print("Standard Deviation (σ):", std_dev)
df['z_score'] = (df['value'] - mean) / std_dev
outliers = df[np.abs(df['z_score']) > 3]
print("\nDataset with Z-Scores:\n")
print(df)
print("\nStatistical Outliers (|Z| > 3):\n")
print(outliers)
