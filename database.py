#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np


# In[12]:


# 

x = pd.DataFrame ({'Brand' : ['Maruti', 'Hyundai', 'Tata', 'Mahindra', 'Maruti', 'Hyundai', 'Renault', 'Tata', 'Maruti'], 
                    'Year' : [2012, 2014, 2011, 2015, 2012,2016, 2014, 2018, 2019], 
                    'Kms Driven' : [50000, 30000, 60000,25000, 10000, 46000,31000, 15000, 12000], 
                    'City' : ['Gurgaon', 'Delhi', 'Mumbai','Delhi', 'Mumbai','Delhi','Mumbai','Chennai', 'Ghaziabad'], 
                    'Mileage' : [28, 27, 25, 26, 28,29, 24, 21, 24]})
display(x)


# In[13]:


#selecting range from rows 2 to 5
display(x.loc[2:5])


# In[15]:


#selecting cars with brand maruti and mileage >25
display(x.loc[(x.Brand=='Maruti')&(x.Mileage>25)])


# In[16]:


# selecting 0th, 2th, 4th, and 7th index rows 
display(x.iloc[[0, 2, 4, 7]]) 


# In[17]:


s = pd.Series(np.nan, index=[49,48,47,46,45, 1, 2, 3, 4, 5])


# In[18]:


s


# In[21]:


hi = pd.DataFrame({'age':[30, 2, 12, 4, 32, 33, 69],
                   'color':['blue', 'green', 'red', 'white', 'gray', 'black', 'red'],
                   'food':['Steak', 'Lamb', 'Mango', 'Apple', 'Cheese', 'Melon', 'Beans'],
                   'height':[165, 70, 120, 80, 180, 172, 150],
                   'score':[4.6, 8.3, 9.0, 3.3, 1.8, 9.5, 2.2],
                   'state':['NY', 'TX', 'FL', 'AL', 'AK', 'TX', 'TX']
                   },
           
index=['Jane', 'Nick', 'Aaron', 'Penelope', 'Dean', 'Christina', 'Cornelia'])
hi.loc['Penelope']


# In[22]:


hi.loc[['Cornelia', 'Jane', 'Dean']]


# In[23]:


hi.iloc[4]


# In[ ]:




