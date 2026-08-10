user_0 = {
    'username':'efermi',
    'first':'enrico',
    'last':'fermi',
    }
for key,value in user_0.items():#这里的key和value分别用来储存遍历时的键和值，然后需要用到一个items的方法
    #需要注意，字典的遍历与前面讲到的列表访问不同，因为字典这个东西他没有下标，只有键值对
    #因为字典这个东西他没有下标，只有键值对
    print("\nKey:"+key)
    print("Value:"+value)
print('\n')
#如果我们只需要遍历它的键，用方法keys()注意不是key！！！！！
for k in user_0.keys():#带括号别忘了
    print(k)
#值同样，用.value() 方法
