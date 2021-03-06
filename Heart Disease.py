#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 19:17:32 2021

@author: maddieenseleit
"""

import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', 50)
#Basic data exploration
df = pd.read_csv('/Users/maddieenseleit/Downloads/heart.csv')
print(df.head())
df1 = df[['HeartDisease', 'Oldpeak']]
df1.head()

# Can specify columns
df.dtypes
print(df.info())
df[df.HeartDisease == 0].describe()
df[df.HeartDisease == 1].describe()
#Observations show multiple binary variables. 
#No NA values
#The mean age in heart disease is higher by 5 years.
#RestingBP and Cholesterol has min of 0. Explore further

#Find correlation between values
corr = df.corr()["HeartDisease"]
print(corr.sort_values(ascending = False))
# OLDPEAK has highest correlation to heart disease
sns.pairplot(df, hue = 'HeartDisease')


df.hist(figsize=(12,12))
# FASTING BS IS HIGH AT 0 


plt.plot(df1["Oldpeak"], label = 'Heart Disease against Oldpeak')

