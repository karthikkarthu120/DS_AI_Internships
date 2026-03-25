# PCA (Principal Component Analysis) is a dimensionality reduction technique that transforms a dataset into a new coordinate system. The new coordinates (principal components) are ordered such that the first few retain most of the variation present in the original dataset. This is particularly useful for reducing the number of features while preserving as much information as possible.
import numpy as np
import pandas as pd
from sklearn.datasets import load_iris

# Load dataset
data = load_iris()
df = pd.DataFrame(data.data, columns=data.feature_names)

# Calculate Variance for each feature
variances = df.var()

print("Feature Variances:")
print(variances)
print("\nFeature with highest variance:", variances.idxmax())
print("Feature with lowest variance:", variances.idxmin())


# Standardization is crucial before applying PCA because PCA is sensitive to the scales of the features. If the features are on different scales, PCA may give more weight to those with larger ranges, leading to skewed results. Standardizing the data ensures that each feature contributes equally to the analysis by centering the data around the mean and scaling it to unit variance.
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import pandas as pd
from sklearn.datasets import load_iris

# Load and Scale
data = load_iris()
X = data.data

# 1. Standardization is MANDATORY
X_scaled = StandardScaler().fit_transform(X)

# 2. Fit PCA
pca = PCA()
pca.fit(X_scaled)

print(f"Original shape: {X.shape}")
print(f"Number of components found: {pca.n_components_}")
print("\nPrincipal Components (Eigenvectors):\n", pca.components_)


# Explained Variance Ratio
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import load_iris
import numpy as np

# Setup
X = load_iris().data
X_scaled = StandardScaler().fit_transform(X)

# Fit PCA
pca = PCA()
pca.fit(X_scaled)

# Ratios
ratios = pca.explained_variance_ratio_
cumulative = np.cumsum(ratios)

print("Variance explained by each component:")
for i, r in enumerate(ratios):
    print(f"PC{i+1}: {r:.4f} ({r*100:.1f}%)")

print("\nCumulative Variance:")
print(cumulative)
print(f"\nFirst 2 components capture {cumulative[1]*100:.1f}% of the data!")


# PCA for Dimensionality Reduction
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import load_iris
import pandas as pd

# Load
iris = load_iris()
X_scaled = StandardScaler().fit_transform(iris.data)

# Reduce to 2 Components
pca_2 = PCA(n_components=2)
X_reduced = pca_2.fit_transform(X_scaled)

print(f"Original shape: {X_scaled.shape}")
print(f"Reduced shape: {X_reduced.shape}")
print("\nFirst 5 rows of reduced data (PC1, PC2):")
print(X_reduced[:5])

# In a real notebook, you would now use:
# plt.scatter(X_reduced[:, 0], X_reduced[:, 1], c=iris.target)