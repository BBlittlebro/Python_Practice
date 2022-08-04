def unicode_test(value):
    import unicodedata
    name = unicodedata.name(value)
    value2 = unicodedata.lookup(name)
    print("value:'%s', name:'%s', value2:'%s'" % (value, name, value2))

unicode_test('A')
unicode_test('$')
unicode_test('\u00a2')
unicode_test('\u20ac')
unicode_test('\u2603')

u_umlaut = '\N{LATIN SMALL LETTER U WITH DIAERESIS}'    #用名字指定字串
drink = 'Gew' + u_umlaut + 'rztraminer'
print(drink)

######################

# encode
snowman = '\u2603'
print(len(snowman))     # 1
ds = snowman.encode('utf-8')
print(len(ds))          # 3
print(ds)
ds = snowman.encode('ascii', 'replace')     # 後面可以加上不同方式去處理無法編碼狀況
print(ds)

# decode
place = 'caf\u00e9'     #type = 'str'
place_bytes = place.encode('utf-8')     #type = 'bytes'
place2 = place_bytes.decode('utf-8')
print(place2)
place3 = place_bytes.decode('latin-1')
print(place3)

######################

import html
import imp
place = 'caf\u00e9' 
byte_value = place.encode('ascii', 'xmlcharrefreplace')
print(byte_value)
print(byte_value.decode())
print(html.unescape(byte_value.decode()))

######################

eacute1 = 'é'
eacute2 = '\u00e9'
eacute3 = '\N{LATIN SMALL LETTER E WITH ACUTE}'
eacute4 = chr(233)
eacute5 = chr(0xe9)
print(len(eacute1))
print(eacute1,eacute2,eacute3,eacute4,eacute5)
print(eacute1 == eacute2 == eacute3 == eacute4 == eacute5)

print("\nAfter combining:")
eacute_combined1 = "e\u0301"
eacute_combined2 = "e\N{COMBINING ACUTE ACCENT}"
eacute_combined3 = "e" + "\u0301"
print(eacute_combined1, eacute_combined2, eacute_combined3)
print(len(eacute_combined1))    # 用兩個字元建立一個 Unicode
print(eacute1 == eacute_combined1)      #雖然長一樣，但本質不太一樣

print("\nAfter normalized:")
import unicodedata
eacute_normalized = unicodedata.normalize('NFC', eacute_combined1)
print(len(eacute_normalized))
print(eacute_normalized == eacute1)
print(unicodedata.name(eacute_normalized))