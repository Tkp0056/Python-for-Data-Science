#!/usr/bin/env python
# coding: utf-8

# In[4]:


import requests


# In[5]:


response=requests.get('https://api.themoviedb.org/3/movie/popular?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US&page=1').json()


# In[6]:


response['results']


# In[7]:


import pandas as pd
df=pd.DataFrame()


# In[13]:


adult=[]
original_language=[]
title=[]
release_date=[]

for i in response['results']:
    adult.append(i['adult'])
    original_language.append(i['original_language'])
    title.append(i['title'])
    release_date.append(i['release_date'])
    
    d={'title':title,'release_date': release_date, 'original_language':original_language, 'adult':adult}   

df=pd.DataFrame(d)


# In[14]:


df


# In[ ]:




