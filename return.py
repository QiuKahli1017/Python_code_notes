#在函数中，执行了return语句后，后面的一概不运行
def f(x):
    return x*x
    print(x)
print(f(3))#发现不会打印x的值