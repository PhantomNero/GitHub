import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('2.csv')

df['funding_total_usd'].plot(kind='bar')
plt.show()


