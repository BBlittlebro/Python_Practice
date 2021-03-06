from ast import And
from turtle import circle


class Cat:
    def __init__(self, name):
        self.name = name

number1 = Cat('Andy')
print(number1.name)

##################################

class Car:
    def exclaim(self):
        print('I am a car.')

class Toyota(Car):
    def exclaim(self):
        print('I am a car in Toyota!')
    def run(self):
        print('MAX POWER!!!!!')

car1 = Car()
car2 = Toyota()
car1.exclaim()
car2.exclaim()
#car1.run()         只有子類別有
car2.run()

##################################

class Person:
    def __init__(self, name):
        self.name = name
    def says(self):
        print("HAhaha...")

class Student(Person):
    def __init__(self, name):
        self.name = 'student:' + name

class Teacher(Person):
    def __init__(self, name):
        self.name = name + ' teacher'

person = Person('Andy')
student = Student('Andy')
teacher = Teacher('Andy')
print(person.name)
print(student.name)
print(teacher.name)

##################################

class EmailPerson(Person):
    def __init__(self, name, email):
        super().__init__(name)
        self.email = email
emailperson1 = EmailPerson('Bob', 'Bob123@gmail.com')
print(emailperson1.name)
print(emailperson1.email)
emailperson1.says()

##################################

class PrettyMixin:
    def dump(self):
        import pprint
        pprint.pprint(vars(self))

class Thing(PrettyMixin):
    pass

thing1 = Thing()
thing1.name = 'OMG'
thing1.sex = 'Male'
thing1.age = 25
thing1.dump()

##################################
#法一：

class Duck():
    def __init__(self, input_name):
        self.hidden_name = input_name
    def get_name(self):
        print('inside the getter!')
        return self.hidden_name
    def set_name(self, input_name):
        print('inside the setter!')
        self.hidden_name = input_name
    name = property(get_name, set_name)

gua = Duck('Cute_Duck')
print(gua.name)
gua.name = 'BBQ_Duck'
print(gua.name)

#法二：

class Duck2():
    def __init__(self, input_name):
        self.hidden_name = input_name
    @property       #設定屬性
    def name(self):
        print('inside the getter2!')
        return self.hidden_name
    @name.setter
    def name(self, input_name):
        print('inside the setter2!')
        self.hidden_name = input_name

gua2 = Duck2('Cute_Duck')
print(gua2.name)
gua2.name = 'BBQ_Duck'
print(gua2.name)

#法二(隱藏屬性)：

class Duck3():
    def __init__(self, input_name):
        self.__name = input_name
    @property       #設定屬性
    def name(self):
        print('inside the getter3!')
        return self.__name
    @name.setter
    def name(self, input_name):
        print('inside the setter3!')
        self.__name = input_name

gua3 = Duck3('Cute_Duck')
print(gua3.name)
gua3.name = 'BBQ_Duck'
print(gua3.name)
#print(gua3.__name)     => 存取不到，被隱藏起來
print('I find you! ' + gua3._Duck3__name)   # => 被修飾過後的真正名字

##################################

class Circle():
    def __init__(self, radius):
        self.radius = radius
    @property
    def diameter(self):
        return 2 * self.radius

c = Circle(5)
print(c.radius)
print(c.diameter)
c.radius = 7
#c.diameter = 14      => error
print(c.diameter)

##################################
# 類別方法
class A():
    count = 0
    def __init__(self):
        A.count += 1
    def exclaim(self):
        print('I am an A!')
    @classmethod
    def kids(cls):
        print('A has', cls.count, 'little objects.')    # cls.count => A.count

A1 = A()
A2 = A()
A3 = A()

A.kids()

# 靜態方法
class Hello():
    @staticmethod
    def say():
        print("hello world!")

Hello.say()         # => 不用建立物件可以直接使用

##################################

# 鴨子定型、多型
class Quote():
    def __init__(self, name, words):
        self.name = name
        self.words = words
    def who(self):
        return self.name
    def says(self):
        return self.words + '.'

# 沒有要改函式，不用 super 父類別，直接自動呼叫就好
class QuestionQuote(Quote):
    def says(self):
        return self.words + '?'

class ExclamationQuote(Quote):
    def says(self):
        return self.words + '!'

hunter = Quote('Hunter1', "I'm hunting rabbits")
hunter2 = QuestionQuote('Hunter2', "What's up, doc")
hunter3 = ExclamationQuote('Hunter3', "It's rabbit season")
print(hunter.who(), 'says:', hunter.says())
print(hunter2.who(), 'says:', hunter2.says())
print(hunter3.who(), 'says:', hunter3.says())
print("\nDuck Typing")

