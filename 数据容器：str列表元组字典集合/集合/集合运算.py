#我们会提到并集，交集，差集，对称差集
#并集
s1={1,2,3}
s2={1,3,4}
result= s1|s2#return是二者并集

#交集
result0=s1 & s2 #return是二者交集

#差集：减号
result1=s1-s2#得到，属于s1同时不属于s2的
result3=s1-s2#属于s2但不属于s1的

#对称交集
result2=s1^s2#s1s2顺序调换都一样
#删去二者交集内容后保留下来