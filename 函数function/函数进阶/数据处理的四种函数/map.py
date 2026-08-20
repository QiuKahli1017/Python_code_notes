nums=[1,2,3,4,5,6,7]
#map()对数据进行统一的加工

#比如让每个数据进行乘以三
nums_new=map(lambda x:x*3,nums)#这里运用了匿名函数
print(nums_new)
#map返回的对象是迭代器类型对象，所以输出了一个内存地址
#所以我们需要进行类型转换，或者遍历一下
nums_new=list(nums_new)
print(nums,'\n',nums_new)#发现原来的也没变

#注意由于这里map本身就是一个函数，所以我们写的是triple,而不是triple()
#如果写成调用就会错误
#要操作的可迭代对象写在后面
#而且使用以后，如果不保存，他就会被“消耗”


#eg：字符串转化
temps=['java','cpp','python']
temps_new=map(lambda x:x.title(),temps)
print(list(temps_new))

#eg:类型转换
str_number={'1','3','13','5','11'}
str_number_new=map(lambda x:int(x),str_number)
print(str_number,' ',list(str_number_new))