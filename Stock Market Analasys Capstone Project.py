#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd


# In[3]:


pip install pandas_datareader


# In[5]:


import pandas_datareader as web


# In[6]:


import datetime


# In[7]:


start= datetime.datetime(2012,1,1)


# In[9]:


end= datetime.datetime(2017,1,1)


# In[12]:


path= r"C:\Users\Asus\Downloads\Python-for-Finance-Repo-master\Python-for-Finance-Repo-master\07-Stock-Market-Analysis-Capstone-Project\Ford_Stock.csv"


# In[13]:


ford = pd.read_csv(path)


# In[14]:


ford.head()


# In[15]:


path2= r"C:\Users\Asus\Downloads\Python-for-Finance-Repo-master\Python-for-Finance-Repo-master\07-Stock-Market-Analysis-Capstone-Project\GM_Stock.csv"


# In[17]:


path3= r"C:\Users\Asus\Downloads\Python-for-Finance-Repo-master\Python-for-Finance-Repo-master\07-Stock-Market-Analysis-Capstone-Project\Tesla_Stock.csv"


# In[18]:


tesla= pd.read_csv(path3)


# In[19]:


gm = pd.read_csv(path2)


# In[21]:


import matplotlib.pyplot as plt


# In[27]:


plt.figure(figsize = [20,10])
plt.plot(gm['Close'], label= 'General Motors')
plt.plot(tesla['Close'], label= 'TESLA')
plt.plot(ford['Close'], label= 'FORD Motors')
plt.legend()


# In[30]:


plt.figure(figsize = [30,30])
plt.plot(gm['Volume'], label= 'General Motors')
plt.plot(tesla['Volume'], label= 'TESLA')
plt.plot(ford['Volume'], label= 'FORD Motors')
plt.legend()


# In[31]:


tesla.head()


# In[32]:


tesla['Volume'].max()


# In[33]:


tesla['Volume'].argmax()


# In[36]:


tesla.set_index('Date',drop=True, inplace = True)


# In[38]:


ford.set_index('Date',drop=True, inplace = True)
gm.set_index('Date',drop=True, inplace = True)


# In[39]:


tesla['Volume'].argmax()


# In[40]:


tesla.head()


# In[41]:


tesla.index = pd.to_datetime(tesla.index)


# In[42]:


tesla.head()


# In[43]:


type(tesla.index
    )


# In[45]:


tesla['Volume'].argmax()


# In[46]:


tesla.index[341]


# In[47]:


tesla['Traded Val']= tesla['Open']*tesla['Volume']


# In[48]:


ford['Traded Val']= ford['Open']*ford['Volume']


# In[49]:


gm['Traded Val']= gm['Open']*gm['Volume']


# In[51]:


ford.index = pd.to_datetime(ford.index)
gm.index = pd.to_datetime(gm.index)


# In[52]:


plt.figure(figsize = [30,30])
plt.plot(gm['Traded Val'], label= 'General Motors')
plt.plot(tesla['Traded Val'], label= 'TESLA')
plt.plot(ford['Traded Val'], label= 'FORD Motors')
plt.legend()


# In[59]:


plt.figure(figsize = [30,20])
plt.plot(ford['Open'], label = 'Ford Opening Stock')
plt.plot(ford.rolling(50).mean()['Open'], label= 'Ford 50 Day MA')
plt.plot(ford.rolling(200).mean()['Open'], label = 'Ford 200 Day MA')
plt.legend()


# In[60]:


import seaborn as sns


# In[84]:


df = pd.DataFrame(columns =['Ford Open','GM Open','Tesla Open'] )


# In[90]:


ford.rename({'Open':'Ford Open'}, inplace = True, axis = 1)


# In[91]:


tesla.rename({'Open':'Tesla Open'}, inplace = True, axis = 1)
gm.rename({'Open':'GM Open'}, inplace = True, axis = 1)


# In[92]:


df = pd.concat([ford['Ford Open'],gm['GM Open'],tesla['Tesla Open']], axis = 1)


# In[93]:


df


# In[94]:


df.fillna(0, 
          inplace =True, axis =1 )


# In[95]:


sns.pairplot(df)


# In[ ]:




