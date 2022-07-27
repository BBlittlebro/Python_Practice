import math
from typing import OrderedDict

print(math.pi)
math.pi = 3.14
print(math.pi)

##################################

#setdefault, defaultdict
table = {'A':1, 'B':2}
a = table.setdefault('C', 3)        # 不存在回傳新值
print(a)
b = table.setdefault('A', 100)      # 存在回傳舊值
print(b)

from collections import defaultdict
def no_idea():
    return 'Huh?'
table2 = defaultdict(no_idea)
table2['A'] = 100
table2['B'] = 99
print(table2['A'])
print(table2['C'])

table3 = defaultdict(lambda: 0)     # 直接用lambda 定義函式
table3['A'] = 50
print(table3['A'])
print(table3['B'])

##################################

# 計數器
food_counter = defaultdict(int)     # 如果不是 defaultdict，要先初始化
foods = ['milk', 'cookie', 'milk', 'milk']
for food in foods:
    food_counter[food] += 1

for food, num in food_counter.items():
    print(food, num)

# Counter
from collections import Counter
breakfast = ['spam', 'spam', 'eggs', 'spam']
breakfast_counter = Counter(breakfast)
print(breakfast_counter)
print(breakfast_counter.most_common())      
print(breakfast_counter.most_common(1))         # 降冪排序，引數回傳前幾筆資料

lunch = ['eggs', 'eggs', 'bacon']
lunch_counter = Counter(lunch)
print(lunch_counter)

print("+: ", breakfast_counter + lunch_counter) # 用法跟集合一樣
print("-: ", breakfast_counter - lunch_counter)
print("&: ", breakfast_counter & lunch_counter)
print("|: ", breakfast_counter | lunch_counter) #跟加法不同，選出最多的群組

##################################

# Stack + Queue = deque
def palindrome(word):
    from collections import deque
    de = deque(word)
    while len(de) > 1:
        if de.popleft() != de.pop():
            return False
    return True

print(palindrome("abcdcba"))

##################################

# pprint
from pprint import pprint
quotes = OrderedDict([('A', 1), ('B', 2), ('C', 3)])
print(quotes)
pprint(quotes)

from random import randrange
print(range(10))
b = randrange(10)
print(b)

##################################

#11.1
import zoo
zoo.hours()

#11.2
import zoo as menagerie
menagerie.hours()

#11.3
from zoo import hours
hours()

#11.4
from zoo import hours as info
info()

#11.5
plain = {'A':1, 'B':2, 'C':3}
print(plain)

#11.6
fancy = OrderedDict({'A':1, 'B':2, 'C':3})
print(fancy)

#11.7
from collections import defaultdict
dict_of_list = defaultdict(list)
#dict_of_list = {}
dict_of_list['a'].append("something for a")
dict_of_list['a'].append("something for a2")
print(dict_of_list)