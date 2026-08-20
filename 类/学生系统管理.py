class Student:
    def __init__(self,name,gender,idcard):
        self.name=name
        self.gender=gender
        self.id=idcard
        self.score='NONE'

#main
signal=True
info={}
while signal:
    print("*"*10+'学生管理'+"*"*10)
    print('1.添加学生')
    print('2.删除学生')
    print('3.查看所有学生')
    print('4.录入成绩')
    print("5.退出")
    temp=input("请输入操作序号:")
    if temp=='5':
        print('感谢使用本系统')
        break
    elif temp=='1':
        print('请输入学生信息')
        name0=input('姓名：')
        gender0=input('性别：')
        id0=input("编号:")
        student=Student(name0,gender0,id0)
        info[id0]=student
    elif temp=='3':#查看所有学生信息
        if info=={}:
            print('目前无人录入')
            continue
        for keys,value in info.items():
            print("编号"+keys,' ','姓名'+value.name,' ','性别'+value.gender,'成绩'+value.score)
    elif temp=='4':
        if info == {}:
            print('目前无人录入')
            continue
        id1=input('请输入学生编号')
        score0=input('请输入学生成绩:')
        info[id1].score=score0
    elif temp=='2':
        if info=={}:
            print('目前无人录入')
            continue
        te=input('输入True来确认需要删除，输入False返回管理主页')
        if te=='True':
            student_id=input('请输入需要删除的学生ID')
            del info[student_id]
            print('删除完毕')
