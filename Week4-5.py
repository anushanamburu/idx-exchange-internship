#!/usr/bin/env python
# coding: utf-8

# # Week 4-5 Deliverable

# In[1]:


import pandas as pd


# ### Read Datasets

# In[2]:


sold = pd.read_csv("soldFINAL.csv")
list = pd.read_csv("listFINAL.csv")


# In[3]:


#number of rows and coluns in sold before any changes
sold.shape


# In[4]:


#number of rows and coluns in list before any changes
list.shape


# ### Convert Date Fields to Datetime Format

# In[5]:


#converting sold dataset
sold["CloseDate"] = pd.to_datetime(sold["CloseDate"])
sold["PurchaseContractDate"] = pd.to_datetime(sold["PurchaseContractDate"])
sold["ListingContractDate"] = pd.to_datetime(sold["ListingContractDate"])
sold["ContractStatusChangeDate"] = pd.to_datetime(sold["ContractStatusChangeDate"])

#checking the data types after conversion
print(sold["CloseDate"].dtypes)
print(sold["PurchaseContractDate"].dtypes)
print(sold["ListingContractDate"].dtypes)
print(sold["ContractStatusChangeDate"].dtypes)


# In[6]:


#converting list dataset
list["CloseDate"] = pd.to_datetime(list["CloseDate"])
list["PurchaseContractDate"] = pd.to_datetime(list["PurchaseContractDate"])
list["ListingContractDate"] = pd.to_datetime(list["ListingContractDate"])
list["ContractStatusChangeDate"] = pd.to_datetime(list["ContractStatusChangeDate"])

#checking the data types after conversion
print(list["CloseDate"].dtypes)
print(list["PurchaseContractDate"].dtypes)
print(list["ListingContractDate"].dtypes)
print(list["ContractStatusChangeDate"].dtypes)


# ### Remove Unnecessary Columns

# #### Already removed unnecessary columns that had over 90% missing data in Week 2

# ### Analyze Missing Values 

# ##### Checked percentage of missing values in each column to double check if any columns needed to be dropped that had high number of missing values and dropped them accordingly if needed

# In[7]:


sold_missing = sold.isnull().mean()*100
sold_missing[sold_missing>0].sort_values(ascending=False)


# In[8]:


#dropped waterfront and basement columns because over 90% missing data
sold=sold.drop(columns=["WaterfrontYN","BasementYN"])


# In[9]:


list_missing = list.isnull().mean()*100
list_missing[list_missing>0].sort_values(ascending=False)


# ### Ensure Numeric Fields are Proper

# In[13]:


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

# In[ ]:


#flagging invalid numeric values in list
list["invalid_nums"] = (
    (list["ClosePrice"]<=0) | (list["LivingArea"]<=0) |
    (list["DaysOnMarket"]<0) | (list["BedroomsTotal"]<0) |
    (list["BathroomsTotalInteger"]<0)
)

#flagged 419 invalid numeric values in list
list["invalid_nums"].sum()


# In[ ]:


#flagging invalid numeric values in sold
sold["invalid_nums"] = (
    (sold["ClosePrice"]<=0) | (sold["LivingArea"]<=0) |
    (sold["DaysOnMarket"]<0) | (sold["BedroomsTotal"]<0) |
    (sold["BathroomsTotalInteger"]<0)
)

#flagged 202 invalid numeric values in sold
sold["invalid_nums"].sum()


# ### Data Consistency Checks

# In[16]:


#data check for sold / flag count in each column
sold["listing_after_close_flag"] = (sold["ListingContractDate"]>sold["CloseDate"])
sold["purchase_after_close_flag"] = (sold["PurchaseContractDate"]>sold["CloseDate"])
sold["negative_timeline_flag"] = (sold["PurchaseContractDate"]<sold["ListingContractDate"])
sold[["listing_after_close_flag","purchase_after_close_flag","negative_timeline_flag"]].sum()


# In[17]:


#data check for list / flag count in each column
list["listing_after_close_flag"] = (list["ListingContractDate"]>list["CloseDate"])
list["purchase_after_close_flag"] = (list["PurchaseContractDate"]>list["CloseDate"])
list["negative_timeline_flag"] = (list["PurchaseContractDate"]<list["ListingContractDate"])
list[["listing_after_close_flag","purchase_after_close_flag","negative_timeline_flag"]].sum()


# ### Geographic Data Checks

# #### Flag Missing Coordinates

# In[18]:


#flagging missing coordinates in sold
sold["missing_coord_flag"] = (sold["Latitude"].isna()|sold["Longitude"].isna())
sold["missing_coord_flag"].sum()


# In[19]:


#flagging missing coordinates in list
list["missing_coord_flag"] = (list["Latitude"].isna()|list["Longitude"].isna())
list["missing_coord_flag"].sum()


# #### Flag Latitude or Longitude is zero

# In[20]:


#flagging when latitude/longitude is zero in sold and list
sold["zero_coord_flag"] = (sold["Latitude"]==0) | (sold["Longitude"]==0)
print(sold["zero_coord_flag"].sum())

list["zero_coord_flag"] = (list["Latitude"]==0) | (list["Longitude"]==0)
print(list["zero_coord_flag"].sum())


# #### Flag Longitude > 0 errors

# In[21]:


#flagging longitude > 0 errors, since CA longitudes are always negative
sold["positive_long_flag"] = sold["Longitude"]>0
print(sold["positive_long_flag"].sum())

list["positive_long_flag"] = list["Longitude"]>0
print(list["positive_long_flag"].sum())


# #### Flag Out of State / Implausible Coordinates

# In[22]:


sold["implausible_coord_flag"] = (
    (sold["Latitude"]<32) | (sold["Latitude"]<42) | 
    (sold["Longitude"]<-125) | (sold["Longitude"]>-115)
)

print(sold["implausible_coord_flag"].sum())


# In[23]:


list["implausible_coord_flag"] = (
    (list["Latitude"]<32) | (list["Latitude"]<42) | 
    (list["Longitude"]<-125) | (list["Longitude"]>-115)
)

print(list["implausible_coord_flag"].sum())


# ### Save datasets as CSVs

# In[25]:


sold.to_csv("sold_clean_week45.csv", index=False)
list.to_csv("list_clean_week45.csv", index=False)

