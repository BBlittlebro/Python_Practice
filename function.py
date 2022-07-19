
def square_it(func):
    def new_function(*args, **kwargs):
        result = func(*args, **kwargs)
        return result * result
    return new_function



# short_list = [1,2,3]
# while True:
#     value = input("Position: ,[q to Quit]")
#     if value == 'q':
#         break
#     try:
#         position = int(value)
#         print(short_list[position])
#     except IndexError as err:
#         print('Bad index:', position)
#     except Exception as other:
#         print('Something else error:', other)

# try:
#     raise IndexError('nice!')
# except IndexError as bb:
#     print(bb)

def good():
    return ['Harry', 'Ron', 'Hermione']

print(good())

def get_odds():
    for i in range(1,10,2):
        yield i

count = 1
for number in get_odds():
    if count == 3:
        print(number)
        break
    count += 1

def test(func):
    def new_function(*arg, **kgarg):
        print('start')
        a = func(*arg, **kgarg)
        print('end')
        return a
    return new_function

@test
def add_int(a,b):
    print('Doing...')
    return a + b

print(add_int(3,5))

class OopsException(Exception):
    print('nice')

try:
    raise OopsException()
except OopsException:
    print('Caught an oops')
