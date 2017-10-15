import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn

df = pd.read_csv('data michigan.csv',sep=';')
df['month_year'] = df['Day'].apply(lambda date: date[3:])

AnnArbor = df[df['City'] == 'Ann Arbor'].groupby('month_year').aggregate({'High':np.mean})
Lansing = df[df['City'] == 'Lansing'].groupby('month_year').aggregate({'High':np.mean})

plt.figure()
plt.plot_date(x=AnnArbor.index, y=AnnArbor.High, fmt="r-", label= 'Ann Arbor')
plt.plot_date(x=Lansing.index, y=Lansing.High, fmt="b-", label= 'Lasing')
plt.title("Monthly average of maximum temperatures (2017)")
plt.ylabel("Average temperatures (°F)")
plt.xlabel("Month")
plt.xticks(rotation=45)
plt.ylim([0,90])
plt.grid(True)
plt.legend()
plt.show()

