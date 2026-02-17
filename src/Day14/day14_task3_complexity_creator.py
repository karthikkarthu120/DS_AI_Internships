import pandas as pd
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score

df = pd.DataFrame({
    "Feature": [1,2,3,4,5,6,7,8,9,10],
    "Target":  [2,5,10,17,26,37,50,65,82,101]
})

X = df[["Feature"]]
y = df["Target"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

linear_model = LinearRegression()
linear_model.fit(X_train, y_train)

y_pred_linear = linear_model.predict(X_test)
r2_linear = r2_score(y_test, y_pred_linear)

poly = PolynomialFeatures(degree=2)
X_train_poly = poly.fit_transform(X_train)
X_test_poly = poly.transform(X_test)

poly_model = LinearRegression()
poly_model.fit(X_train_poly, y_train)

y_pred_poly = poly_model.predict(X_test_poly)
r2_poly = r2_score(y_test, y_pred_poly)

print("R² score (Linear Model):", r2_linear)
print("R² score (Polynomial Model):", r2_poly)

if r2_poly > r2_linear:
    print("Curved (polynomial) features improved the model")
else:
    print("Polynomial features did not help")
