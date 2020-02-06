#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 09:34:15 2019

@author: mac
"""

import pandas as pd
import numpy.random as np
import matplotlib.pyplot as plt

names = ['Bob', 'Jessica', 'Mary', 'John', 'Mel']

np.seed(500)
random_names = [names[np.randint(low = 0, high = len(names))] for i in range(1000)]

print(random_names[0:20])
#randint(low = 1, high = 100 )

births = [np.randint(low = 0, high = 1000 ) for i in range(1000)]

print(births[0:10])

BabyDataSet = list(zip(random_names, births))
print(BabyDataSet[0:10])

df =  pd.DataFrame(data = BabyDataSet, columns = ['Names','Births'])
print(df)

df.to_csv('births1880.csv', index = False, header = False)

Location = 'births1880.csv'
df = pd.read_csv(Location, header = None)

print(df.head(10))
print(df.tail())
print(df.info())


df = pd.read_csv(Location, names = ['Names', 'Births'])

print(df.head())
"""
print(df.Names.unique())

for x in df.Names.unique():
    print(x)
    
print(df.Births.describe())

name = df.groupby('Names')
df= name.sum()
print(df)


df.Births.plot.bar()

df.sort_values(by = "Births", ascending = False)
print(df)

"""


