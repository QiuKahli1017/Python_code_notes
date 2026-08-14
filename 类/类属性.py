class Person:
    #类属性就是在初始化方法前面写到的属性
    #类属性可以用类访问，也可以用实例访问
    max_age=120
    #当然，类属性是可以在下面这些方法里面使用的
    def __init__(self,name,age,gender):#除了self，还有其他三个自定义的参数
        if age<=Person.max_age:
            self.name = name
        else:
            print('年龄输入错误')
            age=120
        self.age=age
        self.gender=gender

person=Person('秋石',age=130,gender="male")
print(person.__dict__)


#值得一提，类属性保存在类的身上
print(Person.__dict__)
#验证一下，类属性不是保存在实力上
print(person.__dict__)


#注意点，对于实例的属性进行修改的时候，根本不会修改类属性
p1=Person(name='秋石',age=18,gender="male")
p1.max_age=140
print(p1.__dict__)#发现max_age变了，说明这个"p1.max_age=140"语句不能全局影响
print(Person.max_age)#发现Person这个类的属性还是不变