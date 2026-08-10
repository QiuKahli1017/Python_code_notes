a={1,2,3,4}
b={1,3,4,5}
#difference,找出a不同于b的元素，返回值是一个集合
print(a.difference(b))

#difference_update,作用，从a中，删除b中存在的元素（a会被修改，b不变）
a.difference_update(b)#他们都有134，所以a只剩下2
print(a)
#二者原理基本相同，不过一个return，一个不return;一个作删除操作，一个不动

a={1,2,3,4}
b={1,3,4,5}
#union,合并a和b，但a b 都不变，会return一个新的集合
c=a.union(b)
print(c)

#is sub set:判断a是否是b的子集（与数学中判断方法相同）,return一个布尔值
print(a.issubset(b))#很显然会return False
#is super set:判断a是否是b的母集
a={1,2,3,4,5}
b={1,2,3}
print(a.issuperset(b))#很显然是True
#is dis joint判断a与b有没有交集，return 一个布尔值
#还是跟数学一样，我就不写了
