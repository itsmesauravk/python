#classes are basically used to call the functions

class HumanDetails:
    def age():
        print("The age is yours ??/")

    def height():
        print("same as yours")


check = HumanDetails
check.height
print(check.height())


#CONSTRUCTOR

class HumanDetails:
    def __init__(self,x,y):
        self.x = x
        self.y = y  #this is constructor this will remembers the values for x and y
    def age():
        print("The age is yours ??/")

    def height():
        print("same as yours")


check = HumanDetails(10,11)
print(check.x)  #this will print 10

#exapmle
class Person:
    def __init__(self,name):
        self.name = name
    def talk(self):
        print(f"Hello mero name chhai {self.name}.")


saurav = Person("Saurav")
print(saurav.name)
saurav.talk()

karki = Person("Karkiy")
karki.talk()
 

#inheritance
class Box:
    def chocolate(self):
        print('I eat em.')

class Darymilk(Box):
    pass

class Kitkat(Box):
    def cheap(self):
        print("this is so cheap..???/")

#this is inheritance which means inside the class Darymilk and Kitkat,
#there are same function defined as in Class Box do we dont have to write them repetedly
sweet = Darymilk()
sweet.chocolate()

price = Kitkat()
price.cheap()

