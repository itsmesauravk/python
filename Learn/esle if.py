Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
costPrice=float(input('Enter the cost price ofthe product'))
Enter the cost price ofthe product 50
sellingprice= float(input('selling price'ArithmeticError))
SyntaxError: invalid syntax. Perhaps you forgot a comma?

cp=float(input('costprice'))
costprice 50
sp=float(input('sellingprice'))
sellingprice 60
p=sp-cp
print('profit',p)
profit\ 10.0


c=float(input('enter temp in celcius'))
enter temp in celcius32
f=c*9/5=32
SyntaxError: cannot assign to expression


C=float(input('tmpr in celcius :'))
tmpr in celcius :32
F=C*9/5+32
print('tempr in fahrenheit is :',F)
tempr in fahrenheit is : 89.6

def celcius(c)
SyntaxError: incomplete input


def convert(celcius)
SyntaxError: incomplete input


def convert(celcius):
    in_f=(celcius*9/5)+32
    return in_f
convert(37)
SyntaxError: invalid syntax


def convert(celcius):
    in_f=(celcius*9/5)+32
    return in_f

convert(37)
98.6


grade=20
grade>=70
False


grade=50
grade=50


grade=float(input('enter grade:'))
enter grade:40
if grade>=40:
    print('pass')

    
pass
if grade>=40:
    print('pass')
else:
    print('fail')

    
pass


def grade(mark):
    if mark>=40:
        print('pass')
    else:
        print('fail')
    return mark

mark(34)
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    mark(34)
NameError: name 'mark' is not defined


def grade(mark):
    if mark>=40:
        print('pass')
    else:
        print('fail')
    return grade

\
grade(45)
pass
<function grade at 0x0000024F1029ED40>


def grade(mark):
    if mark>=40:
        print('pass')
    else:
        print('fail')
    return grade

grade(46)
pass
<function grade at 0x0000024F1029CC20>


def grade(mark):
    if mark>=40:
        print('pass')
    else:
        print('fail')
    return grade

grade(20)
SyntaxError: invalid syntax



def result():
    grade = float(input('grade got :'))
    if grade>=40
    
SyntaxError: incomplete input
def result():
    grade = float(input('grade got :'))
    if grade>=40:
        print('pass')
    else:
        print('fail')
    return grade

def result():
    grade = float(input('grade got :'))
    if grade>=40:
        print('pass')
    else:
        print('fail')
    return result

def result():
    grade = float(input('grade got :'))
    if grade>=40:
        print('pass')
    else:
        print('fail')

        
result
<function result at 0x0000024F1028F560>
def result():
    grade = float(input('grade got :'))
    if grade>=40:
        print('pass')
    else:
        print('fail')


45
45
def result():
    grade = float(input('grade got :'))
    if grade>=40:
        print('pass')
    else:
        print('fail')

result()
grade got :80
pass

def sum_thrice(x,y,z)
SyntaxError: incomplete input
def sum_thrice(x,y,z):
    if x==y or y==z or z==x:
    else:
        
SyntaxError: expected an indented block after 'if' statement on line 2
def sum_thrice(x,y,z):
    if x==y or y==z or z==x:
        sum=0
    else:
        sum=x+y+z

        
return sum
SyntaxError: 'return' outside function
def sum_thrice(x,y,z):
    if x==y or y==z or z==x:
        sum=0
    else:
        sum=x+y+z
    return sum

def sum_thrice(x,y,z):
    if x==y or y==z or z==x:
        sum=0
    else:
        sum=x+y+z
    return sum
x=int(input('enter a number'))
SyntaxError: invalid syntax
SyntaxError: incomplete input
SyntaxError: incomplete input




print('hy, beautiful soul')
hy, beautiful soul


def result():
    grade = float(input('grade got :'))
    if grade>=40:
        print('pass')
    elif grade>=70:
        print('you are genius')
    else grade<40:
        
SyntaxError: expected ':'
def result():
    grade = float(input('grade got :'))
    if grade>=40:
        print('pass')
    elif grade>=70:
        print('you are genius')
    else:
        print('try again')

        
result()
grade got :36
try again
result()
grade got :81
pass
 ':'
def result():
    grade = float(input('grade got :'))
    if grade>=40:
        print('pass')
    if grade>=70:
        print('you are genius')
    else:
        print('try again')
        
SyntaxError: unexpected indent

def result():
    grade = float(input('grade got :'))
    if grade>=40:
        print('pass')
    if grade>=70:
        print('you are genius')
    else:
        print('try again')

        
result()
grade got :81
pass
you are genius


def result():
    grade=float(input('your grade :'))
    if grade>=70:
        return('average')
    elif grade>=50:
        return('not bad not bad')
    else:
        return('very good')

    
result()
your grade :23
'very good'
result()
your grade :569
'average'
a=87
b=49
s=a-b
print(s)
38
a=93
b=59
s=a-b
>>> print s
SyntaxError: incomplete input
>>> print (s)
34
>>> 
>>> 
>>> SyntaxError: incomplete input
SyntaxError: incomplete input
>>> 
>>> print('Herald college Kathmandu',\n 'Naxal PO:44600 ',\n, 'Kathmandu Nepal')
SyntaxError: unexpected character after line continuation character
>>> print('Herald college Kathmandu,\n Naxal PO:44600 ,\n Kathmandu Nepal')
Herald college Kathmandu,
 Naxal PO:44600 ,
 Kathmandu Nepal
>>> 
>>> 
>>> n=float(int('enter a number'))
Traceback (most recent call last):
  File "<pyshell#185>", line 1, in <module>
    n=float(int('enter a number'))
ValueError: invalid literal for int() with base 10: 'enter a number'
>>> n=float(input('enter any number'))
enter any number 6
>>> Remainder=n%2
>>> print('the remainder is',Remainder)
the remainder is 0.0
>>> 
>>> n=float(input('enter any number'))
... enter any number 7
... Remainder=n%2
... print('the remainder is',Remainder)
SyntaxError: multiple statements found while compiling a single statement
>>> 
>>> n=float(input('enter any number'))
enter any number 23
>>> Rem=n%2
>>> print('the remainder is',Rem)
the remainder is 1.0
>>> Remainder=n%2
>>> 
>>> weight=float(input('Your weight :'))
Your weight :60.3
>>> height=float(input('Your height :'))
Your height :5.8
>>> BIM=weight/height
