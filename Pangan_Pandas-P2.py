#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[5]:


#load the corresponding .csv file into a data frame named cars using pandas
cars = pd.read_csv('cars.csv')
cars


# #### A.)

# In[21]:


#display the first five rows with odd-numbered columns (columns 1, 3, 5, 7...) of cars
cars.iloc[1::2].head()


# #### B.) 

# In[85]:


#display the row that contains the 'Model' of 'Mazda RX4'
cars.loc[[0],['Model']]


# #### C.)

# In[80]:


#display how many cylinders ('cyl) does the car model 'Camaro Z28' have
cars.loc[[23],['Model','cyl']]


# #### D.) 

# In[83]:


#display how many cylinders (‘cyl’) and what gear type (‘gear’) do the car models ‘Mazda RX4 Wag’, ‘Ford Pantera L’ and ‘Honda Civic’ have
cars.loc[[1,28,18],['Model','cyl','gear']]


# In[ ]:




