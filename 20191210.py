#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 16:13:47 2019

@author: mac
"""
import pandas as pd

users = pd.read_table('user.txt', sep = "|", index_col = 'user_id')

print(users.head())

#1. 처음부터 25개의 행을 확인하여라.
print(users[0:25])


#2. 끝에 10개의 행을 확인하여라.
print("---2-----------------")
print(users.tail(10))

#3. 데이터의 관측치는 몇 개있는가.
print("-3-------------------")
print(users.shape[0])  #행의 갯수 , 관측치는 몇 개 있는 가는 행을 물어보는거임! 
#print(users.shape[1])  #열의 갯수 

#4. 열의 개수는 몇개인가.
print("-4-------------------")
print(len(users.columns))

#5. 열의이름을 프린트하여라.
print("5--------------------")
print(users.columns)

#6. 인덱스는 어떻게 되어있는가.
print("6--------------------")

print(users.index)
#7. 각 열의 데이터타입은 어떻게 되는가.
print("7--------------------")

print(users.dtypes) 

#한가지 열만 하고 ㅇ싶으면 users.age.dtype

#8. occupation열만 출력하여라.
print("8--------------------")
print(users.occupation)


#9. 데이터셋에 있는 서로다른 occupation은 몇개인가. 
print("9--------------------")
print(len(users.occupation.unique()))
print(users.occupation.nunique())


#10. 가장 많이 등장한 직업은?
print("10-------------------")
print(users.occupation.value_counts())
print(users.occupation.value_counts().head(1)) #특정 만 출력할떄 

#11. 데이터 프레임을 요약 - 개수, 최대값, 최소값 등. 
print("11-------------------")

print(users.describe())
"""
1. 처음부터 25개의 행을 확인하여라.
2. 끝에 10개의 행을 확인하여라.
3. 데이터의 관측치는 몇 개있는가.
4. 열의 개수는 몇개인가.
5. 열의이름을 프린트하여라.
6. 인덱스는 어떻게 되어있는가.
7. 각 열의 데이터타입은 어떻게 되는가.
8. occupation열만 출력하여라.
9. 데이터셋에 있는 서오다른 occupation은 몇개인가. 
10. 가장 많이 등장한 직업은?
11. 데이터 프레임을 요약 - 개수, 최대값, 최소값 등. 
"""



data = {'A' :[1,2,3,4,5,6],
        'B' :[0,2,4,6,8,10],
        'C' :[2,2,2,2,2,2]}

df = pd.DataFrame(data)

print(df)


print(df.sum()) #각 열의 합! 구하기

print(df.sum(axis =1)) #각 행의 합 구하기

import numpy as np

#1. A열의 인덱스 4,5 인 자료를 결측치(nan)변경하기

#df.A[4,5] = np.NAN
df.loc[4:5,'A'] = np.nan
print(df)

#2. C열에 인덱스 2,3,4,5, 인 자료를 결측치 변경
df.loc[2:5,'C'] = np.nan
#df.C[2,3,4,5] = np.NAN
print(df)

#3. 각 열과 행에 결측치가 아닌 갯수를 각각 구하기
print(df.notnull().sum())
print(df.notnull().sum(axis = 1))

#4. 각 행에 결측치가 아닌 값이 2개 이상인 데이터 프레임의 일부를 출력 하시오.
print(df.loc[df.notnull().sum(axis=1) > 1])


#5.각 열에 결측치가 아닌 값이 3개 이상인 df의 일부를 출력
print(df.loc[:,df.notnull().sum() > 2])


#각 열에 결측치가 아닌 값이 80%이상이면 선택

print(df.loc[:,df.notnull().sum() > len(df)*0.6])


#결측치 있는 행 열들을 다 제거 시키는 것
print(df.dropna())
print(df.dropna(axis = 1))


print(df.dropna(thresh = 0.6*len(df),axis = 1))
