import pandas as pd
import matplotlib.pyplot as plt

pop_data = pd.read_csv('countries of the world.csv', index_col=0)
pop_data.plot(kind='barh', figsize=(100, 300))

plt.title('Population of All Countries')
plt.xlabel('Population')
plt.ylabel('Country')

plt.show()