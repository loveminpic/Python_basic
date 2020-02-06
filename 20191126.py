#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 12:50:52 2019

@author: mac
"""
"""
import pandas as pd

d = [0,1,2,3,4,5,6,7,8,9]

df = pd.DataFrame(d)
print(df)

df.columns = ['Rev']
print(df)

df['NewCol'] = 5
print(df)

df['NewCol'] = df['NewCol'] +1
print(df)

df['test'] = 3
df['col'] = df['Rev']
print(df)
print("======================================================")
print(df.index)

i = ['a','b','c','d','e','f','g','h','i','j']
print("======================================================")
df.index = i
print(df)
print("======================================================")

print(df.loc['a'])

print(df.loc['a':'d'])
print("=========iloc=============================================")
print(df.iloc[0:3])
print("=========Rev============================================")
print(df['Rev'])

print(df[['Rev','test']])

print(df.loc[df.index[0:3], 'Rev' ])
print(df.loc[df.index[5], 'col' ])
print(df.loc[df.index[0:3], ['Rev', 'test']])

print(df.head())
print(df.tail())


"""

import pandas as pd
import numpy as np

d = {'one' : [1,1], 'two' : [2,2]}
i = ['a','b']

df = pd.DataFrame(data = d, index = i)
print(df)

print(df.index)

stack = df.stack()
print(stack)
print(stack.index)

unstack = df.unstack()
print(unstack)

print(unstack.index)

transpose = df.T
print(transpose)


d = {'one' : [1,1,1,1,1], 'two' : [2,2,2,2,2], 'letter' : ['a','a','b','b','c']}

df = pd.DataFrame(data = d)
print(df)

one = df.groupby('letter')
print(one.sum())

letterone = df.groupby(['letter','one']).sum()
print(letterone)


letterone = df.groupby(['letter','one'],as_index = False).sum()
print(letterone)

import pandas as pd
import numpy as np


url = 'https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv'

chipo = pd.read_csv(url,sep = '\t')

print(chipo)

#1.처음부터 10개의 행을 확인해라
print(chipo.head(10))

#2. 데이터 셋에는 몇개의 관측치가 있는가

print(chipo.info())
print(chipo.shape[0])
print(chipo.shape[1])

#3. 열의 이름을 확인해라
print(chipo.columns)

#4. 인텍스를 확인해라. 
print(chipo.index)
"""
1.처음부터 10개의 행을 확인해라
2. 데이터 셋에는 몇개의 관측치가 있는가
3. 열의 이름을 확인해라
4. 인텍스를 확인해라. 
"""


#5. 가장많이 주문한 아이템은 무엇인가.
#6. 가장많이 주문한 아이템은 몇개나 주문했는가?
print('++==============')
chip = chipo.groupby('item_name').sum()
chip = chip.sort_values('quantity', ascending = False)
print(chip.head(1))

#7. choice_description 열에서 가장많이 주문한 아이템
chip1 = chipo.groupby('choice_description').sum()
chip1 = chip1.sort_values('quantity', ascending = False)
print(chip1.head(1))

#8. 총 주문량은 얼마인가?
total_item_orders = chipo.quantity.sum()
print(total_item_orders)

#9. 아이템의 가격은 어떤 타입으로 저장되어 있는가.

print(chipo.item_price.dtype)

#10. 아이템 가격을 부동소수점 타입으로 변경하여 저장하여라.
dollarizer = lambda x : float(x[1:-1])
chipo.item_price = chipo.item_price.apply(dollarizer)
print(chipo.item_price.dtype)

#11. 이 기간 동안에 수익이 얼마인가?
revenue = (chipo.item_price * chipo.quantity).sum()
print('Revenue was : $' + str(np.round(revenue, 2)))


#11 이 기간동안 얼마나 많은 주문자가 있엇나?

orders = chipo.order_id.value_counts().count()
print(orders)

#12. 주문자당 평균 지출 급액
chipo['revenue'] = chipo['quantity'] * chipo['item_price']
order_grouped = chipo.groupby('order_id').sum()

print(order_grouped.revenue.mean())

#13.얼마나 많은 다른 아이템이 팔렸나?

print(chipo.item_name.value_counts().count())

