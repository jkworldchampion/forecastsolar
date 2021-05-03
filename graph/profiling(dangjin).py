#!/usr/bin/env python
# coding: utf-8

# In[8]:


import pandas_profiling as pp
import pandas as pd

energy= pd.read_csv('https://raw.githubusercontent.com/cjfghk5697/forecastsolar/main/csv%20file/dangjin_obs_data_energy.csv')
pp.ProfileReport(energy)


# In[ ]:




