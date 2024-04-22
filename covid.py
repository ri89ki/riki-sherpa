import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("all_weekly_excess_deaths.csv")
df.head()
print(df['country'].unique())
df1 = df.loc[(df['country']=='Canada') & (df['year']==2020)]

df1.head()
plt.plot(df1['week'],df1['total_deaths'])
plt.xlabel('week')
plt.ylabel('total_deaths')
plt.title('line chart')
plt.show()
plt.scatter(df1['week'],df1['total_deaths'],df1['covid_deaths'])
plt.xlabel('week')
plt.ylabel('total_deaths')
plt.title('scatter chart')
plt.show()
plt.hist(df['total_deaths'],bins=20)
plt.xlabel('total_deaths')
plt.title('histogram')
plt.xticks([0,20000,40000,60000,80000],['0','20k','40k','60k','80k'])
plt.show()
