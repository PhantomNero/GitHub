import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('GoogleApps.csv')
d = df.pivot_table(index='Content Rating', columns='Type',
                   values='Installs', aggfunc='mean')

# subplots - постройка графиков друг под другом
d.plot(kind='barh', subplots=True)
plt.show()

# совмещение графиков:
d.plot(kind='barh', grid=True)
plt.show()

# layout 2,1 - по умолчанию друг на другом - два в одну линию:
d.plot(kind='barh', subplots=True, layout=(2, 1))
plt.show()

# layout 1,2 - в две линии по одному:
d.plot(kind='barh', subplots=True, layout=(1, 2))
plt.show()