Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
def loop():
    sum=0
    num=int(input('enter :'))
    while num!=0:
        sum+=num
        num=int(input('enter new :'))
    print(sum)

    
loop()
enter :1
enter new :2
enter new :3
enter new :3
enter new :0
9
def loop():
    sum=0
    num=int(input('enter :'))
    while num!=0:
        sum+=num
        num=int(input('enter new :'))
        if num==5:
            break
    print(sum)

    
loop()
enter :1
enter new :2
enter new :3
enter new :4
enter new :5
10
def loop():
    sum=0
    num=int(input('enter :'))
    while num!=0:
        sum+=num
        num=int(input('enter new :'))
        if num==5:
            continue
    print(sum)

    
loop()
enter :1
enter new :2
enter new :3
enter new :4
enter new :5
enter new :0
15
>>> def loop():
...     sum=0
...     num=int(input('enter :'))
...     while num!=0:
...         sum+=num
...         num=int(input('enter new :'))
...         if num==5:
...             print('loop continue')
...             continue
...     print(sum)
... 
...     
>>> loop()
enter :10
enter new :10
enter new :5
loop continue
enter new :10
enter new :0
35
>>> 
>>> def loop():
...     sum=0
...     num=int(input('enter :'))
...     while num!=0:
...         num=int(input('enter new :'))
...         if num==5:
...             print('loop continue')
...             continue
...         sum+=num
...     print(sum)
... 
...     
>>> loop()
enter :10
enter new :20
enter new :5
loop continue
enter new :20
enter new :0
40
