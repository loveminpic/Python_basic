#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 09:39:42 2019

@author: mac
"""

a_number = 4
print (a_number *2)
print(type(a_number))

#변수명은  시작은 a-z, A-Z ,_ 로 시작
#변수명은 예약어 (print, def,type)사용 하지 않는다. 
#변수명은 대소문자 구별
#변수명 연산자는 (+ - * / 등)를 넣지 않음. 더불어 특수기호도 ?@# 이런거
#변수 타입을 지정해줄 필요가 없다. 대입 된 값에 따라 알아서 해줌. 

print(7)
print(type(7)) # 타입을 쓰면 7에 대한 타입을 알려줌.
print(type(7.0))

print(2+5)
print(2-5)
print(3*5)
print(4/2) # 결과 값이 2인데 소수 첫째까지 나옴. 2.0
print(4//2) # // 두번쓰면 최대정수형으로 나옴
print(7%2) #나머지 값이 나옴

print(-7/2) # -3.5 나옴
print(-7//2) # -4 나옴
print(-7%2) # -7 = -4*2 +1 = 1
print(2**3) # 2의 세제곱 . ** 이거 붙이면 지수표현
print(2**0.5) #이건 루트2 왜냐면 루트는 2의 1/2니까.

a_number = 2
print(a_number*7)
print((a_number + 6)/2) #지정된 변수는 연산에 사용가능

first_result = 9/2
print(first_result) # 변수를 출력하면 연산된 값인 4.5만 나옴
print(type(first_result))

print(a_number)
a_number = 9 
print(a_number) # a number 안을 2 에서 9로 변경해서 9로 값이 됨

print(int(3.8)) # 변수를 형변환을 강제로 함. int는 정수형인데 3.8 을 변환 시켜서 3이 나옴
print(float(4)) 

basic = 3
print(float(basic))
print(basic) # 강제 형변환을 한다고 해서 변수의 고유의 타입이 변하는것은 아니다. 
print(type(basic))

float_basic_int = float(basic) 
print(type(float_basic_int))
#새로운 변수에 형변환 하고 싶은 변수(float_basic_int)에 넣더라도 고유의 변수(basic)의 타입은 변하지 않는다. 

#연산우선순위 PEDMAS (괄호, 지수, 곱셈, 나눗셈, 덧셈, 뺄셈 )


#불리언 자료형 (bool) 자료형
#불리언 자료형에는 True, False 가 ㅇ있다.
# 예제) 강아지를 한마리 있다.
puppy = True
print(puppy)
print(type(puppy))

puppies = False
# puppy,puppies = True, False 넣으면 puppy 는 True, puppies 는 False 로 들어감

print("do I have a puppy?", puppy)
print("do I have a puppy?", puppies)

# not > and, or
print(True and True) #ture
print(True and False) #false 
print(True or False) # 수학에서는 하나씩 택하거나 둘다 먹거나 
print(False or True)

print(puppy and puppy) # ture 
print(not puppy and puppy) #Flase 

# != 같은지 다른지 비교하는 연산자, == 은 같은지 비교하는 연산자

print( 3 !=2 ) # True 다른지 여부를 확인 

# 결과값은 true and false 
# <= , >=, <, >


# 연습문제1, 두숫자의 평균값을 구하는 함수 
# average(a,b)

#   함수를 쓸때는 def 를 사용해야함. 그리고 ㅋ세미콜론 마지막. 
def average(a,b):
    """ 두개의 숫자 a,b를 받아 두 숫자의 평균을 구하는 함수. """
    
    return (a+b)/2

print(average(3,5))
print(help(average))

#연습문제2 두 숫자의 기하평균을 리턴하는 geometric_mean(a,b)

def geometric_mean(a, b):
    return (a*b)**0.5

#연습문제3 두 숫자의 a,b 사이의 거리를 리턴하는 distance(a,b), hint abs
def fistance(a, b):
    return abs(a-b)

#연습문제4 바닥 면적이 A이고 높이가 h 인 피라미드의 부피를 리턴하는 pyramid_bolume(A,h)
def pyramind_bolume(A, h):
    return (A*h)/3

#연습문제5 초 단위의 숫자를 받아서 일 단위의 값으로 되돌려주는 second2day(sec)
def second2day(sec):
    daysec = 60*60*24
    return (sec/daysec)
    






















