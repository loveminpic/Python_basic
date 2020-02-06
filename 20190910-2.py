#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 13:35:19 2019

@author: mac
"""
"""예1"""

import urllib.request
page = urllib.request.urlopen("https://beans-r-us.appspot.com/prices.html")
text = page.read().decode("utf-8")

#예2
print(text.find(">$")) # >의 자리수를 나타낸다. 
print(text[234:238])


price_index = text.find(">$") + 2 
bean_price_str = text[price_index : price_index+4]
print(bean_price_str)


import urllib.request
import time

price = 5.0

while price < 5.0:
    time.sleep(1)
    page = urllib.request.urlopen("https://beans-r-us.appspot.com/prices.html")
    text = page.read().decode("utf-8")
    where = text.find("<$") + 2
    price_str = text[where:where+4]
    price = float(price_str) #강제 형변환
    
print("커피가격은?", price ,"아메리카도 가격인상하세요")

    