class Person:
    def __init__(self,name,age,gender):#除了self，还有其他三个自定义的参数
        self.name=name
        self.age=age
        self.gender=gender
    #自定义方法（给实例添加其他的行为）
    def speak(self,word):#speak方法收到的参数：1.实例对象（self) 2.其他函数
        print(f"我叫{self.name},我想说{word}")
        #不难看出，如果要在其他方法里面调用参数，比如用初始化方法里面的name，就不能直接这样写


person0=Person('阿秋',18,'男性')
Person.speak(person0,'早上好')
