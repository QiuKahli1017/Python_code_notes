#用简洁语句，从可迭代对象中，生成新对象的语法结构
#实际上是for循环+append的一种简便写法
#语法格式：[表达式 for 变量 in 可迭代对象]

#列表推导式
scores=[i**2 for i in range(0,10)]
print(scores)

#字典推导式
names=['张三','李四','王五']
scores=[21,43,74]
result0={names[i]:scores[i] for i in range(len(names))}
print(result0)

#集合推导式
names=['张三','李四','王五']
names_set={name+'!' for name in names}#别忘记了集合用花括号
print(names_set)