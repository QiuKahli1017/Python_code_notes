#函数range()的使用方法
list0=list(range(0,8))
print(list0)
list0=list(range(8))#函数range（a,b）返回的值是从a到b-1
print(list0)
#如果a不写，我们默认a=0
list0=list(range(-1,8))
print(list0)

#在循环中我们也常常用
for i in range(8):
    print(i)
