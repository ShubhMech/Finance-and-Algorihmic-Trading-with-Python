#!/usr/bin/env python
# coding: utf-8

# In[1]:


path= r"C:\Users\Asus\Downloads\Python-for-Finance-Repo-master\Python-for-Finance-Repo-master\07-Stock-Market-Analysis-Capstone-Project\Ford_Stock.csv"


# In[2]:


import pandas as pd


# In[4]:


ford_stock= pd.read_csv(path)


# In[5]:


ford_stock.head()


# In[12]:


import matplotlib.pyplot as plt


# In[13]:


plt.plot(ford_stock['Close'])


# In[32]:


file = ford_stock.copy()
file.index = pd.to_datetime(file['Date'])
file.drop('Date', axis =1, inplace = True)
plt.figure(figsize = [40,15])
plt.plot(file['Close'])
plt.plot(file.shift(1)['Close'], label = 'Shifted One Period Back')
plt.plot(file.shift(12)['Close'], label = 'Shifted One Period Back')
plt.legend()


# In[39]:


plt.figure(figsize = [40,15])
plt.plot(file['Close'], label= 'Original Data')
plt.plot(file.rolling(1).mean()['Close'], label = 'Rolled One Period Back')
plt.plot(file.rolling(12).mean()['Close'], label = 'Rolled 12 Period Back')
plt.legend()


# In[50]:


file['Close'].expanding(1).mean().plot()
plt.plot(file.rolling(12).mean()['Close'], label = 'Rolled 12 Period Back')


# In[42]:


file.shape


# In[52]:


file['Close'].expanding(120).mean().plot()
plt.plot(file.rolling(12).mean()['Close'], label = 'Rolled 12 Period Back')


# In[56]:


file['Close'].expanding(12
                       ).mean()


# In[54]:


file.head()


# ## Bollinger Bands

# In[57]:


file['20_Day Moving Average'] = file['Close'].rolling(20).mean()


# In[58]:


file['Upper Band']= file['20_Day Moving Average']+ file['Close'].rolling(20).std()


# In[60]:


file['Lower Band']= file['20_Day Moving Average']- file['Close'].rolling(20).std()


# In[65]:


plt.figure(figsize = [30,10])
plt.plot(file['Close'], label = 'Closing')
plt.plot(file['20_Day Moving Average'], label = '20 period MA')
plt.plot(file['Upper Band'], label = 'Upper Band')
plt.plot(file['Lower Band'], label = 'Lower Band')
plt.legend()


# In[ ]:




