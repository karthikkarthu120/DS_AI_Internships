import pandas as pd
df = pd.read_csv("customer_orders.csv")
print("Original shape:", df.shape)
print("\nMissing values report:")
print(df.isna().sum())
num_cols = df.select_dtypes(include=['number']).columns
df[num_cols] = df[num_cols].fillna(df[num_cols].median())
df = df.drop_duplicates()
print("\nCleaned shape:", df.shape)
df.to_csv('D:\\DS_AI_Internship\\src\\Datasets\\cdata.csv', index=False)
