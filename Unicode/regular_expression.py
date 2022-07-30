import re
source = "Hello World"
ob = re.match("He", source)     # 找開頭
if ob:
    print(ob.group())

ob = re.match("^He", source)
if ob:
    print(ob.group())

if ob := re.match(".*World", source):   # 我是海象
    print(ob.group())

if ob := re.search("World", source):    # 第一個找到的
    print(ob.group())

if ob := re.findall("o", source):
    print(ob)
if ob := re.findall(".o", source):      # o 前面有一個字
    print(ob)

##################################

import string
printable = string.printable
print(printable[:50])
print(printable[50:])                   # 後面很多換行、空白符號

print(re.findall('\d', printable))
print(re.findall('\w', printable))
print(re.findall('\s', printable))      # 空格、tab、換行、回車、垂直tab、跳頁

x = 'abc' + '+-/' + '\u00ea' + '\u0115'
print(re.findall('\w', x))

##################################

# anchor(錨點)使用
print('')
source = """I wish I may, I wish I might
Have a dish of fish tonight!"""
print(re.findall('wish', source))
print(re.findall('wish|fish', source))
print(re.findall('^wish', source))          # 找開頭
print(re.findall('^I wish', source))
print(re.findall('fish$', source))          # 找結尾  
print(re.findall('fish tonight.$', source)) # 找結尾的任何字元，不是真的找句點
print(re.findall('fish tonight\.$', source))
print(re.findall('[wf]ish', source))        # 找 w|f + ish
print(re.findall('[wsh]+', source))         # 找一個或多個 w、s、h
print(re.findall('ght\W', source))          # ght開頭，後面接非英數字元
print(re.findall('I (?=wish)', source))     # wish 之前的 I
print(re.findall('(?<=I) wish', source))    # I 之後的 wish
print(re.findall('\bfish', source))         # 被當作是 Python 的轉義字元(backspace)
print(re.findall(r'\bfish', source))        # 前方加上 r 停用轉義

##################################

# 指定 match 輸出
print('')
m = re.search(r'(. dish\b).*(\bfish)', source)
print(m.group())
print(m.groups())

# 比對橘色的 expr，匹配的放入藍色群組中
m = re.search(r'(?P<DISH>. dish\b).*(?P<FISH>\bfish)', source)
print(m.group())
print(m.groups())
print(m.group('DISH'))
print(m.group('FISH'))