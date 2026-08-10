def num(n):
    if n==0 or n==1:
       return 1
    elif n>1:
       return n*num(n-1)
print(num(3))