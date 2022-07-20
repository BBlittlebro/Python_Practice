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
