#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 09:48:39 2019

@author: mac
"""
"""
자료 - 수치자료(양적자료), 범주형자료(질적자료)

1. 양적자료 또는 수치자료
    1) 연속형 자료 예) 키, 몸무게 등
    2) 이산형 자료 예) 자동차의 수 

2. 범주형자료 또는 질적자료
    1) 순위형 자료 예) 선호도, 평점
    2) 명목형 자료 예) 성별, 혈액형
    
================
시각화
1. 선그래프 : 변화 하는 것을 이야기할 떄 
2. 막대그래프 : 비교할 떄 , 범주형 자료나 이산형 자료
3. 히스토그램 : 비교할 떄,  연속형 자료 
4. 원그래프 : 비율에 대하여
5. 산점도 : 두개 이상 변수에 대하여 관계
"""

import matplotlib.pyplot as plt

data_f = open('Seoul_pop1.csv')

years = []
populations =[]

for line in data_f:
    (year,population) = line.split(",")
    years.append(int(year))
    populations.append(int(population))

data_f.close()

print(years)
print(population)

fig1 = plt.figure()
ax1 = fig1.add_subplot(1,1,1)

plt.plot(years, populations, color = "green", marker = 'o', linestyle = "solid")
plt.title('Seoul Population Change')

plt.ylabel('10Million')
plt.show()

sport = ['Archery', 'Badminton', 'Boxing', 'Teakwondo', 'Wrestling']
medals = [39, 19, 20, 43, 19]

fig2 = plt.figure()
ax2 = fig2.add_subplot(1,1,1)

plt.bar(sport, medals)
plt.ylabel ('Medal')
plt.title('Olympic Medals')
plt.show()




fig3 = plt.figure()
ax3 = fig3.add_subplot(1,1,1)

memtions = [500,505]
years = [2013,2014]

plt.bar(years, memtions)

plt.xticks(years)

plt.axis([2012.5, 2014.5, 499,506])



fig4 = plt.figure()
ax4 = fig4.add_subplot(1,1,1)

label = ['Blue', 'Green','Red', 'white']
x = [ 50, 23, 41, 11]
explode = [ 0,0,0,0.3]
plt.pie(x,autopct = "%1.1f%%", shadow = True, colors = label, labels = label, explode = explode)

import numpy as np #수치형 자료들이 담아있는


fig5 = plt.figure()
ax5 = fig5.add_subplot(1,1,1)

gaussian_numbers = np.random.randn(1000)

plt.hist(gaussian_numbers,bins = 10)
plt.title('Gaussian Histogram')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()


fig6 = plt.figure()
ax6 = fig6.add_subplot(1,1,1)

#핸드폰에 저장된 친구의 수와 핸드폰 사용시간

num_friends = [ 41, 26, 90,50, 18, 124, 88, 72, 51, 3]
phone_time = [4.1, 3.3, 5.7, 4.2, 3.2, 6.4, 6.0, 5.1, 3.1, 1.0]


plt.scatter(num_friends, phone_time)
plt.show()

#산점도를 통해 인과 관계를 알수는 없다. 


