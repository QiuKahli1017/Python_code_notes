#sorted函数默认按照Unicode编码进行排列
#写入reverse=True的参数会反向排列
#语法格式:sorted(list,key=xxx,reverse=True/False)
#这里的key就是排列的依据，可以写函数
language=['java','cpp','python']
language=sorted(language,key=lambda x:len(x),reverse=True)
print(language)