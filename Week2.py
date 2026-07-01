#!/usr/bin/env python
# coding: utf-8

# # Week 2 Deliverable

# In[36]:


import pandas as pd
import matplotlib.pyplot as plt


# In[3]:


list = pd.read_csv("list_residentials.csv")
sold = pd.read_csv("sold_residentials.csv")


# ## Sold Dataset

# ### Dataset Understanding

# In[ ]:


#first five rows of sold dataset
sold.head()


# In[ ]:


#591,465 rows and 84 columns for sold
sold.shape


# In[ ]:


#all the column names in sold
sold.columns


# In[16]:


#datatypes for all the columns in sold
sold.dtypes


# In[20]:


#Identify property types in sold
sold["PropertyType"].value_counts()


# In[21]:


#Checking property type categories in sold
sold["PropertyType"].unique()


# In[22]:


#filter to just residential property types and identify the shape of the new sold dataset
sold_new = list[list["PropertyType"]=="Residential"]
sold_new.shape


# ### Missing Value Analysis

# In[23]:


#identify percentage of missing data in the columns of list
sold_missing_percent = sold_new.isnull().mean()*100
sold_missing_percent


# In[27]:


#identify columns in sold that have over 90% missing data
sold_missing_percent[sold_missing_percent>90].index


# In[28]:


#drop irrelevant columns in sold that have over 90% missing data
drop_sold_cols = ['FireplacesTotal', 'AboveGradeFinishedArea', 'TaxAnnualAmount',
       'BuilderName', 'TaxYear', 'BuildingAreaTotal',
       'ElementarySchoolDistrict', 'CoBuyerAgentFirstName',
       'BelowGradeFinishedArea', 'BusinessType', 'CoveredSpaces',
       'LotSizeDimensions', 'MiddleOrJuniorSchoolDistrict']
final_sold = sold_new.drop(columns=drop_sold_cols)
final_sold.head()


# ### Numeric Distribution Review

# In[33]:


#Percentile summaries for the following columns in sold
numeric_cols_sold = ["ClosePrice", "ListPrice", "OriginalListPrice", "LivingArea", "LotSizeAcres", "BedroomsTotal", "BathroomsTotalInteger", "DaysOnMarket", "YearBuilt"]
final_sold[numeric_cols_sold].describe(percentiles=[0.10,0.25,0.50,0.75,0.90])


# In[37]:


#Historgram numeric distribution for key numeric fields for sold
for column in numeric_cols_sold:
    final_sold[column].hist(bins=30)
    plt.title(column)
    plt.show()


# In[39]:


#Boxplot numeric distribution for key numeric fields for sold
for column in numeric_cols_sold:
    plt.boxplot(final_sold[column].dropna())
    plt.title(column)
    plt.show()


# ## Listings Dataset

# ### Dataset Understanding

# In[ ]:


#first five rows of listing dataset
list.head()


# In[ ]:


#591,465 rows and 84 columns for listings
list.shape


# In[ ]:


#all the names of the columns in listings
list.columns


# In[5]:


#datatypes for all the columns in listings
list.dtypes


# In[4]:


#identify property types in list
list["PropertyType"].value_counts()


# In[18]:


#Checking propety type categories in list
list["PropertyType"].unique()


# In[7]:


#filter to just residential property types and identify the shape of the new list dataset
list_new = list[list["PropertyType"]=="Residential"]
list_new.shape


# ### Missing Value Analysis

# In[8]:


#identify percentage of missing data in the columns of list
list_missing_percent = list_new.isnull().mean()*100
list_missing_percent


# In[26]:


#identify which columns in list are over 90% missing data
list_missing_percent[list_missing_percent>90].index


# In[15]:


#drop irrelevants columns that have over 90% missing data in list
drop_list_cols = ['FireplacesTotal', 'AboveGradeFinishedArea', 'TaxAnnualAmount',
       'BuilderName', 'TaxYear', 'BuildingAreaTotal',
       'ElementarySchoolDistrict', 'CoBuyerAgentFirstName',
       'BelowGradeFinishedArea', 'BusinessType', 'CoveredSpaces',
       'LotSizeDimensions', 'MiddleOrJuniorSchoolDistrict']
final_listings = list_new.drop(columns=drop_list_cols)
final_listings.head()


# ### Numeric Distribution

# In[42]:


#Percentile summaries for the following columns in list
numeric_cols_list = ["ClosePrice", "ListPrice", "OriginalListPrice", "LivingArea", "LotSizeAcres", "BedroomsTotal", "BathroomsTotalInteger", "DaysOnMarket", "YearBuilt"]
final_listings[numeric_cols_list].describe(percentiles=[0.10,0.25,0.50,0.75,0.90])


# In[43]:


#Historgram numeric distribution for key numeric fields for list
for column in numeric_cols_list:
    final_listings[column].hist(bins=30)
    plt.title(column)
    plt.show()


# In[44]:


#Boxplot numeric distribution for key numeric fields for listings
for column in numeric_cols_list:
    plt.boxplot(final_listings[column].dropna())
    plt.title(column)
    plt.show()


# ## Suggested Intern Questions EDA

# In[ ]:





# ## Saving updated datasets as CSV files

# In[ ]:




