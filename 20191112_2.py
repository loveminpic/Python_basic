#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 13:13:26 2019

@author: mac

"""

import matplotlib.pyplot as plt
import pandas as pd


#1.데이터 만들기
names = ['Bob', 'Jessica','Mary', 'John', 'Mel']
births = [968, 155, 77, 578, 973]


BabyDataSet = list(zip(names, births))
print(BabyDataSet)

df = pd.DataFrame(data = BabyDataSet, columns = ['Names','Births'])

print(df)

df.to_csv('births1880.csv',index = False, header = False)

#2데이타 가져오기
print('====================')
Location = 'births1880.csv'
df = pd.read_csv(Location, names =['Names', 'Births'])
print(df)


import os
os.remove(Location)

print(df.dtypes)
print('================')
print(df.Births.dtype)
print(df['Births'].dtype)
print('================')

Sorted = df.sort_values(['Births'], ascending = False) # 내림차순
print(Sorted)
print(Sorted.head(1))

print(df.Births.max())

df.Births.plot()
MaxValue = df.Births.max()
MaxName = df.Names[df.Births == df.Births.max()]. values 
Text = str(MaxValue) + "-" + MaxName
print('================')
print(Text)

plt.annotate(Text,xy = (1,MaxValue), xytext = (8,0), xycoords = ('axes fraction', 'data'), textcoords = 'offset points')