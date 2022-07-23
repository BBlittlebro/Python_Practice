import math

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