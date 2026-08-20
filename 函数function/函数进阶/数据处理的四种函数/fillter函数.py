#对一组数据里面进行筛选，并留下筛选通过的
#filter(过滤规则即函数，操作对象)

#eg:筛选数值
nums=[1,2,3,4,5,6,7]
def f(x):
    if x%2==0:
        return x
nums_new=list(filter(f,nums))
nums_new=list(filter(lambda x:x%2==0,nums))
#两种写法都可以，第二种写法意思是，只要取余2为0，都会被保留
print(nums_new)

#eg:筛选成年人
person=[
    {'id':1,'age':18,'gender':'男'},
    {'id':2,'age': 19, 'gender': '女'},
    {'id':3,'age': 14, 'gender': '女'},
    {'id':4,'age':32,'gender':'男'}
]
result0=filter(lambda x:x['age']>=18)
#如果函数不写，他会自动识别False值
#但要写成filter(None,data)