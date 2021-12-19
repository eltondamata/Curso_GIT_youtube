#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df = pd.read_pickle('~/Downloads/OMR_COMPRASFILIAL.pkl')


# In[3]:


display(df)


# In[11]:


df2 = df.groupby('DESTIPCNLVNDOMR')[['VLRVNDFATLIQ']].sum()
display(df2)


# In[8]:


display(df2)


# In[ ]:




