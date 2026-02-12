import pandas as pd
df = pd.read_csv("cdata.csv")
print("Initial data types:\n")
print(df.dtypes)
df["Price"] = (
    df["Price"]
    .astype(str)                 
    .str.replace("$", "", regex=False) 
    .str.replace(",", "", regex=False)  
)
df["Price"] = pd.to_numeric(df["Price"], errors="coerce")
df["date"] = pd.to_datetime(df["date"], errors="coerce")
print("\nUpdated data types:\n")
print(df.dtypes)
