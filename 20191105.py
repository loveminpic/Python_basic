#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Tue Nov  5 12:35:23 2019

@author: mac



튜플의 단점겸 장점은 수정이 불가
리스트 단점은 느림
딕셔너리 리스트보다는 빠른데 키와 키값을 연결 해야함. 이차 삼차 배열을 만들수 없다. 
"""
import numpy as np

a = np.array([0,1,2,3])

print(a)

print(type(a))


b = np.array((0,1,2,3,))


print(b)

c = a == b

print(c.dtype)
print(b.dtype)
print(a.dtype)

d = np.array([True, True, False], dtype = int)
e = np.array([True, True, False])
print(d)
print(e)


import time
start1 = time.clock()

a_list = range(0,100000000,2)
a_list_square = [i**2 for i in a_list]

end1 = time.clock()
print("time1 is", end1-start1)

start2= time.clock()
an_array = np.arange(0,100000000,2)
square = an_array**2
end2 = time.clock()
print("시간2는", end2 - start2)



import numpy as np

a_1dim = np.array([0,1,2,3])
print(a_1dim)
print(a_1dim.ndim)
print(a_1dim.shape)


a_2dim = np.array([[1,2],[3,4],[5,6]])

print(a_2dim)
print(a_2dim.ndim)
print(a_2dim.shape)

print(len(a_2dim))
print(len(a_2dim.shape))

print(np.shape(a_2dim)[0] == len(a_2dim))
len(np.shape(a_2dim)) == a_2dim.ndim











