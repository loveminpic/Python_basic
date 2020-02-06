#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 21:21:09 2019

@author: mac

1. 자연수 n을 입력받아 n 번째 피보나치 수를 리턴하는 함수 fibo(n)를 구현하라.
참고) fibo(1) = 1, fibo(2) = 1, fibo(n) = fibo(n-1) + fibo(n-2)이다.
test) fibo(5) = 5, fibo(10) = 55
"""
def fibo(n):
	if n == 1:
		return 1
	else:
		return n + fibo(n-1)

print("fibo(3): " + str(fibo(3)))

print("fibo(15): " + str(fibo(15)))
 
 
"""
2. 쇼핑리스트(첨부파일)을 입력받아, 총 가격을 리턴하는 함수 shopping_total_sum(shopping_file)를 구현하라.
단, 이 함수는 아래의 조건을 만족시킨다.

"""

def shopping_total_sum(shopping_file):
    file = open(shopping_file,'r')
    buy_list = file.read()
    buy_list = buy_list.split('\n')

    for item in buy_list:
        _item = item.split(" ")
        print(_item[0],"의 가격은",_item[2])

    print("예) bread : 1, cola : 2")
    item = input("bread, Tomato, Cola 중에서 구매할 품목과 수량을 적어주세요 : ")
    try:
          buy = item.split(",")
          i, sum = 0, 0
          if 'bread' in item.lower():
              sum += (int(buy_list[0].split()[2]))*(int((buy[i].split()[2])))
              i += 1
          if 'tomato' in item.lower():
              sum += (int(buy_list[1].split()[2]))*(int((buy[i].split()[2])))
              i += 1
          if 'cola' in item.lower():
              sum += (int(buy_list[2].split()[2]))*(int((buy[i].split()[2])))
          print("총 가격은:",sum,"원 입니다.")
          
    except ValueError:
          print("정수형으로 잘 입력해주세요. 예시와 같이")

shopping_total_sum("shopping_list.txt")



"""
3. 리스트를 받아 중복값을 제거한 리스트를 리턴해주는 remove_elt(list) 함수를 구현하라.
test) remove_elt(['a', 'a', 'b', 'c', 'd', 'b']) = ['a', 'b', 'c', 'd']
"""

def remove_elt(list):
    newlist =[]
    newlist2 =[]
    newlist.extend(list)
    newlist.sort()
    for i in range(len(newlist)):
        if i == 0:
            newlist2.append(newlist[i])                        
        elif newlist2[-1] != newlist[i]:
            newlist2.append(newlist[i])           
    return newlist2

print(remove_elt(['a', 'a', 'b', 'c', 'd', 'b']))