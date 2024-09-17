#!/usr/bin/env python
# coding: utf-8

# ##EXPERIMENT 3: 
# PYTHON DATA ANALYSIS (PANDAS) 

# #PROBLEM 1

# In[38]:


#To access the pandas library
import pandas as pd

#To load the csv file
cars = pd.read_csv('cars.csv')


# Problem 1A - Load the corresponding .csv file.

# In[40]:


cars


# Problem 1B - Display the first five and last five rows of the resulting cars.

# In[42]:


cars.head()


# In[43]:


cars.tail()

