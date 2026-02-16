import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.DataFrame({
    'Sales': [200,220,250,270,300,320,350,370,400,1000],
    'Advertising': [20,22,25,27,30,32,35,37,40,95],
    'Profit': [50,55,60,65,70,75,80,85,90,200],
    'Customers': [100,110,120,130,150,160,170,180,190,500]
})

corr = df.corr()
print(corr)

sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()

print("\nHighly Correlated Features (>0.8):")
for i in range(len(corr.columns)):
    for j in range(i):
        if abs(corr.iloc[i, j]) > 0.8:
            print(corr.columns[i], "-", corr.columns[j], "=", round(corr.iloc[i, j],2))

sns.boxplot(y=df['Sales'])
plt.title("Sales Outliers")
plt.show()
