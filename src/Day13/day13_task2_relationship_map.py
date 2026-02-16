import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    'SquareFootage': [1200, 1500, 1800, 2200, 2600, 3000, 1100, 2900],
    'Price': [200000, 250000, 280000, 350000, 400000, 450000, 190000, 440000],
    'Neighborhood': ['Rural', 'Suburb', 'Suburb', 'Downtown', 
                     'Downtown', 'Downtown', 'Rural', 'Suburb']
}
df = pd.DataFrame(data)

sns.scatterplot(x='SquareFootage', y='Price', data=df)
plt.title('Scatter Plot: SqFt vs Price')
plt.show()

sns.boxplot(x='Neighborhood', y='Price', data=df)
plt.title('Boxplot: Neighborhood vs Price')
plt.show()