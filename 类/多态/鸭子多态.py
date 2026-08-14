#如果一个东西看起来像鸭子，叫起来也像鸭子，那么他就是鸭子
#鸭子类型是一种“编程风格”,只关注对象能否做某件事

#这俩都不作为Animal子类
class Dog:
    def sound(self):
        print('大狗大狗叫叫叫')

class Duck:
    def sound(self):
        print('小鸭小鸭嘎嘎嘎')

def make_sound(animal):#我们不进行任何类型限制
    animal.sound()

dog=Dog()
duck=Duck()
make_sound(dog)
make_sound(duck)