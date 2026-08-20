#不用def去定义的，没名字的函数
#使用lambda去定义
#使用场景：每个函数只使用一次，只用来做小事，匿名函数会很简洁
temp=lambda x:x*x*x#不写return，自动把这个表达式会变成一个return值
#注意必须要接收一下，不然就消失了
temp0=temp(10)
print(temp0)

#没有参数也可以
text=lambda :'This is the text.'
print(text())

#我们也可以在函数调用函数的时候使用匿名函数
def cauculate(function,x,y):
    print(f'{function(x,y)}')
cauculate(lambda x,y:x*y**3,10,3)
#由于第一个要填写的是function类型，为了方便，我们不def新建函数，直接用lambda一步到位

#注意点：
# 只能写一行
#不能写if，while，for，这种代码块,不过条件表达式还是可以写的
#冒号右边必须为表达式
#自动转化为return值