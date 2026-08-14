from datetime import datetime
class Person:
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender

    #静态方法的装饰器
    @staticmethod
    def is_adult(age):#静态方法不接受cls,也不接受self
        return int(age)>=18

    @staticmethod
    def id_card(id):
        return id[0:6]+'******'+id[11:18]

#调用静态方法需要用到类
print(Person.id_card('34120220081017431X'))