# 跟上面毫無關係，但看起來一樣 => 鴨子定型
class FakeDuck():
    def who(self):
        return "FakeDuck"
    def says(self):
        return "I'm fake."
fake = FakeDuck()
print(fake.who(), "says:", fake.says())

##################################

# 魔術方法
class Word():
    def __init__(self, text):
        self.text = text
    def __eq__(self, word2):
        return self.text.lower() == word2.text.lower()
    def __str__(self):
        return self.text
    def __repr__(self):
        return "My word is " + self.text + "."

first = Word('Ha')
second = Word('ha')
print(first == second)
first           # 使用 __repr__
print(first)    # 使用 __str__，沒寫會用__repr__

##################################

# 聚合與組合
class Bill():
    def __init__(self, description):
        self.description = description
class Tail():
    def __init__(self, length):
        self.length = length
class Cat():
    def __init__(self, bill, tail):
        self.bill = bill
        self.tail = tail
    def about(self):
        print("This cat has", self.bill.description, "bill and a",
        self.tail.length, "tail.")
a_bill = Bill("wide orange")
a_tail = Tail("long long")
cat = Cat(a_bill, a_tail)
cat.about()

# 具名 tuple (名稱、欄位名稱字串)
from collections import namedtuple
New_cat = namedtuple('New_cat', 'bill tail')   
ncat = New_cat("wide orange", "long long")
print(ncat)
print(ncat.bill)
print(ncat.tail)

# 用字典製作具名 tuple
New_cat2 = namedtuple('New_cat2', 'bill tail')
parts = {'bill':'wide orange', "tail":"long long"}
cat2 = New_cat2(**parts)
print(cat2)

cat3 = cat2._replace(bill = 'small black')
print(cat3)

##################################

# dataclass
from dataclasses import dataclass
@dataclass
class AndyDataClass:
    name: str
    sex: str
    age: int = 0
andy = AndyDataClass('Handsome Boy', 'Male', 22)
BB = AndyDataClass('Cool Boy', 'Female')
print(andy)
print(andy.name)
print(BB)

##################################

# 10.1
class Thing():
    pass
print(Thing)
thing = Thing()
print(thing)

#10.2
class Thing2():
    letters = 'abc'
print(Thing2.letters)

#10.3
class Thing3():             #letters 屬於用 Thing3 製造的物件，而不是類別本身
    def __init__(self):
        self.letters = 'xyz'
thing3 = Thing3()
print(thing3.letters)

#10.4
class Element():
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number
    def dump(self):
        print(self.name, self.symbol, self.number)
element = Element("Hydrogen", "H", 1)

#10.5
dict1 = {"name":"Hydrogen", "symbol":"H", "number":1}
hydrogen = Element(**dict1)     #kwarg 要符合類別引數
print(hydrogen.name)

#10.6
hydrogen = Element(**dict1)
hydrogen.dump()

#10.7
print(hydrogen)
class Element():
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number
    def __str__(self):          #print()
        return ("%s %s %s" % (self.name, self.symbol, self.number))
hydrogen = Element(**dict1)
print(hydrogen)

#10.8
class Element():
    def __init__(self, name, symbol, number):
        self.__name = name
        self.__symbol = symbol
        self.__number = number
    def __str__(self):          #print()
        return ("%s %s %s" % (self.__name, self.__symbol, self.__number))
    @property
    def name(self):
        return self.__name
    @property
    def symbol(self):
        return self.__symbol
    @property
    def number(self):
        return self.__number
    
hydrogen = Element(**dict1)
print(hydrogen.name, hydrogen.symbol, hydrogen.number)

#10.9
class Bear():
    def eats(self):
        return 'berries'
class Rabbit():
    def eats(self):
        return 'clover'
class Octothorpe():
    def eats(self):
        return 'campers'
bear = Bear()
rabbit = Rabbit()
octothorpe = Octothorpe()
print(bear.eats(), rabbit.eats(), octothorpe.eats())

#10.10
class Laser():
    def does(self):
        return "disintegrate"
class Claw():
    def does(delf):
        return "crush"
class SmartPhone():
    def does(self):
        return "ring"

class Robot():
    def __init__(self):
        self.laser = Laser()
        self.claw = Claw()
        self.smartphone = SmartPhone()
    def does(self):
        return ("""Laser can %s\nClaw can %s\nSmartPhone can %s""" % 
        (self.laser.does(), self.claw.does(), self.smartphone.does()))
robot = Robot()
print(robot.does())