Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
Age[1,2,3,4,5,6]
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    Age[1,2,3,4,5,6]
NameError: name 'Age' is not defined
Age range[1,10]:
    
SyntaxError: invalid syntax
Age[1,2,3,4,5]:
    
SyntaxError: incomplete input
num=[1,2,3]
type(num)
<class 'list'>
list[1]
list[1]
num[2]
3
num.append[4]
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    num.append[4]
TypeError: 'builtin_function_or_method' object is not subscriptable
num=[1,2,3,4,5,6,7]
num[-1]
7
num[1]
2
num.append(8)
print(num)
[1, 2, 3, 4, 5, 6, 7, 8]
num.insert(2,"a")
print(num)
[1, 2, 'a', 3, 4, 5, 6, 7, 8]
num.insert(1,'b')
print(num)
[1, 'b', 2, 'a', 3, 4, 5, 6, 7, 8]
ant[8,9,0]
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    ant[8,9,0]
NameError: name 'ant' is not defined. Did you mean: 'any'?
ant=[8,9,0]
num.extent(ant)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    num.extent(ant)
AttributeError: 'list' object has no attribute 'extent'. Did you mean: 'extend'?
num.extend(ant)
print(num)
[1, 'b', 2, 'a', 3, 4, 5, 6, 7, 8, 8, 9, 0]
num_copy=nums
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    num_copy=nums
NameError: name 'nums' is not defined. Did you mean: 'num'?
num_copy=num
num.append('zz')
print(num_copy)
[1, 'b', 2, 'a', 3, 4, 5, 6, 7, 8, 8, 9, 0, 'zz']


print(num)
[1, 'b', 2, 'a', 3, 4, 5, 6, 7, 8, 8, 9, 0, 'zz']
del num(1)
SyntaxError: incomplete input
eight.remove('b')
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    eight.remove('b')
NameError: name 'eight' is not defined
num.remove('b')
print(num)
[1, 2, 'a', 3, 4, 5, 6, 7, 8, 8, 9, 0, 'zz']
del num(1)
SyntaxError: incomplete input
del num(1):
    
SyntaxError: incomplete input
del num[1]
print(num)
[1, 'a', 3, 4, 5, 6, 7, 8, 8, 9, 0, 'zz']

len(num)
12

for number in nums:
    print(number)

...     
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    for number in nums:
NameError: name 'nums' is not defined. Did you mean: 'num'?
>>> for number in num:
...     print(number)
... 
...     
1
a
3
4
5
6
7
8
8
9
0
zz
>>> 
>>> 
>>> nums=[1,2,[2.1,2.2],3,4]
>>> nums[2]
[2.1, 2.2]
>>> nums[2][0]
2.1
>>> nums_1=nums[2][1]
>>> print[nums_1]
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    print[nums_1]
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> print(nums_1)
2.2
>>> l=[1,2,[3,4,[5,6],7],8]
>>> l[2][2][1]
6
