def dashboard():
    list=[]
    print(" choose option from below \n1. Add product \n2. Remove product \n3. Search producct \n4. List all the product \n5. Quit ")
    while True :
        option=input("enter your option here : ")
        if option == "1":
            prod1=input("enter product to add :")
            list.append(prod1)
        elif option == "2":
            prod2 = input ("enter product to remove :")
            list.remove(prod2)
        elif option == "3":
            prod3 = input("enter your product code :")
            if prod3 in list:
                print("yes it is in store")
            else:
                print('not in store')
        elif option =="4":
            print(list)
        elif option =="5":
            print("ending list")
            break
        else:
            print("choose from options ")
        
    

