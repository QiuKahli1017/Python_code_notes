i=[1,2,3,4,5]
if 3 in i:
    print("True")
if 6 not in i:
    print('False')
#如上，我们使用了in和not in来判断元素是否在列表中，同理，也可以用来判断字典
i0={#提醒一下，键值对之间需要用冒号链接哦
    1:1,
    2:4,
    3:9,
    4:16,
}
if 5 in i0.keys():
    print("False")
