project0=['iphone','ipad','airpods']
def project_print(project):
    while project:
        a=project.pop()
        print(a)
#关键是在调用函数的时候的两种不同写法
project_print(project0[:])#如果这样写，实际上是把project0给复制了一下，并不影响project0的本体
print(project0)
#如果我不这样写
project_print(project0)
print(project0)#我们发现这一行里面啥都没输出，说明在第十行的函数操作后，project0被pop清空了 
