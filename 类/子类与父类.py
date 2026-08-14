#我们记Person为父类
class Person:
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender

    def speak(self):
        print(f"I'm {self.name},and age is {self.age}.")

#定义它为子类
class Student(Person):#在括号里加个父类，就可以继承它的所有代码,还可以加代码
    def __init__(self,name,age,gender,school):
        super().__init__(name=name,age=age,gender=gender)
        self.school=school

# 如果子类"重写"了某个方法，但还想在子类方法中调用父类版本，可以使用 super().方法名(参数)

#用子类Student来创建实例对象
student=Student('王秋石','18','男性','UQ')
student.speak()#这样子直接就调用了一个方法，而且这个方法本质源于父类Person

#需要注意的是，如果我在Student里面写了个和Person完全不同的一个init方法，那么python不会让它继承Person的init
#其他方法也同理，只要名字相同，就不会继承，而是另起炉灶，也就是“重写”


#下面介绍两种常用方法
print(isinstance(student,Student))#判定某个对象是否为一个类的实例
print(isinstance(student,Person))
#值得注意的是，Person作为父类，student既是Student的实例，也算Person的实例


print(issubclass(Student,Person))#判定这两个类是否为父子关系
