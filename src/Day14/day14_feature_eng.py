import pandas as pd

df = pd.read_csv("D:\DS_AI_Internship\data\data.csv")
df.info()

from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()
df['encoded_col'] = le.fit_transform(df['category'])

df = pd.get_dummies(df, columns=['category'], drop_first=True)

from sklearn.preprocessing import MinMaxScaler, StandardScaler

scaler = StandardScaler()
scaled_features = scaler.fit_transform(df[['age', 'salary']])

from sklearn.preprocessing import PolynomialFeatures

poly = PolynomialFeatures(degree=2, include_bias=False)
poly_features = poly.fit_transform(df[['feature']])