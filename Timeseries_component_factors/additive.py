#!/usr/bin/env python
# coding: utf-8

# In[7]:


import numpy as np

import pandas as pd

#파일 가져옴
df=pd.read_csv('https://raw.githubusercontent.com/cjfghk5697/forecastsolar/main/csv%20file/dangjin_obs_data_energy.csv')
#dangjin행만 가져옴
gen=df.fillna(0).loc[:,'dangjin']
#nan값 삭제
data1=gen.dropna(how='all')
#42개월치 가져옴 1월~2월 사이는 안가져옴
dates = pd.date_range('2018-03-01', periods=30, freq='M')
#right=data1.set_index(dates)



# In[11]:


timestamp = np.arange(len(dates))

trend_factor = timestamp*1.1

cycle_factor = 10*np.sin(np.linspace(0, 3.14*2, 30))

seasonal_factor = 7*np.sin(np.linspace(0, 3.14*8, 30))

np.random.seed(2004)

irregular_factor = 2*np.random.randn(len(dates))


# In[12]:


df = pd.DataFrame({'timeseries': trend_factor + cycle_factor + seasonal_factor + irregular_factor, 

                   'trend': trend_factor, 

                   'cycle': cycle_factor, 

                   'seasonal': seasonal_factor, 

                   'irregular': irregular_factor},

                   index=dates)




# In[13]:


df


# In[15]:


# Time series plot

import matplotlib.pyplot as plt



plt.figure(figsize=[10, 6])

df.timeseries.plot()

plt.title('Time Series (Additive Model)', fontsize=16)

plt.ylim(-12, 55)

plt.show()




# In[17]:



# -- Trend factor

#timestamp = np.arange(len(dates))

#trend_factor = timestamp*1.1



plt.figure(figsize=[10, 6])

df.trend.plot()

plt.title('Trend Factor', fontsize=16)

plt.ylim(-12, 55)

plt.show()




# In[18]:



# -- Cycle factor

#cycle_factor = 10*np.sin(np.linspace(0, 3.14*2, 48))



plt.figure(figsize=[10, 6])

df.cycle.plot()

plt.title('Cycle Factor', fontsize=16)

plt.ylim(-12, 55)

plt.show()




# In[19]:



# -- Seasonal factor

#seasonal_factor = 7*np.sin(np.linspace(0, 3.14*8, 48))



plt.figure(figsize=[10, 6])

df.seasonal.plot()

plt.title('Seasonal Factor', fontsize=16)

plt.ylim(-12, 55)

plt.show()




# In[20]:



# All in one: Time series = Trend factor + Cycle factor + Seasonal factor + Irregular factor


from pylab import rcParams

rcParams['figure.figsize'] = 12, 8

df.plot()

plt.ylim(-12, 55)

plt.show()




# In[ ]:




