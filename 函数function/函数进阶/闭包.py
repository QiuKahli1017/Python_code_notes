#Q什么是闭包？
#A内层函数(inner)+被内层函数所引用的外层变量(inner.__closure__)

#闭包产生条件：1.有嵌套函数  2.内层访问了外层里面的变量 3.外层函数是高级函数————返回内容是内层变量

#易错点：多个闭包之间是相互不影响的
#a=outer()
#b=outer()
#这俩互不影响

#a=outer()
#b=a
#这俩会互相影响


from hexid import hexid
def outer():
    num=10
    def inner():
        nonlocal num
        num+=1
        return num
    return inner
a=outer()
print(a())
print(a())
print(a())
#这个外部作用域的num还可以进行修改

#打印closure元组
print(a.__closure__)
#closure元组0是cell at 0x000001F89E9392D0: int object at 0x00007FF99E3FC5F8，
#closure[1]是空白字符串

#打印closure元组里面的具体值，我只想要num本身
print(a.__closure__[0].cell_contents)#num的调用

#结论：
#1.发现本应该被删除的num,由于inner使用，会被封存到闭包单元（cell）身上
#2.这些cell会组成一个__closure__元组，放在inner函数内


print('---------------------------------------')
print('下面是第二类测试')



from hexid import hexid
def outer():
    num1=10
    num2=20
    def inner():
        nonlocal num1
        num1+=1
        return num1,num2
    return inner
a=outer()
print(a())
print(a())

print(a.__closure__)
print('我们可以看到，由于我们写了两个num，所以closure元组现在变成了两个元素，分别调用就要使用不同的下标')
print(a.__closure__[0].cell_contents)
print('num的地址: ',hexid(a.__closure__[0].cell_contents))
print(a.__closure__[1].cell_contents)
print('num1的地址:',hexid(a.__closure__[1].cell_contents))


