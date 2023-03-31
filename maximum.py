def max():
    if x>y and x>z:
        max=x
    elif y>x and y>z:
        max=y
    else:
        max=z
    return max
x=int(input('enter number:'))
y=int(input('enter number:'))
z=int(input('enter number:'))
result=max()
print(result,'is the max number among three.')

