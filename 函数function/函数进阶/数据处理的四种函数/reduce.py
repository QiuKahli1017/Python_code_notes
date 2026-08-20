#reduce可以将一组数据按照一个规则一直进行合并，最终变成单个结果
#格式：reduce(函数，可迭代对象，初始值)
#reduce必须从functools模块里面引用
from functools import reduce

#注意：reduce函数必须传入两个变量，写三个错误

#eg:数列求和
a=[1,2,3,4,5]
sum0=reduce(lambda x,y:x+y,a,0)#如果不写，这里也是0
print(sum0)#会输出a数列里面的所有元素和

#str拼接
a=['ab','cd','ef']
print(reduce(lambda x,y:x+y,a,''))#这里我们需要初始值写成str类型
