def caculate(x,y):
    res=x*y
    res1=x/y
    return res,res1
#接受方法1
result0=caculate(30,10)
print(result0)#(300,3)
print(type(result0))#输出的类型是元组

#接受方法2
result1,result2=caculate(30,10)
print(result1,result2)


#参数打包
#*args将位置参数打包起来变成一个元组
#**kwargs将关键字参数打包起来变成一个字典
#写法
def f(*args,**kwargs):
    #星号只需要在f括号里面写就行了，下面调用不需要使用
    print(args)
    print(kwargs)

#参数解包
num=(1,2,3,4,5)
dict0={
    'name':1,
    'tuple':3,
    'temp':5
}
#上面我创建了一个元组和一个字典
#如果一个一个写入很麻烦，所以我们这样写入函数


#二者同时使用
f(*num,**dict0)#这样子Python会自动把元组拆开，把字典拆开