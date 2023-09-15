#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
df=pd.read_csv('E:\pride/stock price apple.csv')
df


# In[6]:


print("first five set of data:")
df.head()


# In[5]:


print("last five set of data:")
df.tail()


# In[6]:


df.info()


# In[10]:


print("data types in dataset:")
df.dtypes


# In[22]:


print("print only data of specific location: ")
print(df.loc[1]['Date'])
print(df.loc[1]['High'])


# In[24]:


print("dataset of first 1000 dataset")
df.iloc[:1001]


# In[29]:


print("no of (rows,columns) in dataset:",df.shape)


# In[45]:


print("showing dataset from highest value of of all time to lowest:")
max_of_high=df.sort_values(by='High', ascending=False)
max_of_high.head(1)


# In[43]:


df2=df["Close"].mean()
print("average closing price of dataset:\n",df2)


# In[50]:


df3=df.describe()
print(df3)


# In[48]:


print("shows the difference of opening and closing of product in stockmarket:")
df4=df['Close']-df['Open']
print(df4)


# In[60]:


print("return the minimun value of each column in dataset:")
df.min()


# In[61]:


print("return the maximum value of each column in dataset:")
df.max()


# In[5]:


import pandas as pd
import numpy as np
df=pd.read_csv('E:\pride/stock price apple.csv')
df.isnull()


# In[7]:


df.notnull()


# In[7]:


df.columns


# In[13]:


df[df['Open']==max(df['Open'])]


# In[14]:


df[df['Open']==min(df['Open'])]


# In[3]:


import matplotlib.pyplot as plt
print(plt.style.available)


# In[7]:


df


# In[3]:


import matplotlib.pyplot as plt


# In[12]:


plt.plot(dates,opening_price,color='red',linewidth=2)
plt.xlabel('Date')
plt.ylabel('Open')
plt.title('apple stock price')
plt.show()


# In[19]:


#line plot
dates=df['Date']
Closing_price=df['Close']
plt.plot(dates,Closing_price,marker='*')
plt.show()


# In[22]:


df.iloc[999]


# In[6]:


df_groupby_year=df.groupby('year')
year=df_groupby_year
avg_close=df_groupby_year['Close'].mean()
avg_close


# In[7]:


plt.plot(avg_close,color='red',linewidth=2)
plt.xlabel('year')
plt.ylabel('average_of_closing')
plt.title('apple stock price')
plt.show()


# In[12]:


avg_open=df_groupby_year['Open'].mean()
avg_open


# In[43]:


plt.plot(avg_close,color='red',linewidth=2)
plt.xlabel('year')
plt.ylabel('average_of_opening')
plt.title('apple stock price')
plt.show()


# In[13]:


plt.plot(avg_close,color='red',label="close")
plt.plot(avg_open,color='blue',label="open")
df_groupby_year=df.groupby('year')
year=df_groupby_year
plt.xlabel('year')
plt.ylabel('measure')
plt.title('apple stock price')
plt.legend(loc="center left")
plt.show()


# In[30]:


plt.figure(figsize = (18,9))
plt.plot(range(df.shape[0]),(df['Low']+df['High'])/1.0)
plt.xticks(range(0,df.shape[0],365),df['year'].loc[::365])
plt.xlabel('Date',fontsize=18)
plt.ylabel('Mid Price',fontsize=18)
plt.show()


# In[53]:


plt.figure(figsize = (30,15))
plt.plot(range(df.shape[0]),(df['Low'])/1.0)
plt.xticks(range(0,df.shape[0],365),df['year'].loc[::365])
plt.xlabel('Days',fontsize=18)
plt.ylabel('LOW',fontsize=18)
plt.show()
max_of_high.tail(1)


# In[56]:


plt.figure(figsize = (30,20))
plt.plot(range(df.shape[0]),(df['High'])/1.0)
plt.xticks(range(0,df.shape[0],365),df['year'].loc[::365])
plt.xlabel('year',fontsize=18)
plt.ylabel('high',fontsize=18)
plt.show()
max_of_high=df.sort_values(by='High', ascending=False)
max_of_high.head(1)


# In[42]:


df.max()


# In[8]:


#histogram
avg_high=df_groupby_year['High'].mean()
avg_high


# In[20]:


avg_low=df_groupby_year['Low'].mean()
avg_low


# In[14]:


plt.hist(x=[year],color='orchid')
plt.title('average of high of year')
plt.xlabel('df(groupby_year)')
plt.ylabel('average_high')
plt.show()


# In[32]:


import seaborn as sns
plt.figure(figsize=(5,5))
sns.boxplot([df['High'],df['Low']])
sns.boxplot()
p = plt.title('distribution for high and low')
p = plt.ylabel('price')
plt.xticks([0,1.4],['High','Low'])
plt.show()


# In[4]:


import seaborn as sns
plt.figure(figsize=(5,5))
sns.boxplot([df['Open'],df['Close']])
sns.boxplot()
p = plt.title('distribution for open and close')
p = plt.ylabel('price')
plt.xticks([0,1.4],['Open','Close'])
plt.show()


# In[11]:


import seaborn as sns
sns.stripplot(x = 'Low',y='High',data=df)
plt.show


# In[ ]:




