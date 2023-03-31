Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
num=[1,2,3,4,5]
For i in num:
    
SyntaxError: invalid syntax
for number in num:
    number+=num
    print(number)

    
Traceback (most recent call last):
  File "<pyshell#5>", line 2, in <module>
    number+=num
TypeError: unsupported operand type(s) for +=: 'int' and 'list'
num=[1,2,3,4]
number=0
for number in num:
    number+=num
    print(number)

    
Traceback (most recent call last):
  File "<pyshell#11>", line 2, in <module>
    number+=num
TypeError: unsupported operand type(s) for +=: 'int' and 'list'
total=sum(num)
print(total)
10

num=[1,2,3]
sum=0
for number in num:
    sum+=number
    print(sum)

    
1
3
6


a={1,2,2,4,5}
print(a)
{1, 2, 4, 5}
a={'a','b','b',2}
print(a)
{2, 'b', 'a'}
a={'a','b','b'}
print(a)
{'b', 'a'}

a={'a','b','b',}
print(a)
{'b', 'a'}

x=(1,2,3,4)
del x(1)
SyntaxError: incomplete input
x.remove(1)
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    x.remove(1)
AttributeError: 'tuple' object has no attribute 'remove'
>>> 
>>> 
>>> 
>>> 
>>> x=('a',1,2,3)
>>> 
>>> 
>>> nums=[2,3,4,5]
>>> nums_sqr=nums**2
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    nums_sqr=nums**2
TypeError: unsupported operand type(s) for ** or pow(): 'list' and 'int'
>>> num=[1,2,3,4]
>>> nums_1=num[0]**2
>>> print(nums_1)
1
>>> num=[1,2,3]
>>> sqr=1
>>> for square in num:
...     sqr=square**2
... 
...     
>>> print(sqr)
9
>>> num[1,2,3]
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    num[1,2,3]
TypeError: list indices must be integers or slices, not tuple
>>> num=[1,2,3,4]
>>> num_1=[]
>>> for numbers in num:
...     num_1.append(number**2)
... 
...     
>>> num_1
[9, 9, 9, 9]
