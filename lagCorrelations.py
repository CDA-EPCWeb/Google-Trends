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


# In[3]:


#obtendo dados apenas das semanas desejadas dos indicadores
brasilDf=brasilDf.iloc[0:44]
statesDf=statesDf[statesDf['state']=='MG']
statesDf=statesDf.reset_index()
statesDf=statesDf.iloc[0:44]


# In[4]:


statesDf


# In[5]:


#reordenando colunas para mais facil visualização
cols=kwMG.columns.tolist()
cols=cols[0:1]+cols[-1:]+cols[1:-1]
kwMG=kwMG[cols]
cols=kwBR.columns.tolist()
cols=cols[0:1]+cols[-1:]+cols[1:-1]
kwBR=kwBR[cols]


# In[6]:


#normalizando os dados de indicador a serem usados
brasilDf.loc[:,'new_week_cases']=(brasilDf.loc[:,'new_week_cases']/brasilDf.loc[:,'new_week_cases'].max())*100
brasilDf.loc[:,'new_week_deaths']=(brasilDf.loc[:,'new_week_deaths']/brasilDf.loc[:,'new_week_deaths'].max())*100
statesDf.loc[:,'new_week_cases']=(statesDf.loc[:,'new_week_cases']/statesDf.loc[:,'new_week_cases'].max())*100
statesDf.loc[:,'new_week_deaths']=(statesDf.loc[:,'new_week_deaths']/statesDf.loc[:,'new_week_deaths'].max())*100


# In[7]:


#criando a coluna de semanas nas keywords
semanas=[]
for i in range(len(kwBR)):
    semanas.append(i+9)
kwMG['epidemiological_week']=semanas
kwBR['epidemiological_week']=semanas


# In[8]:


#extraindo apenas dados necessários das databases
brasilDf=brasilDf.set_index('epidemiological_week')
statesDf=statesDf.set_index('epidemiological_week')
brasilDf=brasilDf[['new_week_cases','new_week_deaths']]
statesDf=statesDf[['new_week_cases','new_week_deaths']]
kwBR=kwBR.set_index('epidemiological_week')
kwMG=kwMG.set_index('epidemiological_week')
kwBR=kwBR.drop('date',axis=1)
kwMG=kwMG.drop('date',axis=1)


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


# In[10]:


lagcorr=pd.DataFrame(getMaxCorrelations(kwBR,brasilDf,'new_week_cases'))
lagcorr=lagcorr.set_index('Keyword')
lagcorr.sort_values(by='MaxCorrelation',ascending=True)[0:20]






