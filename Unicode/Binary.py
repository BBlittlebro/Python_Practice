blist = [1,2,255]       #only 0 - 255
byte = bytes(blist)
print(byte)

the_bytes = bytes(range(0,256))
print(the_bytes)

a = "stre" + \
    "okok"

print(a)

######################

#struct
print('')
import struct
print(struct.pack('>L', 154))       # Big-endian
print(struct.pack('<L', 154))       # Little-endian

######################

# 沒 magic 了？
# from construct import Struct, Magic, UBInt32, Const, String
# fmt = Struct('png',
#     Magic(b'\x89PNG\r\n\x1a\n'),
#     UBInt32('length'),
#     Const(String('type', 4), b'IHDR'),
#     UBInt32('width'),
#     UBInt32('height')
# )
# data = b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR' + \
#     b'\x00\x00\x00\x9a\x00\x00\x00\x8d\x08\x02\x00\x00\x00\xc0'
# result = fmt.parse(data)
# print(result)

######################

# 12.1
print('')
mystery = '\U0001f984'
import unicodedata
print(mystery, unicodedata.name(mystery))

# 12.2
pop_bytes = mystery.encode('utf-8')
print(pop_bytes)

# 12.3
pop_string = pop_bytes.decode('utf-8')
print(pop_string)

# 12.4
print('')
mammoth = """We have seen the Queen of cheese,
Laying quietly at your ease,
Gently fanned by evening breeze,
Thy fair form no flies dare seize.

All gaily dressed soon you'll go
To the great Provincial Show,
To be admired by many a beau
In the city of Toronto.

Cows numerous as a swarm of bees,
Or as the leaves upon the trees,
It did require to make thee please,
And stand unrivalled Queen of Cheese.

May you not receive a scar as
We have heard that Mr. Harris
Intends to send you off as far as
The great World's show at Paris.

Of the youth -- beware of these,
For some of them might rudely squeeze
And bite your cheek; then songs or glees
We could not sing, oh! Queen of Cheese.

We'rt thou suspended from baloon,
You'd cast a shade, even at noon,
Folks would think it was the moon
About to fall and crush them soon."""
print(mammoth)

# 12.5
print("")
import re
goal = r'\bc\w*'            # r 轉譯\b，\b => 單字開頭 or 結尾，\w => 任何單字字元
print(re.findall(goal, mammoth))

# 12.6
print('')
goal = r'\bc\w{3}\b'          # {指定數量}， 後面加上 \b 代表單字結尾
print(re.findall(goal, mammoth))

# 12.7
print('')
goal = r'\b\w*r\b'
print(re.findall(goal, mammoth))

goal = r'\b\w*l\b'           # 會有錯誤 取得 you'll 的 ll
print('before', re.findall(goal, mammoth))
# 轉譯 \' or 用不同種的引號
goal = r'\b[\w\']*l\b'
print('after', re.findall(goal, mammoth))
goal = r"\b[\w']*l\b"
print('after2', re.findall(goal, mammoth))

# 12.8
print('')
goal = r'\b[^aeiou\s]*[aeiou]{3}[^aeiou\s]*\w*\b'
print(re.findall(goal, mammoth))

# 12.9
print('')
import binascii
code = '47494638396101000100800000000000ffffff21f9' + \
'0401000000002c000000000100010000020144003b'
gif = binascii.unhexlify(code)
print(gif)

# 12.10
print('')
head = b'GIF89a'                # byte 只能跟 byte 比較
print(gif[:6] == head)

# 12.11
print('')
import struct
width, height = struct.unpack('<2H', gif[6:10])     # Little-endian
print(width, height)