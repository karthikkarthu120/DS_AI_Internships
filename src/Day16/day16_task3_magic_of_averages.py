import numpy as np
import matplotlib.pyplot as plt
np.random.seed(42)
data = np.random.exponential(scale=2, size=10000)

plt.figure()
plt.hist(data, bins=50, density=True)
plt.title("Original Skewed Dataset (Income-like)")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()

sample_means = []

for i in range(1000):        
    sample = np.random.choice(data, size=30)  
    sample_means.append(np.mean(sample))
plt.figure()
plt.hist(sample_means, bins=40, density=True)
plt.title("Distribution of Sample Means (n=30, 1000 samples)")
plt.xlabel("Sample Mean")
plt.ylabel("Frequency")
plt.show()
