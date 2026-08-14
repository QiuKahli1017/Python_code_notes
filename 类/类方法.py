class Person:
    max_num=13
    def __init__(self,name,age,gender):#实例方法
        self.name=name
        self.age=age
        self.gender=gender

    #类方法收到的参数：1.类本身 2.自定义参数

    #类方法通常用来实现与类相关的逻辑.可以操作类级别的信息比如类属性
    #意思是，即使是类属性，也可以通过类方法进行修改，这个很重要

    #类保存在类里面，实例方法保存在实例里面
    @classmethod#装饰器，用来装饰下一行的函数，让它变成类方法
    def test1(cls,data):#因为是“类”方法，所以括号里面写的不是self
        print('Test1',data)
        print(Person.max_num)#调用Person类里面的max num参数
    #由于我们收到了cls参数，所以我们可以以此访问类属性
    @classmethod
    def change_max(cls,data):
        Person.max_num=data

    #类的工厂方法
    @classmethod
    def create(cls,name,age,gender):
        #下面演示如何创建并返回一个实例对象
        return cls(name,age,gender)



print(Person.__dict__)
#我们输出里面有test1

#所以，方法需要用类来调用，而不是实例
Person.test1(data=30)

#我们验证一下类方法是否可以改变类属性
Person.change_max(30)
print(Person.max_num)#发现从13变成了30

#工厂方法：通过类方法进行生成实例对象

temp=Person.create('秋石','18','男性')
print(temp.name,
      temp.age,
      temp.gender)