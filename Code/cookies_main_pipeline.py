#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


# reading the data
cookies = pd.read_csv("../Data/cookies.csv")


# In[3]:


# drop unnecessary columns or rows with NAs
from cleaning_data import dropping_rows_and_columns


cookies = dropping_rows_and_columns(cookies)


# In[4]:


# defining X and y
X = cookies.drop(columns="quality")
y = cookies["quality"]


# In[5]:


# splitting the data

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=8)

# training datasets to DataFrame again to manipulate them
X_train = pd.DataFrame(X_train, columns=X.columns)
X_test = pd.DataFrame(X_test, columns=X.columns)


# In[6]:


# imputing the numeric nulls
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import FunctionTransformer
from fill_num_nulls import fill_num_na
num_cols = X_train.select_dtypes(include=["int64", "float64"]).columns

numeric_nulls_imputer = FunctionTransformer(fill_num_na)


# In[7]:


from mixin_imputer import mixin_fixer

mixin_encoder = FunctionTransformer(mixin_fixer)


# In[8]:


# creating the category encoding pipeline

from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
cat_cols = ["butter type", "mixins"]
categ_encode_pipeline = ColumnTransformer([
    ("oneH_encoder_branch", OneHotEncoder(handle_unknown="ignore"), ["butter type"]),
    ("manual_encoder_branch", mixin_encoder, ["mixins"])
])


# In[9]:


from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.tree import DecisionTreeRegressor
from sklearn.feature_selection import SelectKBest, SelectFromModel, RFE


# In[10]:


imputer_encoder_pipeline = ColumnTransformer([
    ("num_imputer", numeric_nulls_imputer, num_cols),
    ("cat_full_pipe", categ_encode_pipeline, cat_cols)
])


# In[12]:



full_pipeline = Pipeline([
    ("impute_pipeline", imputer_encoder_pipeline),
    ("std_scaler", StandardScaler())
])


# In[13]:


# In[ ]:




