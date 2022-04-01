#!/usr/bin/env python
# coding: utf-8

# # WITH PANDAS AND MATPLOTLIB

# In[1]:


import numpy as np 
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from collections import Counter
import warnings
warnings.filterwarnings('ignore') 


# INSTRUCTIONS
# 
# 1. Number of people by gender
# 1. Kill weapon
# 1. Age of killed people
# 1. Race of killed people
# 1. Killed People According to Races (Pie Chart)
# 1. Most common 15 Name or Surname of killed people
# 
# <br>

# read data
# 
# if didn't work you can use this parameters: encoding="windows-1252"

# In[2]:


kill = pd.read_csv('PoliceKillingsUS.csv', encoding="windows-1252")


# ## 1: Plot number of people by gender

# In[3]:


kill.head(5)


# In[4]:


# with matplotlib
a = np.array(kill.gender.value_counts())
b = np.array(kill.gender.value_counts().index)
plt.bar(b,a)
plt.title("Gender Distribution")
for i in range(len(b)):
    plt.text(i,a[i], a[i],ha='center',va='bottom')

plt.show()


# ## 2: Plot 7 most common kill weapons

# In[68]:


most = kill.armed.value_counts().head(7)
most


# In[5]:


# with matplotlib
i = np.array(kill.armed.value_counts().head(7).index)
most = np.array(kill.armed.value_counts().head(7))
plt.bar(i,most)
plt.xticks(i,rotation=45)
for j in range(len(most)):
    plt.text(j,most[j], most[j],ha='center',va='bottom')

plt.show()


# ## 3: Plot number of age of killed people under two groups : Under 25 and Above 25

# In[7]:


kill["age_cat"] = kill.age.apply(lambda x : "above25" if x > 25 else "below25")
kill.head(5)


# In[8]:


kill.age_cat.value_counts()


# In[9]:


# with matplotlib
x = np.array(kill.age_cat.value_counts().index)
y = np.array(kill.age_cat.value_counts())
plt.bar(x, y)
for i in range(len(x)):
    plt.text(i, y[i], y[i], va="bottom", ha="center")
plt.show()


# ## 4: Plot number of killed poeple by race

# In[10]:


kill["race"].value_counts()


# In[13]:


# with matplotlib
plt.figure(figsize=(10,6))
k = np.array(kill["race"].value_counts())
kk = np.array(kill["race"].value_counts().index)
plt.bar(kk, k)
plt.title("Race of Killed People", color="r")
plt.show()


# ## 5: Killed People According to Races (Pie Chart)

# In[14]:


kill.head()


# In[15]:


kill["race"].unique()


# In[16]:


kill["race"].value_counts(dropna=False)


# Problem: missing value on race column.

# **INSTRUCTION-1: Drop the all raws that contain missing value (dropna)**

# In[17]:


kill.shape


# In[18]:


kill.dropna(how="any",inplace=True)


# In[19]:


kill.shape


# **INSTRUCTION-2: Demonstrate Race Ratio of Killed People by a Pie Chart (You can use Matplotlib)**

# In[20]:


kill["race"].value_counts()


# In[21]:


kill["race"].value_counts().index


# In[22]:


kill["race"].value_counts().values


# In[23]:


# matplotlib
q = np.array(kill["race"].value_counts())
w = np.array(kill["race"].value_counts().index)
explode_list = [0,0,0.2,0,0,0]
plt.figure(figsize=(10,6))
plt.pie(q, labels=w, autopct="%.2f", startangle=75, explode=explode_list)

plt.show()


# In[ ]:




