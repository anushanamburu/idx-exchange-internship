#!/usr/bin/env python
# coding: utf-8

# # Week 4-5 Deliverable

# In[1]:


import pandas as pd


# ### Read Datasets

# In[2]:


sold = pd.read_csv("soldFINAL.csv")
list = pd.read_csv("listFINAL.csv")


# ### Convert Date Fields to Datetime Format

# In[3]:


#converting sold dataset
sold["CloseDate"] = pd.to_datetime(sold["CloseDate"])
sold["PurchaseContractDate"] = pd.to_datetime(sold["PurchaseContractDate"])
sold["ListingContractDate"] = pd.to_datetime(sold["ListingContractDate"])
sold["ContractStatusChangeDate"] = pd.to_datetime(sold["ContractStatusChangeDate"])


# In[4]:


#converting list dataset
list["CloseDate"] = pd.to_datetime(list["CloseDate"])
list["PurchaseContractDate"] = pd.to_datetime(list["PurchaseContractDate"])
list["ListingContractDate"] = pd.to_datetime(list["ListingContractDate"])
list["ContractStatusChangeDate"] = pd.to_datetime(list["ContractStatusChangeDate"])


# ### Remove Unnecessary Columns

# ### Already removed unnecessary columns that had over 90% missing data in Week 2

# ### Analyze Missing Values 

# # checked percentage of missing values in each column to double check if any columns needed to be dropped that had high number of missing values and dropped them accordingly if needed

# In[21]:


sold_missing = sold.isnull().mean()*100
sold_missing[sold_missing>0].sort_values(ascending=False)


# In[ ]:


#dropped waterfront and basement columns because over 90% missing data
sold=sold.drop(columns=["WaterfrontYN","BasementYN"])


# In[22]:


list_missing = list.isnull().mean()*100
list_missing[list_missing>0].sort_values(ascending=False)


# ### Ensure Numeric Fields are Proper

# In[ ]:


#converting all column names into numeric if needed
numeric_cols = ["ClosePrice","ListPrice","OriginalListPrice",
                "LivingArea","LotSizeAcres","BedroomsTotal",
                "BathroomsTotalInteger","DaysOnMarket"]
for col in numeric_cols:
    if col in list.columns:
        list[col]=pd.to_numeric(list[col],errors="coerce")
    if col in sold.columns:
        sold[col]=pd.to_numeric(sold[col],errors="coerce")


# ### Removing or Flagging Invalid Numeric Values

# In[46]:


#flagging invalid numeric values in list
list["invalid_nums"] = (
    (list["ClosePrice"]<=0) | (list["LivingArea"]<=0) |
    (list["DaysOnMarket"]<0) | (list["BedroomsTotal"]<0) |
    (list["BathroomsTotalInteger"]<0)
)

#no invalid numeric values in list
list["invalid_nums"].sum()


# In[ ]:


#flagging invalid numeric values in sold
sold["invalid_nums"] = (
    (sold["ClosePrice"]<=0) | (sold["LivingArea"]<=0) |
    (sold["DaysOnMarket"]<0) | (sold["BedroomsTotal"]<0) |
    (sold["BathroomsTotalInteger"]<0)
)

#no invalid numeric values in sold
sold["invalid_nums"].sum()


# ### Data Consistency Checks

# In[ ]:





# ### Geographic Data Checks

# In[ ]:




