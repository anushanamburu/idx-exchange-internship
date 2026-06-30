#!/usr/bin/env python
# coding: utf-8

# # Week 1 Deliverable
# 
# ##### Read all the Listing files from 2024, 2025, and 2026. First, combined all the Listing files by year and then combined all of the list year files all into one large csv file for Listing data.

# In[1]:


import pandas as pd


# In[2]:


list1 = pd.read_csv("CRMLSListing202401.csv")
list2 = pd.read_csv("CRMLSListing202402.csv")
list3 = pd.read_csv("CRMLSListing202403.csv")
list4 = pd.read_csv("CRMLSListing202404.csv")
list5 = pd.read_csv("CRMLSListing202405.csv")
list6 = pd.read_csv("CRMLSListing202406.csv")
list7 = pd.read_csv("CRMLSListing202407.csv")
list8 = pd.read_csv("CRMLSListing202408.csv")
list9 = pd.read_csv("CRMLSListing202409.csv")
list10 = pd.read_csv("CRMLSListing202410.csv")
list11 = pd.read_csv("CRMLSListing202411.csv")
list12 = pd.read_csv("CRMLSListing202412.csv")

list2024 = pd.concat([list1,list2,list3,list4,list5,list6,list7,list8,list9,list10,list11,list12])

#383,920 listings for 2024 year
len(list2024) 


# In[3]:


list1x = pd.read_csv("CRMLSListing202501.csv")
list2x = pd.read_csv("CRMLSListing202502.csv")
list3x = pd.read_csv("CRMLSListing202503.csv")
list4x = pd.read_csv("CRMLSListing202504.csv")
list5x = pd.read_csv("CRMLSListing202505.csv")
list6x = pd.read_csv("CRMLSListing202506.csv")
list7x = pd.read_csv("CRMLSListing202507.csv")
list8x = pd.read_csv("CRMLSListing202508.csv")
list9x = pd.read_csv("CRMLSListing202509.csv")
list10x = pd.read_csv("CRMLSListing202510.csv")
list11x = pd.read_csv("CRMLSListing202511.csv")
list12x = pd.read_csv("CRMLSListing202512.csv")

list2025 = pd.concat([list1x,list2x,list3x,list4x,list5x,list6x,list7x,list8x,list9x,list10x,list11x,list12x])

#363,315 listings for 2025 year
len(list2025)


# In[ ]:


list1y = pd.read_csv("CRMLSListing202601.csv")
list2y = pd.read_csv("CRMLSListing202602.csv")
list3y = pd.read_csv("CRMLSListing202603.csv")
list4y = pd.read_csv("CRMLSListing202604.csv")
list5y = pd.read_csv("CRMLSListing202605.csv")

list2026 = pd.concat([list1y,list2y,list3y,list4y,list5y])

#182,333 listings for 2026 year
len(list2026)


# In[ ]:


list = pd.concat([list2024,list2025,list2026])
print(list)

#total of 929,568 listings for years 2024, 2025, and 2026
len(list)


# In[ ]:


list_residentials = list[list["PropertyType"] == "Residential"]
list_residentials

#total of 591,465 listings that were residential for years 2024, 2025, and 2026


# ##### Read all of the Sold files from 2024, 2025, and 2026. Removed the last two columns in the files named "filled." After cleaning this part of the data, performed the same code as the Listing data to combine all the datasets into one large csv file for Sold data.

# In[7]:


sold1 = pd.read_csv("CRMLSSold202401.csv")
sold2 = pd.read_csv("CRMLSSold202402.csv")
sold3 = pd.read_csv("CRMLSSold202403.csv")
sold4 = pd.read_csv("CRMLSSold202404.csv")

sold5 = pd.read_csv("CRMLSSold202405_filled.csv")
sold5_new = sold5.drop(columns=sold5.columns[-2:])

sold6 = pd.read_csv("CRMLSSold202406_filled.csv")
sold6_new = sold6.drop(columns=sold6.columns[-2:])

sold7 = pd.read_csv("CRMLSSold202407_filled.csv")
sold7_new = sold1.drop(columns=sold1.columns[-2:])

sold8 = pd.read_csv("CRMLSSold202408.csv")
sold9 = pd.read_csv("CRMLSSold202409.csv")
sold10 = pd.read_csv("CRMLSSold202410.csv")
sold11 = pd.read_csv("CRMLSSold202411.csv")
sold12 = pd.read_csv("CRMLSSold202412.csv")

sold2024 = pd.concat([sold1,sold2,sold3,sold4,sold5_new,sold6_new,sold7_new,sold8,sold9,sold10,sold11,sold12])

#264,227 sold in 2024 year
len(sold2024)


# In[8]:


sold1x = pd.read_csv("CRMLSSold202501_filled.csv")
sold1_newx = sold1x.drop(columns=sold1x.columns[-2:])

sold2x = pd.read_csv("CRMLSSold202502.csv")
sold3x = pd.read_csv("CRMLSSold202503.csv")
sold4x = pd.read_csv("CRMLSSold202504.csv")
sold5x = pd.read_csv("CRMLSSold202505.csv")
sold6x = pd.read_csv("CRMLSSold202506.csv")
sold7x = pd.read_csv("CRMLSSold202507.csv")
sold8x = pd.read_csv("CRMLSSold202508.csv")
sold9x = pd.read_csv("CRMLSSold202509.csv")
sold10x = pd.read_csv("CRMLSSold202510.csv")
sold11x = pd.read_csv("CRMLSSold202511.csv")
sold12x = pd.read_csv("CRMLSSold202512.csv")

sold2025 = pd.concat([sold1_newx,sold2x,sold3x,sold4x,sold5x,sold6x,sold7x,sold8x,sold9x,sold10x,sold11x,sold12x])

#260,104 sold in 2025 year
len(sold2025)


# In[ ]:


sold1y = pd.read_csv("CRMLSSold202601.csv")
sold2y = pd.read_csv("CRMLSSold202602.csv")
sold3y = pd.read_csv("CRMLSSold202603.csv")
sold4y = pd.read_csv("CRMLSSold202604.csv")
sold5y = pd.read_csv("CRMLSSold202605.csv")

sold2026 = pd.concat([sold1y,sold2y,sold3y,sold4y,sold5y])

#107,344 sold in 2026 year
len(sold2026)


# In[ ]:


sold = pd.concat([sold2024,sold2025,sold2026])
print(sold)

#total 631,675 sold in the years 2024, 2025, and 2026
len(sold)


# In[ ]:


sold_residentials = list[list["PropertyType"] == "Residential"]
sold_residentials

#total of 591,465 sold that were residential for years 2024, 2025, and 2026


# ### Saving combined listings and sold residential properties as CSV files

# In[12]:


#Turned into CSV files for new listing and sold datasets
list_residentials.to_csv("list_residentials.csv", index=False)
sold_residentials.to_csv("sold_residentials.csv", index=False)

