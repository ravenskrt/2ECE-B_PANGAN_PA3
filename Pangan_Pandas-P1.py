#!/usr/bin/env python
# coding: utf-8

# #### Display the first and last five rows of the resulting cars

# In[3]:


import pandas as pd


# In[5]:


#load the corresponding .csv file into a data frame named cars using pandas
cars = pd.read_csv('cars.csv')
cars


# In[22]:


#display the first five rows
cars.head()


# In[9]:


#display the last five rows
cars.tail()

