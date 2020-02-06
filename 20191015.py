#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 12:37:13 2019

@author: mac


[] 리스트
{ } 사전형
() 투풀 - 괄호 생략 가능, 불ㅁ변자료ㅎ형
"""

"""
even_number = (2,4,6,8)
print(even_number)
print(type(even_number))

weeks = ('Mon','Tue','Wed','Thu','Fri')
print(weeks)
a = 10,20,30,40,50
print(type(a))
print(a)

print(a[1])
print(a[-1])
print(a[::2])

#=================================

b, c = 1,2

print(b)
print(c)

b,c = c,b # 서로  안에 값을 바꿔줌

print(b)
print(c)

def f(x):
    return x**2, x**3

#tuple로서 리턴을 하게됨
    
b, c = f(3)
print(b)
print(c)

#==================================
#불변자료형에 대한 설명

a = ("hello", "world")
#a[0] = "hi 이게 불가능 하다. 불변자료형이라서.
print(a[0])


b = ('hi', a[1])
print(b)

c = 'hi'+ a[1]
print(c)


c = ('hi',)+ (a[1],) #꼭 콤마를 붙여줘야 투플임을 알수 있다.
print(c)

d = ([1, 2, 3],'d') #서로 다른자료형을 담을 수 있음
#d[0] = [1, 2, 3, 4]  리스트는 변경이 가능한데 투플 안에 있으니까 안됨
print(d)

d[0].append(4) # 이건 가능
print(d)

#==================================


a = ('b', 'b', 'c', 'c', 'c')
print(a.count('c'))
print(a.index('c'))

a_file = open('Students_Records/Byun_Sato.txt','r')

for line in a_file.readlines(): #리스트로 출력 다
    print(line)
    
    
#date_of_birth('95.4.28') = (1995, 4, 28)
    
def date_of_birth(date_birth):
   
    #생년월일 정보를 (년, 월, 일) 형식으로 변경하는 함수
  
    year, month, day = date_birth.split(".")
    year = int(year) + 1900
    month = int(month)
    day = int(day)
    ymd = (year, month, day)
    return ymd

print(date_of_birth('95.4.28'))
        
        
"""

def date_of_birth(date_birth):
    year, month, day = map(int, date_birth.split("."))
    year += 1900
    return year, month, day

print(date_of_birth('95.4.28'))


import string # whitespace 처ㅣ리하기 위해
    
def record_getter(filename):
    """
    지정된 학생의 신상정보를 리스트에 담아 리턴 각 항목은 항목명과 내용의 튜플로 구성됨
    """
    
    std_data = []
    a_file = open(filename)
    for line in a_file.readlines():
        if line[0] == '#' or line in string.whitespace:
            continue
        else:
            item, value = line.split(":")
            item = item.strip()
            value = value.strip()
            if item == 'Date of Birth':
                value = date_of_birth(value)
            
            std_data.append((item,value))
    return std_data


print(record_getter('Students_Records/Byun_Sato.txt'))

#변사또의 전공을 알아내는 함수


Byun_data = record_getter('Students_Records/Byun_Sato.txt')
print(Byun_data)
for i in range(len(Byun_data)):
    if Byun_data[i][0] == 'Department':
        print("전공은", Byun_data[i][1])
        break

