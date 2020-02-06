#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 12:37:29 2019

@author: mac
"""
#
result_f = open("scores_list.txt",'r')
for line in result_f:
    print(line.strip())
result_f.close()

try:
    result_f = open("no_file.txt")
except:
    print("해당하는 파일이 없습니다.")

#점수들 프린트 하기
result_f = open("scores_list.txt",'r')
for line in result_f:
    record = line.split()
    print(record[1])
result_f.close()

#일등찾는법========================================

result_f = open("scores_list.txt",'r')
highest_score = 0
second_highest_score = 0
third_highest_score = 0

for line in result_f:
    record = line.split()
    try:
        score = float(record[1])
    except:
        continue # 첫줄에 score값은 수치로 변환이 안되서 그냥 예외처리!
    if highest_score < score:
        third_highest_score = second_highest_score
        second_highest_score - highest_score
        highest_score = score
        
    elif second_highest_score < score:
        second_highest_score = score
    elif third_highest_score < score:
        third_highest_score = score
    else:
        continue
    
result_f.close()
print("1등의 점수", highest_score)
print("2등의 점수", second_highest_score)
print("3등의 점수", third_highest_score)
#=====================================================

result_f = open("scores_list.txt",'r')
score_list = [] #공리스트 만든느 법

for line in result_f:
    name, score = line.split()
    try:
        score_list.append(float(score))
    except:
        continue
result_f.close()
print(score_list)  #여기까지 리스트에 담는법

#이제 list 정렬하는법!

score_list.sort()
print(score_list)
score_list.reverse()
print(score_list)
print("1등의 점수는", score_list[0])
print("2등의 점수는", score_list[2])

def ranking(rank):
    result_f = open("scores_list.txt",'r')
    score_list = [] #공리스트 만든느 법
    for line in result_f:
        name, score = line.split()
        try:
            score_list.append(float(score))
        except:
            continue
        result_f.close()
        score_list.sort()
        score_list.reverse()
        return score_list[rank-1]

print(ranking(1))



#======================================================

print([1,2,3] + [4,5])
print([1,2,3] *3)

#1. 공리스트 
empty_list = [] 

#2. 리스트의 길이
print(len(empty_list))

#3. 리스트 안에 리스트! 갯수는 1이 나옴
a_sinflenton=[[]]
print(len(a_sinflenton))

a_list = [1,2,[3,4],[[5,6,7],8]]
print(len(a_list))

# 1) a_list 에서 2를 찾는법
print(a_list[1])
# 2) a_list 에서 [3,4]를 찾는법
print(a_list[2])
# 3) a_list 에서 3 를 찾는법
print(a_list[2][0])
# 4) a_list 에서 4 를 찾는법
print(a_list[2][1])
# 5) a_list 에서 7 를 찾는법
print(a_list[3][0][2])


#========================================================


animals = ['dog', 'cat', 'pig']

animals.append('coq')
print(animals)
animals.append(['eagle','bear'])
print(animals)
animals.remove(['eagle','bear'])
print(animals)
animals.extend(['eagle', 'bear'])
print(animals)
animals[1] = 'cow' #cat을 cow로 바꿈
print(animals)
print(animals[1:4])
animals[1:2] = ['tiger','lion','rabbit']
print(animals)
animals[1:2] = [] #tiger 사라짐
print(animals)

print(animals.index('pig')) #인덱스 번호 알려줌.

animals.pop(3) #인덱스가 3인게 사라짐.
print(animals)
animals.pop() #맨뒤가 사라짐
print(animals)
print(animals.pop())

del animals[-1] #맨마지막 꺼 지워줌

animals.insert(1,'leopard') # insert(어디 위치에, 어떤거를.)

print(animals)
print(animals.count('leopard')) #레오파드가 몇게 들어가 있는지 확인하는것. 







