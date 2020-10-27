# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 08:39:31 2020

@author: jonando93
"""

#Import Library
import pandas as pd #To work with dataset
import numpy as np #Math library
import seaborn as sns #Graph library that use matplot in background
import matplotlib.pyplot as plt #To plot some parameters in seaborn
import plotly.offline as py
py.init_notebook_mode(connected=True) #This code allow us to work with offline plotly version
import plotly.graph_objs as go #It's like 'plt' in matplot
import plotly.tools as tls #To access some useful tools in plotly
import warnings #To ignore some warnings
from collections import Counter #To do counter of some features

#Read Dataset
df_credit = pd.read_csv('https://storage.googleapis.com/kagglesdsdata/datasets/9109/12699/german_credit_data.csv?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=gcp-kaggle-com%40kaggle-161607.iam.gserviceaccount.com%2F20201027%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20201027T014939Z&X-Goog-Expires=259199&X-Goog-SignedHeaders=host&X-Goog-Signature=951d40d6645853d646e17cffaaf74543668ff05e315d649bed8aa397ebe178a4f79146abab14b19cd18f747007fc09607e0f93d7359ea0663d4073e4b1c99925599e34ba91633b284b23de262dd98aed0e69d088aac832d8d4dd8e4cebb80247d99adf20a2b3eb92aa0dd6a7d78acd0133306470c726dfac634fd5e404b9576c31556d8658ca7593c4e58092b3fb758db66c4ab77efe40e5dd05af1ad41a46d221db969a8b009a1af241700daeeb6f4c24ebb23d86acdffdd4b3ebdf1b41190f6a5a77f4167e6ac88f509857e520734ae74a1bdc57a0c9eddf42f3bda6a5a7353c222d019c2a18ee03475adcfba0063ac3afcc5f3d90a8722e1a6e1c8cadca68', index_col = 0)

#Quick Glimpse at the Dataset
print(df_credit.info())

#Looking for unique values
print('\n', df_credit.nunique())

#Top 5 row
print('\n', df_credit.head())

#Data Exploration
##Target Variable Distribution
trace0 = go.Bar(
            x = df_credit[df_credit["Risk"]== 'good']["Risk"].value_counts().index.values,
            y = df_credit[df_credit["Risk"]== 'good']["Risk"].value_counts().values,
            name = 'Good credit'
    )

trace1 = go.Bar(
            x = df_credit[df_credit["Risk"]== 'bad']["Risk"].value_counts().index.values,
            y = df_credit[df_credit["Risk"]== 'bad']["Risk"].value_counts().values,
            name = 'Bad credit'
    )

data = [trace0, trace1]

layout = go.Layout(
    
)

layout = go.Layout(
    yaxis=dict(
        title='Count'
    ),
    xaxis=dict(
        title='Risk Variable'
    ),
    title='Target variable distribution'
)

fig = go.Figure(data=data, layout=layout)

py.plot(fig, filename='Credit Risk Analysis - Data Exploration - Target Variable Distribution - Output.html')