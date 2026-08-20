# 一、输入与输出
# print()      ==> 输出指定内容
#print完全体:print(内容，sep=" ",end=xxx,file=xxx,flush=True/False)
# sep:分隔符
# file:输出位置，默认输出在控制台上面，也可以让他输出到外部的一个文件上面
# flush:是否立即刷新,如果False，就不会进行缓存

import time
#第一种
# time.sleep(1)#我们写睡眠函数，可以实现一个输出暂停1秒的效果，从而打造一个进度条效果
# for i in range(10):
#     print('-', end='-')
#     time.sleep(1)

#第二种
#转义字符
# for i in range(101):
#     print(f'\r已加载{i}%',end=' ')#这里的\r就是转义字符，作用是回到本行开头并且覆盖{}里面输出过的内容,
#                                 # 如果你end不写，他就会换行，导致\r没有用
#     time.sleep(0.1)


# input()      ==> 获取用户输入


# 二、类型转换
# int()        ==> 转为整数
# float()      ==> 转为浮点数
# str()        ==> 转为字符串
# bool()       ==> 转为布尔值
# list()       ==> 转为列表
# tuple()      ==> 转为元组
# set()        ==> 转为集合
# dict()       ==> 转为字典
# frozenset() 转为不可变集合


# 三、数学及数据处理相关
# abs()        ==> 取绝对值

# round()      ==> 四舍五入
#语法：round(数字，要保留几位)
#注意这里是小于五会舍，大于五会入，等于5看奇偶性（奇入偶舍），比如35.5会变成36,  32.5会变成32

# pow()        ==> 次方
#语法：pow（数字，多少次方） pow(2,3)=2**3=8
#本质就是一个幂函数

# divmod()     ==> 商和余数
# max()        ==> 最大值（支持 key 函数）
# min()        ==> 最小值（支持 key 函数）
# sum()        ==> 求和
# map()        ==> 加工一组数据
# filter()     ==> 按条件过滤数据
# reduce()     ==> 合并计算（需导入 functools）
# sorted()     ==> 排序（支持 key 函数）


# 四、数据容器相关
# len()        ==> 获取容器中元素的个数
# range()      ==> 生成一个数字序列（可用于循环）
print(range(10),end=' ')#从0-9，步长1
print(range(2,4))#从2-3，步长1
print(range(3,100,4))#从3到99，步长为4

# sorted()     ==> 对序列进行排序，返回新列表
# enumerate()  ==> 给序列添加索引
names=['qiu','shi','wang']
names=enumerate(names)
print(names)#这样写会返回可迭代对象
print(list(names))#这样写就能看到names与每个东西进行了对应
#观察控制台发现：enumerate本质是把数字和每个字符放一块

# zip()        ==> 将多个序列一一配对
name=['qiu','shi','wang']
scores=[1,2,3,4]
temp=dict(zip(name,scores))
print(temp)#把name和scores里面的东西一一对应了
#不过由于scores多了一个数字，无法对应，所以Python忽略了他

# 五、类型判断与对象相关
# type()       ==> 查看类型
# isinstance() ==> 判断类型
# issubclass() ==> 判断两个类的继承关系
# id()         ==> 查看对象的内存地址


# 六、逻辑判断相关
# all()        ==> 全为真返回 True
# any()        ==> 有一个为真即可


# 七、字符串辅助相关
# ord()        ==> 获取字符的 Unicode 编码值
# chr()        ==> 将 Unicode 编码值转为字符
