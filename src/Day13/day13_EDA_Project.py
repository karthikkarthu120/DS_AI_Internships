import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r"D:\DS_AI_Internship\data\dataset.csv")

print(df.head())
print(df.tail())
print(df.shape)
df.info()
print(df.describe())

# Histogram
sns.histplot(df['Age'], kde=True)
plt.show()

# Salary boxplot
sns.boxplot(x=df['Salary'])
plt.show()

# Scatter plot
sns.scatterplot(x='Age', y='Salary', data=df)
plt.show()

# Correlation heatmap (FIX)
numeric_df = df.select_dtypes(include=['number'])
corr = numeric_df.corr()

sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.show()
