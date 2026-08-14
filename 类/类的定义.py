#类的名称：首字母要大写
class Person:
    #当函数被定义在class里面，这个函数就会被称为方法
    #__init__方法：初始化方法（第一个函数必须这样写）
    # 作用：给当前正在创建的instance添加属性
    #init得到的参数：当前正在创建的一个实例对象（self），和其他我们要自定义的参数
    #当我们编写代码去创建Person实例的时候，python会自动调用init的方法
    def __init__(self,name,age,gender):#除了self，还有其他三个自定义的参数
        self.name=name
        self.age=age
        self.gender=gender
        #self的三个属性与后面三个自定义参数关联起来
        #这样就给当前创建的三个实例创建了三个属性
        #可以看出来，self。后面的内容可以和参数名一模一样
        #语法：self.属性名=值


#创建Person类的instance
person0=Person(name='秋',age=18,gender='男')#self就不用写了
person1=Person(name='雨',age=18,gender='女')
#如果直接打印实例，我们看不到实例的属性，只能看到实例的内存地址

#打印写法
print(person0.age,person0.gender)#通过person.语法可以访问实例身上的属性

# 修改实例
person1.name='雨点'
print(person1.name)

#查看所有实例
#实例.__dict__可以查看所有属性
print(person0.__dict__)#会打印出来一个类似字典的东西
print(type(person0.__dict__))#发现这玩意的类型确实是一个字典

#追加属性
#即使我们已经创建好了一个实例，我们仍然可以追加属性
person0.major="AI"#当然追加的属性只有person0可以用，person1不可以
print(person0.major)

#type的另外一种使用方式
#通过type可以溯源查到目标instance是哪个class创建的
print(type(person0))#不出意外应该会输出Person这个类