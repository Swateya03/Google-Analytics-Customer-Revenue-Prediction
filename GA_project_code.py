#!/usr/bin/env python
# coding: utf-8

# In[1]:


## Necessary libraries
import time
import json
import numpy as np
import pandas as pd
from pandas import json_normalize

import datetime

import seaborn as sns
import matplotlib.pyplot as plt

import lightgbm as lgb

from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import mean_squared_error

import warnings
warnings.filterwarnings('ignore')


# ## DATA LOADING
# #### Since in the dataset thier are some json columns so we need to define a function to load them as given below

# In[2]:



def load_df(csv_path, nrows = None):
    json_cols = ['device', 'geoNetwork', 'totals', 'trafficSource']
    df = pd.read_csv(csv_path,
                     #converters are dict of functions for converting values in certain columns. Keys can either be integers or column labels.
                     #json.loads() method can be used to parse a valid JSON string and convert it into a Python Dictionary.
                     #It is mainly used for deserializing native string, byte, or byte array which consists of JSON data into Python Dictionary.
                     converters = {col: json.loads for col in json_cols},                                                                         
                         dtype = {'fullVisitorId': 'str'}, # Important!!
                         nrows = nrows)
    for col in json_cols:
        # for each column, flatten data frame such that the values of a single col are spread in different cols
        # This will use subcol as names of flat_col.columns
        flat_col = json_normalize(df[col])
        # Name the columns in this flatten data frame as col.subcol for tracability
        flat_col.columns = [f"{col}.{subcol}" for subcol in flat_col.columns]
        # Drop the json_col and instead add the new flat_col
        df = df.drop(col, axis = 1).merge(flat_col, right_index = True, left_index = True)
    return df


# In[3]:


csv_train_path = 'train_v2.csv'
csv_test_path = 'test_v2.csv'


# In[4]:


get_ipython().run_cell_magic('time', '', '# %%time is used to calculate the timing of code chunk execution #\ntrain = load_df(csv_train_path, nrows = 120000)\ntest = load_df(csv_test_path, nrows = None)\ntrain.shape, test.shape')


# #### Since we are implementing this using cpu so we have taken 120000 rows while the real shape is as follows:-
# #### Train dataset shape is : (1708337, 60)
# #### Test dataset shape is : (401589, 59)
# #### Here each record corresponds to one visit to store.

# ## DESCRIBING DATA

# In[5]:


train.info()


# In[6]:


train.loc[:2]


# #### We can observe from above that many columns has a huge amount of null values so we have the following options to clean the data :
# #### 1. Get rid of the corresponding rows
# #### 2. Get rid of the whole column
# #### 3. Set the values to some values such as zero,mean,median etc.
# ## DATA PREPROCESSING
# #### NOTE - For further data cleaning we need to get rid of values such as 'unknown.unknown', '(not set)', 'not available in demo dataset', '(not provided)', '(none)', 'NA' in the training dataset so that data cleaning and preproccessing can be done effiently

# In[7]:


unknown_values = ['unknown.unknown', '(not set)', 'not available in demo dataset', '(not provided)', '(none)', '<NA>']


# In[8]:


train.replace(unknown_values, np.nan, inplace=True)


# In[9]:


train.loc[:2]


# #### It can be observed that all the values which were null basically have been replaced to NAN
# #### We also need to drop such columns who has only one unique value ,basically it means if any column has all values same then it is a redundant feature

# In[10]:


unique_value_counts = train.nunique()
unique_value_counts


# In[11]:


columns_to_drop = unique_value_counts[unique_value_counts == 1].index
train.drop(columns=columns_to_drop, inplace=True)


# In[12]:


train.shape


# #### It can be oberved that after dropping the columns with one unique values ,the shape regarding columns has been reduced from 60 -> 53

# In[14]:


# Converting date column from character to Date class.
train['date'] = pd.to_datetime(train['date'], format='%Y%m%d')


# In[15]:


train['date']


# In[21]:


# Converting all the newly JSON columns (hits, pageviews, transactionRevenue) from character to numeric
columns_to_convert = ['totals.hits', 'totals.pageviews', 'totals.transactionRevenue']
for column in columns_to_convert:
    train[column] = pd.to_numeric(train[column], errors='coerce')
# The 'errors' parameter is set to 'coerce' to replace any non-convertible values with NaN.
# If you want to keep the non-convertible values as they are, you can omit the 'errors' parameter.


# In[24]:


# Calculate the percentage of missing values for each column
missing_percentage = (train.isnull().sum() / len(train)) * 100

# Define a threshold for missing values (95% in this case)
threshold = 95

# Get the list of columns to drop based on the threshold
columns_to_drop = missing_percentage[missing_percentage > threshold].index

columns_to_drop


# In[26]:


# Drop the columns with more than 95% missing values
train.drop(columns=columns_to_drop, inplace=True)


# In[27]:


train.shape


# In[30]:


from sklearn.impute import SimpleImputer

# Identify numeric columns with missing values
numeric_columns_with_missing = train.select_dtypes(include=['number']).columns[train.select_dtypes(include=['number']).isnull().any()]

# Create a SimpleImputer with a strategy (e.g., 'mean', 'median', or 'most_frequent')
imputer = SimpleImputer(strategy='median')  # You can choose a different strategy if needed

# Impute missing values in numeric columns only
train[numeric_columns_with_missing] = imputer.fit_transform(train[numeric_columns_with_missing])


# In[31]:


numeric_columns_with_missing


# In[35]:


missing_pageviews = train['totals.pageviews'].isnull().sum()
missing_pageviews


# In[ ]:




