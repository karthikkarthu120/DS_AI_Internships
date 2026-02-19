import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
np.random.seed(42)

heights = np.random.normal(loc=170, scale=7, size=1000)

incomes = np.random.exponential(scale=50000, size=1000)

scores = 100 - np.random.exponential(scale=10, size=1000)

df = pd.DataFrame({
    "Heights": heights,
    "Incomes": incomes,
    "Scores": scores
})

plt.figure(figsize=(15,5))

for i, col in enumerate(df.columns, 1):
    plt.subplot(1,3,i)
    sns.histplot(df[col], kde=True)
    plt.title(col)

plt.tight_layout()
plt.show()

for col in df.columns:
    mean_val = df[col].mean()
    median_val = df[col].median()

    print(f"\n{col}")
    print("Mean   :", round(mean_val,2))
    print("Median :", round(median_val,2))

    if mean_val > median_val:
        print("➡ Right-Skewed Distribution")
    elif mean_val < median_val:
        print("➡ Left-Skewed Distribution")
    else:
        print("➡ Normal Distribution")
