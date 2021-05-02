#!/usr/bin/env python
# coding: utf-8

# In[8]:


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression

df=pd.read_csv('https://raw.githubusercontent.com/cjfghk5697/forecastsolar/main/csv%20file/ulsan_obs_data.csv')
dp=pd.read_csv('https://raw.githubusercontent.com/cjfghk5697/forecastsolar/main/csv%20file/energy.csv')


# In[9]:


df.head()


# In[10]:


dp.head()


# In[11]:


wind=df.fillna(0).loc[:,'기온(°C)']
y=dp.fillna(0).loc[:,'ulsan']

plt.plot(wind,y,'o')
plt.show()


# In[12]:



line_fitter=LinearRegression()
line_fitter.fit(wind.values.reshape(-1,1),y)
line_fitter.coef_


# In[18]:


plt.plot(wind,y,'o')
plt.plot(wind,line_fitter.predict(wind.values.reshape(-1,1)))
plt.show()

