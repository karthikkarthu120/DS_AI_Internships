import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler, MinMaxScaler

df = pd.DataFrame({
    "Age": [22, 25, 30, 35, 40, 45, 50],
    "Salary": [20000, 25000, 40000, 60000, 80000, 100000, 120000]
})

standard_scaler = StandardScaler()
df_standardized = pd.DataFrame(
    standard_scaler.fit_transform(df),
    columns=df.columns
)

minmax_scaler = MinMaxScaler()
df_normalized = pd.DataFrame(
    minmax_scaler.fit_transform(df),
    columns=df.columns
)

fig, axes = plt.subplots(1, 3, figsize=(15, 4))

axes[0].hist(df["Salary"], bins=5)
axes[0].set_title("Before Scaling")
axes[0].set_xlabel("Salary")
axes[0].set_ylabel("Frequency")

axes[1].hist(df_standardized["Salary"], bins=5)
axes[1].set_title("After Standardization")
axes[1].set_xlabel("Scaled Salary")

axes[2].hist(df_normalized["Salary"], bins=5)
axes[2].set_title("After Normalization")
axes[2].set_xlabel("Scaled Salary (0-1)")

plt.tight_layout()
plt.show()