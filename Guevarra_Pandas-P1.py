#!/usr/bin/env python
# coding: utf-8

# ##EXPERIMENT 3: 
# PYTHON DATA ANALYSIS (PANDAS) 

# #PROBLEM 1

# In[21]:


import pandas as pd

cars = pd.read_csv('cars.csv')


# Problem 1A - Load the corresponding .csv file.

# In[22]:


cars


# Problem 1B - Display the first five and last five rows of the resulting cars.

# In[23]:


cars.head()


# In[24]:


cars.tail()

