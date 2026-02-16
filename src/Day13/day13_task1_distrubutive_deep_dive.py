import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = {
    "Price": [200000, 220000, 250000, 270000, 300000,
              320000, 350000, 370000, 400000, 900000],
    "City": ["Bangalore", "Mumbai", "Bangalore", "Delhi",
             "Mumbai", "Delhi", "Bangalore", "Mumbai",
             "Delhi", "Mumbai"]
}

df = pd.DataFrame(data)

sns.histplot(df["Price"], kde=True)
plt.title("Price Distribution")
plt.show()

print("Skewness:", df["Price"].skew())
print("Kurtosis:", df["Price"].kurt())

sns.countplot(x="City", data=df)
plt.title("City Frequency")
plt.show()
