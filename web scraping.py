#!/usr/bin/env python
# coding: utf-8

# In[140]:


get_ipython().system('pip install autoscraper')


# In[141]:


from autoscraper import AutoScraper


# In[172]:


url = "https://www.amazon.com/s?k=iphone"

list_items = ["$589.00"]


# In[173]:


scrape = AutoScraper()
result = scrape.build(url,list_items)
print(result)


# In[174]:


scrape.get_result_similar(url,grouped=True)


# In[177]:


import pandas as pd


# In[180]:


df = pd.DataFrame(result)
df.head(20)


# In[ ]:




