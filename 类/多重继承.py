#其实，在python里面，一个子类可以有好多个父类，我们称之为多重继承
class Person:
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender

class Location:
    def __init__(self,street,city):
        self.street=street
        self.city=city

class Student(Person,Location):
    def __init__(self,name,age,gender,street,city):
        #当我们要调用多个父类的方法时，就不能使用super方法了
        Person.__init__(self,name,age,gender)
        Location.__init__(self,street,city)
        #要用父类.方法名（self,其他参数） 的方式来对父类方法进行调用

Me=Student('Qiushi','18','male','Nanjing Road','Shanghai')
print(Me.__dict__)

#类型有一个特殊的属性叫做：__mro__  用于记录属性和方法查找顺序，让我们跟清楚调用的前因后果
print(Student.__mro__)#注意，这个东西只能对类进行调用