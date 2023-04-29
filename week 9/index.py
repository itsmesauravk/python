# print("hello world")
# try:
#     print(2/0)
# except:
#     print("programm is sucessfully printed")

# print("nothing")

# try:
#     numerator = 10
#     denomerator = 0
#     result = numerator/denomerator
# except Exception as e:
#     print("the error is:",e)

#     print(result)
# except ZeroDivisionError:
#     print("error: denomerator cannot be zero")


# try :
#    with open("tes.txt","r") as file:
#       data = file.read()
#       print(data)
# except FileNotFoundError :
#    print("File not found")
# except PermissionError:
#    print("didnt get the permission")
# except Exception as e:
#    print(f'An error occured:{e}')


# Raising the error

# def div(x,y):
#     if y==0:
#         raise ValueError ("cannot be zero")
#     elif y==5:
#         raise ValueError ("cannot be five")
#     return x/y

# try :
#     result=div(5,5)
#     print(result)
# except ValueError as e:
#     print(e)


# try:
#     numerator = 10
#     denomerator = 0
#     result = numerator/denomerator
# except:
#     pass
# very bad idea doing pass.
    
# def divide(x,y):
#     try:
#         result=x/y
#         print(result)
#     except ZeroDivisionError :
#         print("zero div error")
#     except NameError:
#         print("name error")
#     else:
#         print(f"The result of dividing {x} by {y} is {result}")
# try:
#     divide(a,4)
# except NameError:
#     print("name error")

# using finally:
# 
# def divide(x,y):
#     try:
#         result=x/y
#         print(result)
#     except ZeroDivisionError :
#         print("zero div error")
#     except NameError:
#         print("name error")
#     finally:
#         print(f"cant get the result")
#     divide(4,1)





