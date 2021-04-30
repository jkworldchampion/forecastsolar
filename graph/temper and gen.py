import matplotlib.pyplot as plt
import pandas as pd

df=pd.read_csv('https://raw.githubusercontent.com/cjfghk5697/forecastsolar/main/csv%20file/dangjin_obs_data.csv')
dp=pd.read_csv('https://raw.githubusercontent.com/cjfghk5697/forecastsolar/main/csv%20file/energy2.csv')

df.head()
dp.head()

temper=df.loc[:,'기온(°C)']
y=dp.loc[:,'dangjin']

plt.plot(temper,y)
plt.xlabel('energy')
plt.ylabel('temper')
plt.show()
plt.scatter(temper,y)





