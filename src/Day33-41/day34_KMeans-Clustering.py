# K-Means Clustering Example
import numpy as np

# Define some points in a cluster
points = np.array([[1, 2], [1, 4], [5, 8]])

# Calculate the centroid (mean along axis 0)
centroid = points.mean(axis=0)

print(f"Points:\n{points}")
print(f"\nCalculated Centroid: {centroid}")

# K-Means Clustering with Scikit-learn
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import numpy as np

# Synthetic data: 2 features
X = np.array([[1, 2], [1, 4], [1, 0], [10, 2], [10, 4], [10, 0]])

# 1. Scale the data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 2. Fit K-Means with K=2
kmeans = KMeans(n_clusters=2, random_state=42, n_init=10)
labels = kmeans.fit_predict(X_scaled)

print(f"Original Data:\n{X}")
print(f"\nCluster Labels: {labels}")
print(f"\nCentroids:\n{kmeans.cluster_centers_}")


# Elbow Method to Determine Optimal K
from sklearn.cluster import KMeans
import numpy as np

# Synthetic data
X = np.random.rand(100, 2)

inertia = []
K_range = range(1, 11)

for k in K_range:
    model = KMeans(n_clusters=k, random_state=42, n_init=10)
    model.fit(X)
    inertia.append(model.inertia_)

print("K values tested: ", list(K_range))
print("Inertia values: ", [round(i, 2) for i in inertia])
print("\nLook for the 'elbow' where the drop in inertia slows down.")


# K-Means Clustering on Synthetic Data
from sklearn.cluster import KMeans
import numpy as np

# 1. Generate data
X = np.random.randn(50, 2) + [2, 2]
X2 = np.random.randn(50, 2) + [-2, -2]
X_final = np.vstack([X, X2])

# 2. Fit K-Means
kmeans = KMeans(n_clusters=2, random_state=42, n_init=10)
labels = kmeans.fit_predict(X_final)

# 3. Get Centroids
centers = kmeans.cluster_centers_

print(f"Total points: {len(X_final)}")
print(f"Centroid 1: {centers[0]}")
print(f"Centroid 2: {centers[1]}")
print("\nIn a real notebook, you would now use plt.scatter(X[:,0], X[:,1], c=labels)")