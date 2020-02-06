#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 12:31:22 2019

@author: mac
"""

for i in range(4):
    print(i)
    """
예외처리!

try 코드가 실행되면 except를 건너뛰고 나머지로. 
try:
    code1
    
except:
    code2


"""

#예제 1
while True:
    try:
        number_input = input("A number please: ")
        number = int(number_input) # 강제로 스트링을 인트로 변경해주고 프린트해야함. 
        print("제곱의 결과는 " ,number**2 , "입니다.")
        break
    except:
        print("정수를 입력하세요.")
        

#예제 2      
number_input = input(" A number please: ")
try:
    number = int(number_input)
    a = 5/(number - 4)
    print("결과는", a)
    
except ValueError:    
    print("정수를 입력하세요.")
except ZeroDivisionError:
    print("4가 아닌 수를 입력하세요.")


"""
def to_define(n):
    아직 정의되지 않음
    
    raise NotImplementedError("아직 정의되지 않음")
    
    #함수를 정의하지 않고 넘어갈때 , 실수로 이 함수를 밑에서 호출하면 알려주는 경고방법
    #보통 """ """ ㅇ로 작성해놓으면 오류는 안떠서 모를 수도 있기떄문에. 
"""
"""   
print(to_define(3))
    



def my_square(n):
   숫자를 입력받아 제곱을 리턴하는 함수
 
    return n**2

print(help(my_square))
print(my_square(3))

"""

#100을 입력한 값으로 나누는 코드를 작성하라.
#1. 0이 아닌 숫자가 입력될 경우 100을 그 숫자로 나눔
#2. 0이 입력이되면, 0이 아닌 숫자를 입력하라는 문구출력
#3. 숫자가 아닌 값을 입력하면,숫자를 입력하라는 문구출력



while True:
    try:
        number_input = input("A number please: ")
        number = int(number_input)
        print(100/number)
        break
    except ValueError:
        print("정수를 입력하세요.")
    except ZeroDivisionError :
        print(" 0이 아닌 값을 입력하시오.")


#두개의 숫자 a,b를 입력받아 a/b를 계산하는 코드

while True:
    try:
        number_firstinput = input("A number please:")
        number_secondinput = input("Another number please:") 
        number1 = int(number_firstinput)
        number2 = int(number_secondinput)
        print(number1/number2)
        break
    except ValueError:
        print("두 수가 정수가 맞는지 확인하고 아닌 수는 정수를 입력하세요.")
    except ZeroDivisionError :
        print(" 0이 아닌 값을 입력하시오.")

    
        
    





























