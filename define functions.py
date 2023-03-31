def either_side(num):
    n1=num+1
    n2=num-1
    return n1,n2

num=int(input('any number :'))
result=either_side(num)
print(result)
