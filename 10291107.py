#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 09:35:50 2019

@author: mac
"""
import numpy as np
a = np.arange(10)

print(a)

b= np.arange(1,9,2)

c = np.linspace(0,1,6) # 영부터 1까지 6개로 쪼개진다.
print(c)

d = np.linspace(0, 1, 6, endpoint = False)
print(d)

e = np.linspace(0, 1, 7)
print(e)

f = np.zeros((2,2))
print(f)

g= np.ones((2,2))
print(g)

h = np.diag([1,2,3])
print(h)

h1 = np.diag((1,2,3))
print(h1)

h2 = np.diag(np.arange(1,7,2))
print(h2)

i = np.eye(2)
print(i)

h3 = np.arange(0, 9).reshape((3, 3))
print(h3)
h4 = np.diag(h3)
print(h4)

h5 = np.diag(h3,k =1)

print(h5)

print(np.diag(np.diag(h3, k = 1), k = -1))

print(np.ones((2,3)).dtype)

print(np.zeros((2,2)).dtype)

print(np.eye(3).dtype)


print(np.array([1+3j,2+5j]).dtype)

#np.random.rand() : [0, 1)
#np.random.randn() : 정규분포에서 난수를 생성

x = np.random.rand(4)
print(x)

y= np.random.randn(2,3) 
print(y)

g1 = np.random.rand(3)
print(g1)

g1 = np.random.randn(2,3)
print(g1)


np.random.seed(0)
print(np.random.rand(4))

np.random.seed(0)
print(np.random.rand(4))

np.random.seed(1240)
print(np.random.rand(4))

import matplotlib.pyplot as plt

rand_numbers = np.random. rand(1000)

plt.hist(rand_numbers, bins= 10)
plt.show()

gaussian_numbers = np.random.randn(1000)

plt.hist(gaussian_numbers, bins = 10)

plt.show()


#문제
array2 = np.ones((4,4))
array2[2,3] = 2
array2[3,1] = 6
print(array2)

print(np.diag(np.arange(2,7), k= -1))
print("==============")
print(np.diag(np.arange(2,7), k= -2))
print("============22==")
print(np.arange(4, 0, -1))


a = np.arange(4,0,-1).reshape((2,2))
print(a)
print(np.tile(a,(2,3)))



