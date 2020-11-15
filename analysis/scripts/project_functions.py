#!/usr/bin/env python
# coding: utf-8

# In[120]:


import pandas as pd
import seaborn as sns


# In[121]:


def load_and_process(url_or_path_to_csv_file):
    
        df = (pd.read_csv(url_or_path_to_csv_file)
             .dropna(axis = 0)
             .drop(columns = ['game_id', 'team_id', 'head_coach', 'settled_in'])
             .rename(columns = {"HoA" : "home/away", "powerPlayOpportunities" : "power_plays", "powerPlayGoals" : "ppg", "faceOffWinPercentage" : "faceoffs(%)"}))
        return df


# In[122]:


def heatmap(df):
  sns.heatmap(df.corr() , xticklabels=df.corr().columns, yticklabels=df.corr().columns, annot=True, cmap=sns.diverging_palette(220, 10, as_cmap=True))


# In[123]:


def group_by(df):
    return df.groupby('won', as_index = False).mean()


# In[124]:


def barplot1(df):
    sns.barplot(y = 'shots', x= 'won', data =df)


# In[125]:


def stripplot1(df):
    sns.stripplot(y = 'shots', x ='won', data = df)


# In[126]:


def kdeplot1(df):
    sns.kdeplot(x = 'shots', hue = 'won', data = df)


# In[127]:


def displot2(df):
    sns.displot(x = 'faceoffs(%)', hue = 'home/away', data = df)


# In[128]:


def stripplot2(df):
    sns.stripplot(x = 'faceoffs(%)', y = 'home/away', data = df)


# In[129]:


def barplot2(df):
    sns.barplot(y = 'faceoffs(%)', x = 'home/away', data = df)


# In[130]:


def kdeplot3(df):
    sns.kdeplot(x = 'ppg', hue = 'won', data = df)


# In[131]:


def violinplot3(df):
    sns.violinplot(y = 'ppg', x = 'won', data = df)


# In[132]:


def barplot(df):
    sns.barplot(y = 'ppg', x = 'won', data = df)


# In[ ]:




