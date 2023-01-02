#!/usr/bin/env python
# coding: utf-8

# # Steps to Download and Install Python:
#     1.Download python from https://www.python.org/downloads/
#         you need to choose the appropriate version and type of system
#     2.Install downloaded python according to Operating System
#     3.Set path variable in system
#     4.use python filename.py to run python file
#     

# Download python on VSCode
#     Just go to extension see microsofts Python blue ticked icon and add to your IDE and you are good to go

# Download anaconda and it will automatically download and instal python for us

# # Download Dataset
#     1.If we want to  download proper dataset we can use platform named Kaggle 
#     2.First go to https://www.kaggle.com/
#     3.Open accound using email
#     4.In search bar search for the dataset you want and Download it in the same directory in which your python file is to avoid giving path of files

# # Data Cleaning
#     1.Cleaning of data contains understanding null values and removing or adjusting it
#     2.convert datatypes
#     3.Integrate data

# # Example

# In[1]:


# Download python and check downloaded or not
get_ipython().system('python --version')


# In[3]:


#Download dataset and import it in python using pandas package
# Download dataset using https://www.kaggle.com/datasets/ilayaraja07/data-cleaning-feature-imputation?select=Wine_Quality.csv
#!pip install pandas  ##If pandas if not installed
import pandas as pd #importing the library
#reading the file in dataframe
df=pd.read_csv("C:/Users/Hp/Desktop/Practicles/ML/Wine_Quality.csv")


# In[4]:


#check tables and first five rows in dataset
df.head()


# In[5]:


df.isnull().sum()


# Some of the columns are containing the null values so as values are very small so just delete those rows using drop() function

# In[6]:


df.dropna(inplace=True)


# In[7]:


df.isnull().sum()


# In[8]:


df.describe()


# In[9]:


# so now our data is properly cleaned


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




