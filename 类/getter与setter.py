class Person:
    def __init__(self,gender):
        self._gender=gender
    #property装饰器包含setter和getter
    #要调用getter直接写property就行，但setter需要写： 要修改的属性名字.setter
    #注意：getter可以没有setter，但setter必须要前面有getter！！！！！
    @property
    def gender(self):
        return self._gender
    #前面用了才可以更改
    @gender.setter
    def gender(self,value):
        self._gender=value
p1=Person("male")
print(p1.gender)#自动调用读取方法：getter
#如果不加property这个装饰器，我们就要写gender（），感觉很奇怪

#调用setter
p1.gender='Female'#调用gender对应的setter
print(p1.gender)