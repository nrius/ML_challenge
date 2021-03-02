#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from sklearn.impute import SimpleImputer


# In[ ]:


def fill_num_na(df):
    imputer = SimpleImputer(strategy="median")
    X = imputer.fit_transform(df)
    return X

