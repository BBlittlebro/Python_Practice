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