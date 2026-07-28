#!/usr/bin/env python
# coding: utf-8

# # Week 6 Deliverable

# In[1]:


import pandas as pd


# In[2]:


sold = pd.read_csv("sold_clean_week45.csv")
list = pd.read_csv("list_clean_week45.csv")


# ### Creating Key Metrics

# In[3]:


#Price Ratio metric for sold and list
sold["PriceRatio"] = sold["ClosePrice"]/sold["OriginalListPrice"]
list["PriceRatio"] = list["ClosePrice"]/list["OriginalListPrice"]


# In[4]:


#Price per square foot metric for sold and list
sold["PricePerSqFt"] = sold["ClosePrice"]/sold["LivingArea"]
list["PricePerSqFt"] = list["ClosePrice"]/list["LivingArea"]


# In[ ]:


#DaysOnMarket already exists in both datasets, so will use the original one and not make a new engineered metric


# In[5]:


#Year, Month, YrMo metrics for sold and list
sold["CloseDate"] = pd.to_datetime(sold["CloseDate"], errors="coerce")
sold["Year"] = sold["CloseDate"].dt.year
sold["Month"] = sold["CloseDate"].dt.month
sold["YrMo"] = sold["CloseDate"].dt.to_period("M").astype(str)


list["CloseDate"] = pd.to_datetime(list["CloseDate"], errors="coerce")
list["Year"] = list["CloseDate"].dt.year
list["Month"] = list["CloseDate"].dt.month
list["YrMo"] = list["CloseDate"].dt.to_period("M").astype(str)


# In[6]:


#Close to Original list ratio metric for sold and list
sold["ClosetoOGList"] = sold["ClosePrice"]/sold["OriginalListPrice"]
list["ClosetoOGList"] = list["ClosePrice"]/list["OriginalListPrice"]


# In[7]:


#Listing to Contract Days metric for sold and list
sold["PurchaseContractDate"] = pd.to_datetime(sold["PurchaseContractDate"], errors="coerce")
sold["ListingContractDate"] = pd.to_datetime(sold["ListingContractDate"], errors="coerce")

sold["ListingtoContract"] = (sold["PurchaseContractDate"] - sold["ListingContractDate"]).dt.days


list["PurchaseContractDate"] = pd.to_datetime(list["PurchaseContractDate"], errors="coerce")
list["ListingContractDate"] = pd.to_datetime(list["ListingContractDate"], errors="coerce")

list["ListingtoContract"] = (list["PurchaseContractDate"] - list["ListingContractDate"]).dt.days


# In[8]:


#Contract to Close Days metric for sold and list
sold["ContractCloseDays"] = (sold["CloseDate"]-sold["PurchaseContractDate"]).dt.days
list["ContractCloseDays"] = (list["CloseDate"]-list["PurchaseContractDate"]).dt.days


# In[9]:


#Sample Output Table with the New Columns in sold
sold.head()


# In[10]:


#Sample Output Table with the New Columns in list
list.head()


# ### Segmented Analysis

# In[11]:


#Property types segment analysis
property = sold.groupby(["PropertyType","PropertySubType"])[[
    "PriceRatio","PricePerSqFt","DaysOnMarket","Year","Month",
    "YrMo","ClosetoOGList","ListingtoContract","ContractCloseDays"
]].describe()

property


# In[12]:


#Area types segment analysis
area = sold.groupby(["CountyOrParish","MLSAreaMajor"])[[
    "PriceRatio","PricePerSqFt","DaysOnMarket","Year","Month",
    "YrMo","ClosetoOGList","ListingtoContract","ContractCloseDays"
]].describe()

area


# In[13]:


#office types segment analysis
office = sold.groupby(["ListOfficeName","BuyerOfficeName"])[[
    "PriceRatio","PricePerSqFt","DaysOnMarket","Year","Month",
    "ClosetoOGList","ListingtoContract","ContractCloseDays"
]].mean()

office


# ### Adding School Districts

# In[ ]:


import geopandas as gpd
from shapely.geometry import Point

school_dists = gpd.read_file("DistrictAreas2425.zip")
print(school_dists.columns)


# In[34]:


sold_geographic = gpd.GeoDataFrame(sold,geometry=gpd.points_from_xy(sold.Longitude,sold.Latitude),crs="EPSG:4326")
sold_geographic = gpd.sjoin(sold_geographic,school_dists[["DistrictNa","geometry"]],how="left",predicate="within")

list_geographic = gpd.GeoDataFrame(list,geometry=gpd.points_from_xy(list.Longitude,list.Latitude),crs="EPSG:4326")
list_geographic = gpd.sjoin(list_geographic,school_dists[["DistrictNa","geometry"]],how="left",predicate="within")


# In[32]:


sold_geographic


# In[35]:


list_geographic


# ### Saving Datasets as CSVs

# In[36]:


sold_geographic.to_csv("soldFINALFINAL.csv", index=False)
list_geographic.to_csv("listFINALFINAL.csv", index=False)

