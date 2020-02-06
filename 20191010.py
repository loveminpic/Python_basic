#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 09:35:57 2019

@author: mac
"""

#key - value ㅅㅏ전형이며 벨류에는 어떠한 형태든 ㄱ들어갈 수 있지만 key에는 실수 정수 등 변경할 수 없는 자료형이 들어감.
#사전은 중ㅅ괄호{} 
"""
peongteak - 22
suwon - 18
jeju - 25
"""

city_temperature = {}
city_temperature['peongteak'] = 22
print(city_temperature) #{'peongteak': 22}

city_temperature['suwon'] = 18
city_temperature['jeju'] = 25
print(city_temperature) #{'peongteak': 22, 'suwon': 18, 'jeju': 25}
city_temperature.update({'ansung' : 21, 'yongin' : 23})
print(city_temperature) #{'peongteak': 22, 'suwon': 18, 'jeju': 25, 'ansung': 21, 'yongin': 23}
print(city_temperature['ansung']) #21 

print(city_temperature.get('suwon'))

print('suwon' in city_temperature) #수원이 들어있는지 ㅇ없는지
print('seoul' in city_temperature)

key_temp = city_temperature.keys() #key만 모아서
print(key_temp)

value_temp = city_temperature.values() #values 만 모아서
print(value_temp)

item_temp = city_temperature.items() #key values 같이
print(item_temp)

for key in city_temperature.keys():
    print(key, "의 온도는 ", city_temperature[key])
    
for key in city_temperature:
    print(key, "의 온도는 ", city_temperature[key])
    
print(dir(city_temperature)) 

city_temperature.pop('suwon') # 수원 해당을 지워라! 
print(city_temperature)


result = open("scores_list.txt",'r')
scores={}
scores2={}

for line in result:
    name, score = line.split() #공란을 기준으로 구분
    try:
        scores[float(score)] = name
    except:
        continue
result.close()
print(scores)
print(sorted(scores.keys(),reverse= True)) #오름차순 정렬하는 솔트 , 이건 함수 그리고 리버스로 정렬 다시

""" 
#3등까지 만 나타내기
for key in sorted(scores.keys(),reverse= True):
    if i <= 3:
        print(scores[key],"의 점수는", key, "이고" ,i ,"등 입니다.")
        i = i+1
    else:
        i += 1
"""
for i in range(3):
    key = sorted(scores.keys(),reverse= True)[i]
    print(scores[key],"의 점수는", key, "이고" ,i ,"등 입니다.")
        
#특정 점수 이상 출력 원할때
n_input =input("몇점이상?")

for key in sorted(scores.keys(),reverse= True):
    if key >= float(n_input):
        print(scores[key],"의 점수는", key, "이고" ,i ,"등 입니다.")
        i = i+1
    else:
        i += 1


    



