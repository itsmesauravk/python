def calculator():
    print("Choose the option below for the particulat operation:")
    print ("A = Addition")
    print ("S = Subtraction")
    print ("M = Multiplication")
    print ("D= Division")
    print ("q= Quit calculator")
    print ("C= Continue ")
    option =input ("choose the option from above :")
    while option != "q" :
        num1=float(input("Enter the first number :"))
        num2=float(input("Enter the second number :"))
        option =input ("choose the option from above :")
        if option == "A":
            result=num1 + num2
            print ("The sum is : ",result)
        elif option == "S":
            result=num1 - num2
            print ("The subtraction is : ",result)
        elif option == "M":
            result=num1 * num2
            print ("The multiplication is : ",result)
        elif option == "D":
            result=num1 / num2
            print ("The division is : ",result)
        elif option == "q":
            print ("The calculator is Terminated by user !!!")
        elif option == "C" :
            print ("continued...")
        else:
            print ("choose from option !")
            
