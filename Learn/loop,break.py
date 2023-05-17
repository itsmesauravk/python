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
def loop():
    sum=0
    num=int(input('enter :'))
    while num!=0:
        sum+=num
        num=int(input('enter new :'))
        if num==5:
            print('loop continue')
            continue
    print(sum)

    
loop()
enter :10
enter new :10
enter new :5
loop continue
enter new :10
enter new :0
35

def loop():
    sum=0
    num=int(input('enter :'))
    while num!=0:
        num=int(input('enter new :'))
        if num==5:
            print('loop continue')
            continue
        sum+=num
    print(sum)

    
loop()
enter :10
enter new :20
enter new :5
loop continue
enter new :20
enter new :0
40
def loop():
    sum=0
    num=int(input('enter :'))
    while num!=0:
        num=int(input('enter new :'))
        if num==5:
            print('loop continue')
            continue
        else:
            sum+=num
    print(sum)

    
loop()
enter :10
enter new :20
enter new :5
loop continue
enter new :0
20
def loop():
    sum=0
    num=int(input('enter :'))
    while num!=0:
        if num==5:
            print('loop continue')
            num=int(input('enter new :'))
            continue
        else:
            sum+=num
            num=int(input('enter new :'))
    print(sum)

    
loop()
enter :10
enter new :20
enter new :5
loop continue
enter new :0
30
def for():
    
SyntaxError: invalid syntax
def for():
    
SyntaxError: invalid syntax
def try():
    
SyntaxError: invalid syntax
def apple():


def try():
    
SyntaxError: expected an indented block after function definition on line 1
def try():
    
SyntaxError: invalid syntax
SyntaxError: invalid syntax
SyntaxError: incomplete input
try any()
SyntaxError: expected ':'
def loop():
    for i in range(0,10,2):
        print(i)

        
loop()
0
2
4
6
8
SyntaxError: expected ':'
def loop():
    for i in range(0,10,4):
        print(i)
        
SyntaxError: invalid syntax
def loop():
    for i in range(0,10,4):
        print(i)

        
loop()
0
4
8
def loop():
    for i in range(0,10,5):
        print(i)

        
loop()
0
5
def loop():
    for i in range(0,100,4):
        print(i)

        
loop()
0
4
8
12
16
20
24
28
32
36
40
44
48
52
56
60
64
68
72
76
80
84
88
92
96
def loop():
    for i in range(0,40,4):
        print(i)

        
loop()
0
4
8
12
16
20
24
28
32
36
>>> def loop():
...     for i in range(0,44,4):
...         print(i)
... 
...         
>>> loop()
0
4
8
12
16
20
24
28
32
36
40
>>> def loop():
...     for i in range(0,10):
...         i*=7
...       print(i)
...       
SyntaxError: unindent does not match any outer indentation level
>>> def loop():
...     for i in range(0,10):
...         i*=7
...         print(i)
... 
...         
>>> loop()
0
7
14
21
28
35
42
49
56
63
