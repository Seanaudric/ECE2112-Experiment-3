#!/usr/bin/env python
# coding: utf-8

# ##EXPERIMENT 3: PYTHON DATA ANALYSIS (PANDAS)

# #PROBLEM 2

# In[24]:


#To access the pandas library
import pandas as pd

#To load the csv file
cars = pd.read_csv('cars.csv')


# Problem 2A - Display the first five rows with odd-numbered columns of cars.

# In[26]:


oddnumcars = cars.iloc[[1,3,5,7,9],: ]
oddnumcars


# Problem 2B - Display the row that contains the ‘Model’ of ‘Mazda RX4’.

# In[28]:


cars.loc[cars['Model'] == 'Mazda RX4']


# Problem 2C - Determine how many cylinders (‘cyl’) the car model ‘Camaro Z28’ have.

# In[30]:


cars.loc[cars['Model'] == 'Camaro Z28',['cyl']]


# Problem 2D - DDetermine how many cylinders (‘cyl’) and what gear type (‘gear’o the car models ‘Mazda RX4 
# Wag’, ‘Ford Pantera L’ and ‘Honda Civic’ have. 

# In[32]:


cars.loc[[1,18,28],['cyl','gear']]

