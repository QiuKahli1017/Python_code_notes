#keys方法：用于获取字典中所有的键
#return的东西类型：dict keys
obj={
    'T':3,
    'T1':4,
    "T5":6,
}
obj_keys=obj.keys()
print(obj_keys,'\n',type(obj_keys))
#注意dict_keys与列表类似，但不可以用下表访问
for obj_key in obj_keys:#用成员标识符就行
    print(obj_key)
#当然，可以用list（）函数，对于他进行一个转化

#以上讲的所有，对于value也是同理

#item方法：获取字典中所有的键值对(return的键值对是以元组呈现 )
obj_items=obj.items()
print(obj_items,'\n',type(obj_items))#这里的类型就是dict_items



obj.update({
    'T3':4,
    'T2':5
})
print(obj)

#get（）方法：获取值，在括号里面写对应的键就可以进行查询