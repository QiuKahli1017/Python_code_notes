#以__xxx__格式写的叫做魔法方法
#比如__str__()在object类里面就有，如果我们print就会出来
"""
__str__：调用 print(对象) 或 str(对象) 时触发
__len__：调用 len(对象) 时触发       obj没有len方法
__lt__：执行 对象1 < 对象2 时触发     obj有，但是不允许两个实例对象进行比较，所以要额外写
__gt__：执行 对象1 > 对象2 时触发     和lt一样
__eq__：执行 对象1 == 对象2 时触发  ：
obj有，而且可以对两个对象进行操作，判断依据是内存地址，即使两个对象的属性完全一样，
但内存地址百分百是不同的，所以无论如何都是False，除非写a==a这种傻子判断语句，所以我们还是需要在类里面创建这个方法

__getattr__：访问一个不存在的属性时触发
"""
class Person:
    def __init__(self,gender,age):
        self.gender=gender
        self.age=age
    def __len__(self):
        return len(self.gender)
    def __lt__(self, other):
        return self.age > other.age
    def __gt__(self, other):
        return self.age < other.age
    def __eq__(self, other):
        return self.__dict__ == other.__dict__#判断属性是否一样
    def __getattr__(self, item):#item放入要判断的
        return f"{item}在该实例对象中不存在"


s1=Person('male')
print(s1)#这里它就会对__str__进行调用
#显示出的是“object at 0x0000029D18A37230” 它的内存地址
#说明object类里面自带的__str__方法会打印s1的内存地址


class People:
    def __init__(self,gender):
        self.gender=gender
    #当使用print(实例对象) 或者  str(实例对象) 都会调用__str__（）
    def __str__(self):
        return f"gender:{self.gender}"
s1=People('male')
print(s1)
#str魔法方法的用处：把实例对象变成一个str
#解释一下：当类里面没有__str__魔法方法的时候，他会一直向上查找，一直找到object里面，而object里面的str作用是显示内存地址
#但我们对类创建了一个__str__的时候，它查找到People里面的str就停下来了，不会再找object的
#所以我们这里输出的是我们想输出的东西

