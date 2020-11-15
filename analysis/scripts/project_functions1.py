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


# In[134]:


def heatmap(df):
    sns.heatmap(df.corr() , xticklabels=df.corr().columns, yticklabels=df.corr().columns, annot=True, cmap=sns.diverging_palette(220, 10, as_cmap=True)).set_title('Correlation of columns in dataset')


# In[123]:


def group_by(df):
    return df.groupby('won', as_index = False).mean()


# In[135]:


def barplot1(df):
    sns.barplot(y = 'shots', x= 'won', data =df).set_title('Shots by winning/losing team')


# In[136]:


def stripplot1(df):
    sns.stripplot(y = 'shots', x ='won', data = df).set_title('Shots by winning/losing team')


# In[137]:


def kdeplot1(df):
    sns.kdeplot(x = 'shots', hue = 'won', data = df).set_title('Shots by winning/losing team')


# In[127]:


def displot2(df):
    sns.displot(x = 'faceoffs(%)', hue = 'home/away', data = df)


# In[138]:


def stripplot2(df):
    sns.stripplot(x = 'faceoffs(%)', y = 'home/away', data = df).set_title('Faceoff percentage by Home/Away teams')


# In[139]:


def barplot2(df):
    sns.barplot(y = 'faceoffs(%)', x = 'home/away', data = df).set_title('Faceoff percentage by Home/Away teams')


# In[140]:


def kdeplot3(df):
    sns.kdeplot(x = 'ppg', hue = 'won', data = df).set_title('Powerplay goals for winning/losing teams')


# In[141]:


def violinplot3(df):
    sns.violinplot(y = 'ppg', x = 'won', data = df).set_title('Powerplay goals for winning/losing teams')


# In[142]:


def barplot3(df):
    sns.barplot(y = 'ppg', x = 'won', data = df).set_title('Powerplay goals for winning/losing teams')

