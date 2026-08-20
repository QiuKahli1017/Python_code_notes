def using(pet='大狗'):
    print(pet)
using('哈基米')
using()#如果不填东西，这里就会默认写大狗，见上面pet里面的括号


def pets(type, name='大狗'):
    print(type, name)
pets('狗狗',)#就像这里，我们定义了两个形参，可以一个给默认值，一个不给默认值，实际运行效果大差不差
#或者这样写
pets(type='狗狗')#效果相同，没有逗号意味着我们忽略了对于name形参的实参输入