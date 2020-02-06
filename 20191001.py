# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

""" 

file = open("shopping_list.txt",'r')
buy_list = file.read()
file.close()

print(buy_list)
"""
def shopping(shopping_file):
    file = open(shopping_file,'r')
    buy_list = file.read()
    file.close()
    return buy_list


#1. 총 비용을 계산하는 코드. 6500원

buy_list = shopping('shopping_list.txt').split('\n')

print(buy_list)

_sum = 0

for item in buy_list:
    _sum += int(item.split()[2])#공백을 기준으로. 브래드 1 3000 이 리스트로 만들어짐
    
print("총비용은", _sum, "입니다.")

    

#2. 파일을 인자로 받아서 총 비용을 리턴해주는 함수 shopping_amount(shopping_file) -> 6500원
def shopping_amount(shopping_file):
    buy_list = shopping(shopping_file).split('\n')
    _sum = 0
    for item in buy_list:
        _sum += int(item.split()[2])
        
    return _sum

print(shopping_amount('shopping_list.txt'))


#3. 구매할 수량이 달라졌을 때, 그 총 가격을 리턴해주는 shopping_amount_n(shopping_file)

def shopping_amount_n(shopping_file):
    buy_list = shopping(shopping_file).split('\n')
    print("Bread, Tomato, Cola 구매할 수량을 순서대로 입력해주세요.")
    while True:
        try:
            number = list(map(int,input().split(', ')))
            break
        except ValueError:
            print("정수형으로 수량을 입력하시오.")
            
    _sum = 0
    for i in range(len(buy_list)):
        _sum += int(buy_list[i].split()[2])*number[i]
    return _sum 

print(shopping_amount_n('shopping_list.txt'))


#4. 쇼핑파일을 인자로 받아서 구매할 물건을 뭍고 그것의 가격을 리턴해주는 함수 shopping_item

def shopping_item(shopping_file):
    buy_list = shopping(shopping_file).split('\n')
    item = input("Bread, Tomato, Cola 중에서 살 품목을 적어주세요.")
    _sum = 0
    if 'bread' in item.lower():
        _sum += int(buy_list[0].split()[2])
    if 'tomato' in item.lower():
        _sum += int(buy_list[0].split()[2])
    if 'cola' in item.lower():
        _sum += int(buy_list[0].split()[2])
    
    return _sum

print(shopping_item('shopping_list.txt'))
    






