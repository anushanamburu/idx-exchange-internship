#!/usr/bin/env python
# coding: utf-8

# # Week 7 Deliverable

# In[1]:


import pandas as pd


# In[2]:


sold = pd.read_csv("soldFINALFINAL.csv")
list = pd.read_csv("listFINALFINAL.csv")


# ### IQR Method

# In[3]:


#checking size of sold dataset
sold.shape


# In[4]:


#falgging and counting total outliers in ClosePrice
close_price_Q1 = sold["ClosePrice"].quantile(0.25)
close_price_Q3 = sold["ClosePrice"].quantile(0.75)
close_price_IQR = close_price_Q3 - close_price_Q1

close_price_lower = close_price_Q1-1.5*close_price_IQR
close_price_upper = close_price_Q1+1.5*close_price_IQR

sold["ClosePriceOutliers"] = (sold["ClosePrice"]<close_price_lower) | (sold["ClosePrice"]>close_price_upper)
sold["ClosePriceOutliers"].sum()


# In[5]:


#flagging and counting total outliers in LivingArea
living_area_Q1 = sold["LivingArea"].quantile(0.25)
living_area_Q3 = sold["LivingArea"].quantile(0.75)
living_area_IQR = living_area_Q3 - living_area_Q1

living_area_lower = living_area_Q1-1.5*living_area_IQR
living_area_upper = living_area_Q1+1.5*living_area_IQR

sold["LivingAreaOutliers"] = (sold["LivingArea"]<living_area_lower) | (sold["LivingArea"]>living_area_upper)
sold["LivingAreaOutliers"].sum()


# In[6]:


#flagging and counting total outliers in DaysOnMarket
days_Q1 = sold["DaysOnMarket"].quantile(0.25)
days_Q3 = sold["DaysOnMarket"].quantile(0.75)
days_IQR = days_Q3 - days_Q1

days_lower = days_Q1-1.5*days_IQR
days_upper = days_Q1+1.5*days_IQR

sold["DaysOnMarketOutliers"] = (sold["DaysOnMarket"]<days_lower) | (sold["DaysOnMarket"]>days_upper)
sold["DaysOnMarketOutliers"].sum()


# In[9]:


#filtered dataset without the outliers
sold_filtered = sold[
    (~sold["ClosePriceOutliers"]) &
    (~sold["LivingAreaOutliers"]) &
    (~sold["DaysOnMarketOutliers"])
]


# In[ ]:


#comparing sizes of the datasets, original dataset and the filtered dataset without outliers
print(sold.shape)
print(sold_filtered.shape)


# In[13]:


#comparing close price before and after filtering
print("Median Close Price before:", sold["ClosePrice"].median())
print("Median Close Price after:",sold_filtered["ClosePrice"].median())


# In[14]:


#comparing living area before and after filtering
print("Median living area before:", sold["LivingArea"].median())
print("Median living area after:",sold_filtered["LivingArea"].median())


# In[15]:


#comparing days on market before and after filtering
print("Median days on market before:", sold["DaysOnMarket"].median())
print("Median days on market after:",sold_filtered["DaysOnMarket"].median())


# ### Written Comparison of the Datasets after Analysus

# ###### The original sold dataset had 423,856 rows, which are the recorded properties. After the IQR method analysis, the filtered and new sold dataset has 279,383 properties, which is a substantial decrease. Looking more closely at the attributes or factors, such as Close Price, Living Area, and Days on Market, there has also been a large change in the number of properties before and after the IQR method analysis as shown above. The median Close Price went from $875,000 to $860,000, the median Living Area went from 1,850 to 1,825 square feet, and the media Days on Market went from 27 to 25 days. Overall, removing or flagging outliers is crucial in the data analysis and cleaning process because it ensures that the data is accurate as possible, without letting rare outliers skew or mislead the housing market information. 

# ### Saving datasets as CSVs

# In[16]:


sold.to_csv("sold_flagged_OG.csv", index=False)
sold_filtered.to_csv("sold_filtered.csv", index=False)

