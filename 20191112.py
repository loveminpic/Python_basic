#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 12:36:03 2019

@author: mac
"""

import numpy as np
import matplotlib.pyplot as plt

#y = 3x
xs = np.linspace(0,3,30)
ys = xs*3
plt.plot(xs,ys)
plt.plot(xs,ys,'o')
plt.show()

#y = x^2
xs =  np.linspace(-1,1,20)
ys = xs**2
plt.plot(xs,ys)
plt.show()


data = np.loadtxt('populations.txt')
print(data)

year, hares, lynxes, carrot = data.T
#t는 열을 행으로 바꿔주는 역할

print(year)

plt.axes([0.2,0.2,0.5,0.8])
plt.plot(year, hares, year,lynxes, year, carrot)

plt.legend(('Hares', 'lynxes','Carrot'), loc =(1.05,0.5))

