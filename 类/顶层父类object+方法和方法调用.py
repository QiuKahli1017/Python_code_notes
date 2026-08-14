"""
__str__()
__repr__()
__eq__()
__hash__()
__getattribute__()
"""
class Person:
    pass
#即使我们在Person这个类里面啥都不写，Person也会从object类里面继承了上面的这些魔法方法

print(isinstance(Person,object))#输出True说明他们存在父子关系

#查看关系
print(Person.mro())

# 对象.方法      -> 不加括号，不会执行方法，而是获取“方法对象”本身
# 对象.方法()    -> 加括号，才会真正调用方法，结果类型取决于 return 返回什么

# @property 会把一个方法包装成“属性”
# 所以原本需要写 对象.方法()，加了 @property 后可以写成 对象.属性
# property 最终得到的值和类型，取决于这个 getter 方法 return 了什么

# 例如：
# p.get_age      -> method 类型
# p.get_age()    -> 执行方法，类型由 return 决定
# p.age          -> 如果 age 是 property，会自动执行 getter，类型由 return 决定