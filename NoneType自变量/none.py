#None是一个特殊自变量，表示空值无意义
msg=None#相当于先定义着，但我们不使用它，不暗示类型，
#类型是Nonetype，该数据类型有且只有一个None
#如果我们不给函数设置返回值，那么函数自动返回一个None
def f(x):
    print(1)

print(type(f(3)))#发现类型是NoneType