# This code demonstrates how to analyze distributions using pandas and matplotlib. 
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("data.csv")
plt.hist(data["value"], bins=30)
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.title("Distribution of Values")
plt.show()

# Calculate mean and median
import numpy as np
mean = data["value"].mean()
std = data["value"].std()
data["z_score"] = (data["value"] - mean) / std
data.head()

# Identify outliers using z-scores
import numpy as np
import matplotlib.pyplot as plt

means = []

for _ in range(1000):
    sample = np.random.choice(data["value"], size=30)
    means.append(sample.mean())

# Visualize the distribution of sample means
plt.hist(means, bins=30)
plt.title("Distribution of Sample Means")
plt.show()

sample = data.sample(n=50, random_state=42)
sample.mean(), data.mean()