def check(num,goal):
    goal=int(goal)
    if num>=goal:
        print('成功完成该目标')
def main():
    goals0 = input('请输入您的总目标')
    goals1 = input('请输入您的平均日目标')
    sums=[]
    num0=0#用来计算总运动量
    for i in range(1,8):
        num=input(f'请输入第{i}天的个数')#局部变量，存储第i天情况
        num=int(num)
        num0+=num
        sums.append(i)
    print('现在出示您总体运动情况')
    for i in range(0,7):
        print(f'第{i+1}天：{sums[i]}')
    print(f'总运动量：{num0}   平均量:{num0/7}')
    print('总量',end=' ')
    check(num=num0,goal=goals0)
    print('均值',end=' ')
    check(num=num0/7,goal=goals1)
main()
