#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 09:41:38 2019

@author: mac

"""

def record_getter(filename):
   
        #지정된 학생의 정보를 리스트에 담아 리턴
        #각 항목은 학목명과 내용의 튜플로 구성됨
   
    std_data = {}
    a_file = open(filename)
    for line in a_file.readlines():
        if line[0] == '#' or line in string.whitespace:
            continue
        else:
            item, value = line.split(":")
            item = item.strip()
            value = value.strip()
            if item == 'Date_of_birth':
                value = date_of_birth(value)
   
            std_data[item] = value
           
    return std_data

print(record_getter('Students_Records/Byun_Sato.txt'))

"""
#변사또의 전공이 무엇인지 알아보는 코드
"""
Byun_Data = record_getter('Students_Records/Byun_Sato.txt')
print(Byun_Data['Department'])


import glob

def std_record_list(dir):
    file = glob.glob(dir + '/*.txt')
    return sorted(files)

filenames = print(std_record_list('Students_Records')

all_records = []

for file in filenames:
    data= record_getter(file)
    all_records.append(data)
print(all_records)

print(all_records[2]['Department'])
print(all_records[0]['Name'])

"""
문제1. 첫번째 학생의 신상 정보를 아래의 형식으로 출력하는 코드를 작성하세요.
제이름은 .. 이고 나이는 ... 살입니다.
"""
print("제 이름은", all_records[0]['Name'],"이고, 나이는",2020 - all_records[0]['Date of Birth'][0])



#문제2 전공이 컴퓨터인 학생 ㄹ이름의 리스트를 구현

#문제3 전공을 인자로 입력하면, 해당 전공학생들이름으로 구성된 리스티를 리턴하는 함수. 