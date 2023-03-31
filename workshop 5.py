Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
def num():
    """To input ,calculate range using range function and give
       output to the user."""
    x=range(1,11)
    for n in x
    
SyntaxError: incomplete input
def num():
    """To input ,calculate range using range function and give
       output to the user."""
    x=range(1,11)
    for n in x:
        print(n)

        
num()
1
2
3
4
5
6
7
8
9
10
def num():
    """To input ,calculate range using range function and give
       output in odd number to the user."""
    x=range(1,11)
    for n in x:
       if n%2==1:
           print (n)

           
num()
1
3
5
7
9
def num():
    """To input ,calculate range using range function and give
       output in odd number to the user."""
    x=range(1,15)
    for n in x:
       if n%2==1:
           print (n)

           
num()
1
3
5
7
9
11
13
def sum():
    """Take user's input,
      calculate their first 10 natural numbers and do sum,
      give output as a result to user."""
    x=range(1,11)
    for n in x:
        sum=x+1
        print(sum)

        
sum()
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    sum()
  File "<pyshell#24>", line 7, in sum
    sum=x+1
TypeError: unsupported operand type(s) for +: 'range' and 'int'
def sum():
    """Take user's input,
      calculate their first 10 natural numbers and do sum,
      give output as a result to user."""
    n=int(input('number :'))
    while(n>0):
        sum+=n
        n-=1
        print ("the sum is",sum)

        
sum()
number :10
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    sum()
  File "<pyshell#36>", line 7, in sum
    sum+=n
UnboundLocalError: cannot access local variable 'sum' where it is not associated with a value
sum=0
\
sum=0
\
sum=0
n=range(1,11):
    
SyntaxError: incomplete input
sum=0
n=range(1,11)
SyntaxError: multiple statements found while compiling a single statement

sum=0
n=range(1,11)
sum+=n
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    sum+=n
TypeError: unsupported operand type(s) for +=: 'int' and 'range'
sum=0
for n in range(1,11)
SyntaxError: incomplete input
sum=0
for i in range(1,11):
    sum+=i

    
