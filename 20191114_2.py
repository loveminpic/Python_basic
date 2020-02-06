#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 10:25:40 2019

@author: mac
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy.random as np

#state/status/data/date

np.seed(111)
def CreateDataSet(Number):
    Output = []
    for i in range(Number):
        rng = pd.date_range(start = '1/1/2009', end = '12/31/2012', freq = 'W-MON')
        data = np.randint(low = 25, high = 1000, size = len(rng))
        status = [1,2,3]
        random_status =[status[np.randint(low = 0, high = len(status))] for i in range(len(rng))]
        state = ['GA','FL', 'fl', 'NY', 'NJ', 'TX']
        random_state = [state[np.randint(low = 0, high = len(state))] for i in range(len(rng))]
        
        Output.extend(zip(random_state,random_status,data,rng))
    return Output

dataset = CreateDataSet(4)
print(dataset[0:5])

df = pd.DataFrame(data = dataset,columns = ['State', 'Status', 'CustomerCount', 'StatusDate'])

print(df.head())
print(df.tail())
print(df.info())

df.to_excel('Lesson3.xlsx', index = False)

Location = 'Lesson3.xlsx'

df = pd.read_excel(Location,0,index_col = 'StatusDate')

print(df.head())
print(df.dtypes)
print(df.index)

"""
1. dataset을 가지고 데이터 프레임
'State', 'Status', 'CustomerCount', 'StatusDate'

2. 데이터 프레임의 정보 확인

3. 데이터프레임의 앞의 5개의 행을 확인

"""

print(df['State'].unique())

#lambda argument : expression
x = lambda a : a+10
y = lambda a,b : a*b
print(x(5))
print(y(3,7))

#1. 데이터의 state의 열에 있ㅇ는 유일한 값들을 확인
df['State'] = df.State.apply(lambda x : x.upper())
print(df.State.unique())
print(df.head(10))

#2. ㄴstatus의 값이 1인 자료만들만 선택해서 데이터 프레임으로 만들기
mask = df.Status == 1
print(mask)

df = df[mask]
print(df.head())

#3. NJ를 NY 변경
mask = df.State == 'NJ'
df['State'][mask] = 'NY'
print("=============================")
print(df.State.unique())

#Srate, Status의 연도를 기준으로 그룹으로 구분한 ㅅ후 각 그룹에 있는 CustomerCount에 대해서 사분위수를 이용한 이상치 처리. 

#groupby; apply & tansform

dftest = pd.DataFrame({'key': ['A','B','C','A','B','C','A','B','C'],'data': [0,5,10,5,10,15,10,15,20], 'test' :[ 1,1,1,1,1,1,1,1,1]})

print(dftest)
print(dftest.groupby('key').sum())
print(dftest.groupby('key').data.apply(lambda x : x.sum()))


print(dftest.groupby('key').data.transform(lambda x : x.sum()))
    

print(df.head())
print(df.reset_index().head())


Daily = df.reset_index().groupby(['StatusDate','State']).sum()

print(Daily.head(10))


del Daily['Status']
print(Daily.head(10))



#print(Daily.index)

print(Daily.index.levels[0])
print(Daily.index.levels[1])

StateYear = Daily.groupby([Daily.index.get_level_values(0).year, Daily.index.get_level_values(1)])


dftest1 = pd.DataFrame({'A' : [1,2,3,4,5,6,7,80,9,10]})
print(dftest1)
Q1 = dftest1.A.quantile(q =.25)
Q2 = dftest1.A.quantile(q =.5)
Q3 = dftest1.A.quantile(q =.75)
IQR = Q3-Q1

dftest1['Lower'] = Q1 - 1.5*IQR
dftest1['Upper'] = Q3 + 1.5*IQR


print(dftest1)
print(dftest1)
print(Q1)
print(Q2)
print(Q3)
print(IQR)


x= pd.Series([1,2,3,4,5])
y= pd.Series([5,5,5,5,5])
print(x>y)
print(x<y)
print((x>y)|(x == y))

Daily['Lower'] = StateYear['CustomerCount'].transform( lambda x: x.quantile(q=.25) - (1.5*(x.quantile(q=.75)-x.quantile(q=.25))))
Daily['Upper'] = StateYear['CustomerCount'].transform( lambda x: x.quantile(q=.75) + (1.5*(x.quantile(q=.75)-x.quantile(q=.25))))
Daily['Outlier'] = (Daily['CustomerCount'] < Daily['Lower']) | (Daily['CustomerCount'] > Daily['Upper'])
print(Daily.head(10))

Daily = Daily[Daily['Outlier'] == False ]

print(Daily.head(10))


