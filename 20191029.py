#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 12:30:58 2019

@author: mac
"""
"""
#1과 20사이에 있는 홀수 리스트를 만들자
odd1_20 = [1,3,5,7,9,11,13,15,17,19] #원소나열법

print(odd1_20)

i = 0  # while 로 리스트 
odd2_20 = []
while i <= 20:
    if i % 2 == 1:
        odd2_20.append(i)
    i += 1
print(odd2_20)

odd3_20 = [] # for 로 리스트

for i in range(21):
    if i % 2 == 1:
        odd3_20.append(i)
print(odd3_20)

def odd_number(num):
    odd = []
    for i in range(num+1):
        if i % 2 == 1:
            odd.append(i)
    return odd

print(odd_number(20))

odd_100M = odd_number(100000)

print(odd_100M[:21])

import time #odd_100M 에 10만개 들어가는 시간이 얼마나 걸리는지 먼저 모듈화

start = time.clock()
odd_100M = odd_number(100000)
end = time.clock()
print(end - start)


#집합에서 원소나열법으로 지금까지 해왔는데, 조건제시법으로 변경하여 이야ㅣ기를 진행

1. 조건제시법 
    {x | 0  < = x < = 100000, 단 x는 홀수}
2. 괄호 []로 바꿔주고, 
    [x | 0  < = x < = 100000, 단 x는 홀수] 
3. 수식을 for in 문으로 
    [x for x in range(100001),단 x는 홀수]  
4.조건 넣기 
    [x for x in range(100001),if x%2 ==1]   


odd1_100 = [x for x in range(100001) if x%2 ==1] 
print(odd1_100[:20])


# 0부터 100000 사이에 있는 값들 중에 홀수를 제곱한 값을 담고있는 리스트를 만들어라 

odd_100_square = [x**2 for x in range(100001) if x%2 == 1]

print(odd_100_square[:20])

odd2_100 = [2*x+1 for x in range(50000)]

print(odd2_100[:20])


odd1_100_square = [x**2 for x in odd1_100]
print(odd1_100_square[:20])
"""

import matplotlib.pyplot as plt

fig = plt.figure() #도화지 만듬
ax = fig.add_subplot(1,1,1)

ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('zero')

ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

xs = [x for x in range(-10,11)]
ys = [x**2 for x in xs]

plt.plot(xs,ys)
plt.show()


#연습1. math.exp [exp(1),exp(3),exp(5),exp(7), exp(9)] 조건제시법 만들기
from math import exp

odd_exp = [exp(n) for n in range(10) if n %2 == 1] 
print(odd_exp)

#연습2. math.exp [exp(3),exp(6),exp(9),exp(12), exp(15)] 조건제시법 만들기

odd_exp_3s= [exp(x*3) for x in range(1,6)]

print(odd_exp_3s)



import matplotlib.pyplot as plt

fig = plt.figure() #도화지 만듬
ax1 = fig.add_subplot(2,2,2)

ax1.spines['left'].set_position('center')
ax1.spines['bottom'].set_position('zero')

ax1.spines['right'].set_color('none')
ax1.spines['top'].set_color('none')

xs1 = [x for x in range(-10,11)]
ys1 = [abs(x**2 - 50) for x in xs1]

plt.plot(xs1,ys1)
plt.show()
    
    
    
    
#relu
fig = plt.figure() #도화지 만듬
ax2 = fig.add_subplot(2,2,3)

ax2.spines['left'].set_position('center')
ax2.spines['bottom'].set_position('zero')

ax2.spines['right'].set_color('none')
ax2.spines['top'].set_color('none')

xs2 = [x for x in range(-10,11)]
ys2 = [max(0,x) for x in xs2]

plt.plot(xs2,ys2)
plt.show()
    
    