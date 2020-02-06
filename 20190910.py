#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 12:33:20 2019

@author: mac
"""

#9/10일
#문제6 변의 길이가 각각 a,b,c, 직각육면체의 표면적을 계산해주는 함수 box_surface(a,b,c)
def box_surface(a,b,c):
    s1, s2, s3 = a*b, b*c, a*c
    return 2*(s1 + s2 + s3)
print(box_surface(1,1,1))

#문제7 주어진 자연수 n이 짝수면 True , 홀수면 False를 리턴해주는 함수 even_test(n)
def even_test(n):
    if n%2==0 :
        return True
    else :
        return False
    
#문제8 반지름이 r인 원의 넓이를 구하는 함수 circle_area(r)
import math # 수학 기호 가져올때 
print(math.pi)      # 파이! 
print(math.sqrt(2)) # 루트사용
        
def circle_area(r):
    return math.pi * r ** 2

#문제9 변의 길이가 각각 a,b,c인 삼각형의 면적A를 계산하는 함수 triangle_area(a,b,c)
    # s = (a+b+c)/2, A= 루트(s(s-a)(s-b)(s-c))
    
def triangle_area(a,b,c):
    s = (a+b+c)/2 
    return math.sqrt(s*(s-a)*(s-b)*(s-c))

#문제10 정삼각형의 넓이를 구하는 eq_triangle_area(a) a는 한변의 길이
def eq_triangle_area(a):
    return (math.sqrt(3)/4) * a * a
    
print(eq_triangle_area(1))



hello = "hello"
print(hello)

hi = "hi"
print(hi)
print(type(hi))


falafel = "kebap"
print(falafel)

print("kebap" + " and " + falafel)
print("kebap" * 3)


import urllib.request
page = urllib.request.urlopen("https://beans-r-us.appspot.com/prices.html")
text = page.read().decode("utf-8")

print(text)

#인덱스
a_food = "kebap"
print(a_food[0])
print(a_food[3])
print(a_food[-2])

"""
#슬라이싱
문자열[시작인덱스 : 끝 인덱스 : 계단(step)]
끝 인덱스의 전까지만 나타낸다.

 
print(a_food[1:3])
print(a_food[0:3:2])
print(a_food[-1::-1])

"""






