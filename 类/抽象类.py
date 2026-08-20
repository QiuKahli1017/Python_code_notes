from abc import  ABC,abstractmethod
#不能直接实例化的类，通常作为规范，被子类继承，让子类创建并实现抽象方法
#Person类如果继承了ABC这个类，他就是抽象类

class Person(ABC):#让Person继承ABC
    @abstractmethod#用“抽象方法”装饰器修饰这个方法，让他变成抽象方法
    def speak(self):
        pass#啥都没有，够抽象
    #目的就是告诉下面，我们需要实现speak这个方法，但我在Person这个方法里面不会实现


class Word(Person):#由于Word继承了Person里面的抽象方法，所以我们要在这里实现它
    def __init__(self,name):
        self.name=name
    def speak(self):
        print(f"I'm {self.name}")