print(sum)
55
def mult():
    """Take input as a positive number,
       creat the multiplication table of that number,
       print the result and give output to user."""
    n=int(input('enter positive num:')
          if n>0:
          
SyntaxError: incomplete input
def mult():
    """Take input as a positive number,
       creat the multiplication table of that number,
       print the result and give output to user."""
    n=int(input('enter positive num:'))
    if n>0:
        for n in range (0,n)
        
SyntaxError: incomplete input
def mult():
    """Take input as a positive number,
       creat the multiplication table of that number,
       print the result and give output to user."""
    n=int(input('enter positive num:'))
    if n>0:
        for n in range (0,11):
            mult*=n
            print(mult)
    else:
        print("enter positive num:")

        
mult()
enter positive num:5
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    mult()
  File "<pyshell#67>", line 8, in mult
    mult*=n
UnboundLocalError: cannot access local variable 'mult' where it is not associated with a value
def mult():
    """Take input as a positive number,
       creat the multiplication table of that number,
       print the result and give output to user."""
    n=int(input('enter positive num:'))
    if n>0:
        for n in range (0,11):
            n*=n
            print(n)
    else:
        print("enter positive num:")

        
mult()
enter positive num:4
0
1
4
9
16
25
36
49
64
81
100
def mult():
    """Take input as a positive number,
       creat the multiplication table of that number,
       print the result and give output to user."""
    x=int(input('enter positive num:'))
    if n>0:
        for n in range (0,11):
            n*=x
            print(n)
    else:
        print("enter positive num:")

        
mult()
enter positive num:5
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    mult()
  File "<pyshell#73>", line 6, in mult
    if n>0:
UnboundLocalError: cannot access local variable 'n' where it is not associated with a value

def mult():
    """Take input as a positive number,
       creat the multiplication table of that number,
       print the result and give output to user."""
    x=int(input('enter positive num:'))
    if x>0:
        for n in range (0,11):
            n*=x
            print(n)
    else:
        print("enter positive num
              
SyntaxError: incomplete input

def mult():
    """Take input as a positive number,
       creat the multiplication table of that number,
       print the result and give output to user."""
    x=int(input('enter positive num:'))
    if x>0:
        for n in range (0,11):
            n*=x
            print(n)
    else:
        print("enter positive num:")

        
mult()
enter positive num:5
0
5
10
15
20
25
30
35
40
45
50
mult()
enter positive num:-1
enter positive num:
def fact():
    """Take a number as a input from user,
        calculate the factorial of the given number,
        give output as a result to the user."""
    n=int(input('enter number:'))
    for i in range(1,n+1):
        i*=n
        sum+=i

        
def fact():
    """Take a number as a input from user,
        calculate the factorial of the given number,
        give output as a result to the user."""
    n=int(input('enter number:'))
    for i in range(1,n+1):
        i*=n
        sum+=i
        print(sum)

        
fact()
enter number:4
Traceback (most recent call last):
  File "<pyshell#96>", line 1, in <module>
    fact()
  File "<pyshell#95>", line 8, in fact
    sum+=i
UnboundLocalError: cannot access local variable 'sum' where it is not associated with a value
def fact():
    """Take a number as a input from user,
        calculate the factorial of the given number,
        give output as a result to the user."""
    n=int(input('enter number:'))
    for i in range(1,n+1):
        i*=n

        
KeyboardInterrupt
def fact():
    """Take a number as a input from user,
        calculate the factorial of the given number,
        give output as a result to the user."""
    n=int(input('enter number:'))
    for i in range(1,n+1):
        i*=n
        print(i)

        
fact()
enter number:4
4
8
12
16
def fact():
    """Take a number as a input from user,
        calculate the factorial of the given number,
        give output as a result to the user."""
    n=int(input('enter number:'))
    for i in range(1,n+1):
        i-=n
        print(i)

        
fact()
enter number:4
-3
-2
-1
0
def fact():
    """Take a number as a input from user,
        calculate the factorial of the given number,
        give output as a result to the user."""
    n=int(input('enter number:'))
    for i in range(1,n+1):
        i+=n
        print(i)

        
fact()
enter number:5
6
7
8
9
10
KeyboardInterrupt
def fact():
    """Take a number as a input from user,
        calculate the factorial of the given number,
        give output as a result to the user."""
    n=int(input('enter number:'))
    for i in range(1,n+1):
        n-=i
        print(i)

        
fact()
enter number:4
1
2
3
4
def fact():
    """Take a number as a input from user,
        calculate the factorial of the given number,
        give output as a result to the user."""
    n=int(input('enter number:'))
    for i in range(1,n+1):
        n-=i
        mult*=i
        print(i)

        
fact()
enter number:4
Traceback (most recent call last):
  File "<pyshell#116>", line 1, in <module>
    fact()
  File "<pyshell#115>", line 8, in fact
    mult*=i
UnboundLocalError: cannot access local variable 'mult' where it is not associated with a value
def fact():
    """Take a number as a input from user,
        calculate the factorial of the given number,
        give output as a result to the user."""
    n=int(input('enter number:'))
    for i in range(1,n+1):
        n-=i
        mult*=i
        print(mult)

        
fact()
enter number:4
Traceback (most recent call last):
  File "<pyshell#119>", line 1, in <module>
    fact()
  File "<pyshell#118>", line 8, in fact
    mult*=i
UnboundLocalError: cannot access local variable 'mult' where it is not associated with a value
def fact():
    """Take a number as a input from user,
        calculate the factorial of the given number,
        give output as a result to the user."""
    n=int(input('enter number:'))
    fact=1
    for i in range(1,n+1):
        fact*=i
        print(i)

        
fact()
enter number:4
1
2
3
4
def fact():
    """Take a number as a input from user,
        calculate the factorial of the given number,
        give output as a result to the user."""
    n=int(input('enter number:'))
    fact=1
...     for i in range(1,n+1):
...         fact*=i
...         print(fact)
... 
...         
>>> fact()
enter number:4
1
2
6
24
>>> def fact():
...     """Take a number as a input from user,
...         calculate the factorial of the given number,
...         give output as a result to the user."""
...     n=int(input('enter number:'))
...     fact=1
...     for i in range(1,n+1):
...         fact*=i
...     print(fact)
... 
...     
>>> fact()
enter number:4
24
>>> text=input('hello world'[.::-1])
SyntaxError: invalid syntax
>>> text='hello world'[.::-1]
SyntaxError: invalid syntax
>>> text=input('Enter text here :')
Enter text here :saurav
>>> print(text,::-1)
SyntaxError: invalid syntax
>>> text=input('enter text here :')[::-1]
enter text here :saurav
>>> print(text)
varuas
>>> def num():
...     """ """
