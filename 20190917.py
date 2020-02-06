#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 12:25:33 2019

@author: mac
""""""
week_days = " Mon, Tue, Wed, Thu, Fri, Sat, Sun "

#1. strip()
print(week_days.strip())

#2. split()
print(week_days.split(","))
print(week_days.strip().split())

#3. replace("a","b") a라는 문자를 b로 변경해라 
print(week_days.replace("M", "m"))

#4. upper() 소문자는 다 대문자로 변경해줌
print(week_days.upper())

#5. lower() 대문자는 다 소문자로 변경
print(week_days.lower())

#6. capitalize() 제일 첫 문자를 대문자
print(week_days.strip().capitalize())

#7. titel()
print(week_days.strip().title())

#8. startswith() 시작하는것이 괄호 안에 맞니 아니니? 트루 아니면 펄스로 나옴.
print(week_days.startswith(" M"))
print(week_days.startswith(" m"))

#9. endswith()
print(week_days.startswith("n "))
print(week_days.startswith("e"))

#문자열은 불변자료형이라 변환된 변수를 사용하고 싶을때는 새로운 변수에 넣어야함!

#오늘의 수업 목표
#1. 두 정수의 최대공약수를 구하는 함수
#2. 자연수 n이 주어졌을때, 1부터 n까지의 자연수 중에서 3의 배수이거나 숫자 3을 포함하는 숫자들의
#합을 구하는 함수 sum_of_3()를 만들자. 
"""
#def 함수명() :
 #   함수본체
"""

#예제 두개의 자연수 k, m 이 주어졌을 때, 만약 m이 3의 배수이거나 3으로 끝나는 숫자일 경우에 k와
    #m을 더하고, 아닌 경우에는 k를 리턴하는 함수 sum_if_3()를 구현하라.

#문자열 강제 형변환 str! m 이 숫자이기때문에 형변환이 필요함.

def sum_if_3(k, m) :
    if(m % 3 == 0) or (str(m).endswith("3")):
        return k+m
    else:
        return k 
    
print(sum_if_3(4,3))

#두 개의 정수 k,m이 주어졌을 때, m이 3의 배수이거나 3을 포함하는 경우에만 k+m을 리턴하고,
#아닌 경우에는 k만 리턴하는 함수 sum_if_3s()

def sum_if_3s(k,m):
    if (m % 3 == 0) or ("3" in str(m)):
        return k + m
    else:
        return k
    
print(sum_if_3s(4,113))

num1 = 5 
num2 = 10

if num1 < num2 :
    print("num1이 num2보다 작다")
else:
    if num1 == num2 :
        print("num1과 num2가 같다")
    else:
        print("num1이 num2보다 크다")


if num1 < num2 :
    print("num1이 num2보다 작다")
elif num1 == num2 :
    print("num1과 num2가 같다")
else:
    print("num1이 num2보다 크다") 


#==============================
"""
#while 조건 :
   # 실행코드
"""
#예제) 43을 7로 나누었을 때, 몫을 구하는 코드를 구하여라



number = 43
divisor = 7
answer = 0

while number > 0 :
    number = number - divisor
    if number > 0 :
     answer = answer + 1
     
   
#두개의 공약수를 찾는 gcd를 만들어라
#유클리드 호제법
     """
"""
gcd(a,b) 1. 작은 수로 큰 수를 나눈다.  만약 나눈어 떨어지면 , gcd 는 작은수
         2. 아니라면, 작은 수를 나머지로 나눈다. 그리고 나머지가 0이 될때 나눈 값이 최대공약수가 된다. 
         3. 15,9 두 숫자가 있다. -  15 / 9 하면 몫 1 이되고 나머지는 6이 남는다
         4. 그리고 9  / 6  - 몫 1 나머지 3 
                 6  /  3 - 몫 2 나머지 0 그래서 3이 최대공약수. 
                 """

"""
def gcd(a,b):
    if a < b :
        a, b = b, a
        
        while b != 0 :
            a, b = b, a%b
       
    return a 


def lcm(a,b):
    return a*b/gcd(a,b)
    

#range(시작, 끝, 계단(step))
    
for i in range(6):
    print(i)

for i in range(5):
    print(i,"의 제곱은", i**2)
    
for i in range(5):
    print("다섯번 반복하세요!")
    
a_word = "hamster"

for i in range(7):
    print(a_word[i])
    
for i in a_word:
    print(i)
    
    

#find_dog(word) - word에 dog가 있으면, True 없으면 False 리턴하는 함수

def find_dog(word):
    if "dog" in word:
        return True
    else:
        return False
    

    

#자연수 n이 주어졌을때, 1부터 n까지의 자연수 중에서 3의 배수이거나 숫자 3 을 포함하는
        #숫자들을 합하는 함수 sume_of_3s()
        
def sum_of_3s(n):
    sum = 0
    for i in range(1, n+1):
        if i % 3 == 0:
            sum += i
        elif '3' in str(i):
            sum += i    
    return sum

print(sum_of_3s(14))


"""
#예제, a_word <= aardvarks, a를 대문자로 변경.

a_word = "aardvarks"
new_word = ""

for char in a_word:
    if char == 'a':
        new_word += 'A'
    else:
        new_word += char
        
print(new_word)
        
        
#예제, n o r t h w e s t e r n -> northwestern

a_word = "n o r t h w e s t e r n"
new_word = ""
for char in a_word:
    if char != " ":
        new_word += char
        

#예제 1) a의 갯수는?
words = "when you are smiling, the whole world smiles with you"

def counta(anything):
    count = 0 
    for i in anything:
        if i == 'a':
            count = count + 1
    return count

print(counta(words))
print(words.count("a"))
print(words.lower().count("w"))


# 2) aeiou는 제거한 문자열 출력
new_words =""

for word in words:
    if word not in "aeiou":
        new_words += word
        
print(new_words)


