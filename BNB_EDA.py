#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[4]:


bnb = pd.read_csv('/Users/pankit/Downloads/bnb_hist.csv')
bnb.head()


# In[5]:


bnb.drop('End', axis=1, inplace=True)


# In[6]:


bnb.rename(columns={'Start' : 'Date'}, inplace=True)

bnb.head()


# In[7]:


bnb.shape


# In[8]:


bnb.isnull().sum()


# In[9]:


bnb.duplicated().sum()


# Exploratory Data Analysis

# In[10]:


bnb.describe()


# In[11]:


bnb['year'] = pd.DatetimeIndex(bnb['Date']).year
bnb['month'] = pd.DatetimeIndex(bnb['Date']).month


# In[12]:


# Opening price by year

def open_price_year(bnb):
    fig, ax = plt.subplots(figsize=(10,5))
    sns.set_style('whitegrid')
    sns.barplot(x='year', y='Open', data=bnb, ci=None)
    ax.set_xlabel('Year')
    ax.set_ylabel('Price')
    ax.set_title('Opening Price by Year')
    plt.show
    
open_price_year(bnb)


# In[13]:


# Closing price by year

def close_price_year(bnb):
    fig, ax = plt.subplots(figsize=(10,5))
    sns.set_style('whitegrid')
    sns.barplot(x='year', y='Close', data=bnb, ci=None)
    ax.set_xlabel('Year')
    ax.set_ylabel('Price')
    ax.set_title('closing Price by Year')
    plt.show
    
close_price_year(bnb)


# In[14]:


# Plotting year and Volume

sns.barplot(x='year', y='Volume', data=bnb)


# In[16]:


# High and Low price over time

high_low = bnb[['Date', 'High', 'Low']]

high_low.set_index('Date').plot(figsize=(15, 5), title='High and Low Prices over time');


# In[17]:


x = high_low.index
sns.lineplot(x=x, y='High', data=high_low, label='High')


# In[19]:


sns.lineplot(x=x, y='Low', data=high_low, label='Low')


# In[20]:


# High Low prices over time

high_low.groupby('Date').mean().plot(figsize=(15, 5),
                                    title='High and Low prices over Time')
high_low.plot(figsize=(10, 5));


# In[21]:


# Repeat the same method for Open and Close Prices as well

high_low = bnb[['Date', 'Open', 'Close']]

high_low.set_index('Date').plot(figsize=(15, 5), title='Open and Close Prices over time');


# In[22]:


sns.pairplot(bnb[['High', 'Low', 'Open', 'Close', 'Volume']]);


# In[23]:


correlation = bnb.corr()
plt.figure(figsize=(10, 5))
sns.heatmap(correlation, annot=True);


# In[ ]:




