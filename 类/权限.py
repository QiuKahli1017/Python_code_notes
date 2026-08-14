class Person:
    def __init__(self,name,age,gender):
        self.name=name#任何地方都可以访问
        # 在age前面加一个下划线，给他加上上权限
        self._age=age#只能在这个类和子类里面可以访问，类的外部不可以访问
        #加上两个下划线变成一个私有属性
        self.__gender=gender#只能在这个类中访问，子类访问不了
class Student(Person):
    def out(self):
        return self.__gender
p1=Student('Q',19,'male')
p1.out()