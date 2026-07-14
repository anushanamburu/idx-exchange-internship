#!/usr/bin/env python
# coding: utf-8

# # Week 3 Deliverable

# In[2]:


import pandas as pd


# In[3]:


sold = pd.read_csv("ResidentialSoldFINAL.csv")
list = pd.read_csv("ResidentialListingsFINAL.csv")


# ### Fetching Mortgage FRED Dataset

# In[4]:


url = "https://fred.stlouisfed.org/graph/fredgraph.csv?id=MORTGAGE30US"
mortgage = pd.read_csv(url, parse_dates=['observation_date'])
mortgage.columns = ['date', 'rate_30yr_fixed']
mortgage


# ### Resample Weekly Rates to Monthly Averages

# In[5]:


mortgage['year_month'] = mortgage['date'].dt.to_period('M')
mortgage_monthly = mortgage.groupby('year_month')['rate_30yr_fixed'].mean().reset_index()
mortgage_monthly


# ### Creating Matching ket on MLS Datasets

# In[6]:


# Sold dataset — key off CloseDate
sold['year_month'] = pd.to_datetime(sold['CloseDate']).dt.to_period('M')
sold['year_month']


# In[7]:


# Listings dataset — key off ListingContractDate
list['year_month'] = pd.to_datetime(list['ListingContractDate']).dt.to_period('M')
list['year_month']


# ### Merge

# In[8]:


sold_with_rates = sold.merge(mortgage_monthly, on='year_month', how='left')
sold_with_rates


# In[9]:


listings_with_rates = list.merge(mortgage_monthly, on='year_month', how='left')
listings_with_rates


# ### Validate Merge

# In[10]:


print(sold_with_rates['rate_30yr_fixed'].isnull().sum())
print(listings_with_rates['rate_30yr_fixed'].isnull().sum())


# In[11]:


print(
    sold_with_rates[
        ['CloseDate', 'year_month', 'ClosePrice', 'rate_30yr_fixed']
    ].head()
)

sold_with_rates.to_csv("soldFINAL.csv", index=False)
listings_with_rates.to_csv("listFINAL.csv", index=False)