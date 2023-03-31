Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
 num =12
 
SyntaxError: unexpected indent
num =12
type(num)
<class 'int'>
n=12.1
type(n)
<class 'float'>
print("hello world")
hello world
print("hello world",1)
hello world 1
type(num)
<class 'int'>
n="12"
type(n)
<class 'str'>
age=19
print("is type of",type(age))
is type of <class 'int'>
int(19)
19
float(19)
19.0
num1=2
num2=3.2
num1+num2
5.2
num1**num2
9.18958683997628
num2-num1
1.2000000000000002
num2/num1
1.6
num1%num2
2.0
print("power",num1+num2)
power 5.2
a=4
b=2
a+=b
print("a+=b")
a+=b
print(a)
6
print("a")
a
a-=3
print(a)
3
a=2
a+=1
print(a)
3
print("comparision operator")
comparision operator
a=(1==2)
check(a)
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    check(a)
NameError: name 'check' is not defined
a=1
b=1
a==b
True
a!=b
False
1or1
SyntaxError: invalid decimal literal
print(1 AND 0)
SyntaxError: invalid syntax. Perhaps you forgot a comma?
print(true and true)
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    print(true and true)
NameError: name 'true' is not defined. Did you mean: 'True'?
print(true or false)
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    print(true or false)
NameError: name 'true' is not defined. Did you mean: 'True'?
print(True and False)
False
print(True or False)
True
print(not true)
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    print(not true)
NameError: name 'true' is not defined. Did you mean: 'True'?
print(not True)
False
print("python is powerful")
python is powerful
current_salary = input("enter your salary")
enter your salary 2000
current_salary
' 2000'
type(current_salary)
<class 'str'>
height=input("height=")
height=5.9
height
'5.9'
type(height)
<class 'str'>
age =int(height)
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    age =int(height)
ValueError: invalid literal for int() with base 10: '5.9'
height=int(height)
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    height=int(height)
ValueError: invalid literal for int() with base 10: '5.9'
float heigh=int(height)
SyntaxError: invalid syntax
height =input("height=")
height=6
type(height)
<class 'str'>
height=int(height)
type(height)
<class 'int'>
print(height)
6
age=input("your age=")
your age=
age=input("your age=")
your age=19
a>=18
False
a>=19
False
a<=7
True
age=input("age=")
age=19
type(age)
<class 'str'>
age=int(age)
\
type(age)
<class 'int'>
a>=18
False
a >= 18
False
x=10000000000000000000
print(x)
10000000000000000000\
a=1.00000000000000000003
print(a)
1.0
a=0.000000000000000000000000000034
print(a)
3.4e-29
print("hello,world!\nle")
hello,world!
le
print("hello,world!\rle")
hello,world!
le
print("I love Saurav")
I love Saurav
print("repled:love you too")
repled:love you too
def calculate_area(l,b)
SyntaxError: incomplete input
calculate_area(l,b)
Traceback (most recent call last):
  File "<pyshell#85>", line 1, in <module>
    calculate_area(l,b)
NameError: name 'calculate_area' is not defined

def add_number(_):
    sum=8+9
    print(sum)

    
add_numbers()
Traceback (most recent call last):
  File "<pyshell#91>", line 1, in <module>
    add_numbers()
NameError: name 'add_numbers' is not defined. Did you mean: 'add_number'?
add_number(_)
17
print(sum)
<built-in function sum>
sum(1,2,3)
Traceback (most recent call last):
  File "<pyshell#94>", line 1, in <module>
    sum(1,2,3)
TypeError: sum() takes at most 2 arguments (3 given)
sum([1,2,3])
6
def sum_numbers(a,b);
SyntaxError: incomplete input
def sum_numbers(a,b):
    add=a+b

    print(add)

    
sum_number(8,9)
Traceback (most recent call last):
  File "<pyshell#101>", line 1, in <module>
    sum_number(8,9)
NameError: name 'sum_number' is not defined. Did you mean: 'sum_numbers'?
sum_numbers(1,2)
3
def add(x,y):
    print(x,y)

    
add(1,3)
1 3
add=add(8,9)
8 9
Add=add(8,9)
Traceback (most recent call last):
  File "<pyshell#108>", line 1, in <module>
    Add=add(8,9)
TypeError: 'NoneType' object is not callable
_add=add(2,3)
Traceback (most recent call last):
  File "<pyshell#109>", line 1, in <module>
    _add=add(2,3)
TypeError: 'NoneType' object is not callable
def add(x,y)
SyntaxError: incomplete input
def add(x,y):
    print(x,y)

    
_add=add(8,9)
8 9
print(_add)
None
def add(x,y)
SyntaxError: incomplete input
... def add(x,y):
...     _sum=x+y
...     return _sum
>>> 
>>> add= add(8,9)
print(_add)
>>> None
add(1,3)
Traceback (most recent call last):
  File "<pyshell#123>", line 1, in <module>
    add(1,3)
>>> TypeError: 'int' object is not callable
... def add(x,y):
...     print(x+y)
... 
>>>     
add(1,3)
>>> 4
add=add(6,7)
>>> 13
print(add)
>>> None
... def add(x,y):
...     sum=x+y
...     return sum
add=add(3,4)
>>> SyntaxError: invalid syntax
add=add(6,7)
Traceback (most recent call last):
  File "<pyshell#134>", line 1, in <module>
    add=add(6,7)
>>> TypeError: 'NoneType' object is not callable
>>> 
>>> 
>>> 
def greet()
>>> SyntaxError: incomplete input
... def greet():
message='hi'
>>> SyntaxError: expected an indented block after function definition on line 1
... def greet():
...     message="hi"
...     print('local',message)
... 
>>>     
greet()
