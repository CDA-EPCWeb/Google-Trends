#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import sqlite3
import numpy as np


# In[2]:


kwBR=pd.read_csv('SeriesKeywords.csv')
kwMG=pd.read_csv('SeriesKeywordsMg.csv')
conn =sqlite3.connect("indicadores.db")
brasilDf=pd.read_sql_query("select * from brazil_df",conn)
statesDf=pd.read_sql_query("select * from states_df",conn)
conn.close()




# In[9]:


#Função que encontra as maxlag correlations (até 8 semanas de lag +- 2 meses)
def getMaxCorrelations(kw,ind,cat):
    dic={
        'Keyword' : [],
        'MaxCorrelation' : [],
        'Lag' : []        
    }
    for i in kw:
        maxcorr=0
        lag=-1
        for j in range(9): 
            corr=kw[:-j].reset_index()[i].corr(ind[j:].reset_index()[cat],method='spearman')
            if np.abs(corr)>=np.abs(maxcorr):
                maxcorr=corr
                lag=j
        dic['Lag'].append(lag)
        dic['MaxCorrelation'].append(maxcorr)
        dic['Keyword'].append(i)
    return dic




