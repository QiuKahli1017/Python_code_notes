#同一个方法名，在不同方法调用的时候，会呈现不同行为
class Animal:
    def __init__(self):
        pass
    def sound(self):
        print("动物动物叫叫叫")

class Dog(Animal):
    def sound(self):
        print('大狗大狗叫叫叫')

def make_sound(animal:Animal):
    # 类型注解：这个形参我希望（不是强制）是animal类型,我写str/int/bool/dict/list 都可以
    # 而类Animal是一种我们自定义的数据类型，所有用Animal创建的实例对象都是Animal类型的
    # 为了实现多态的使用，我们要写父类类型
    animal.sound()#看上面，每个Animal类型里面都有个叫Sound的方法
a1=Animal()
d1=Dog()
#注意，如果B是A的子类，用B创建的实例对象，是A类型也是B类型

make_sound(a1)
make_sound(d1)#由于a1和d1都是属于Animal这个父类的，所以都可以使用