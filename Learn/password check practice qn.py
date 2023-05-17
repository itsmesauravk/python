def password():
    while True:
        psword=input("enter new password :")
        if len(psword)<8:
            print("your password is less then 8 character.")
            continue
        if not any(i.isupper()for i in psword):
            print("enter at least one upper case character.")
            continue
        if not any(i.islower()for i in psword):
            print("enter at least one lower case character.")
            continue
        if not any(i.isdigit()for i in psword):
            print("enter at least one digit.")
            continue
        break
    print("your password is created.")
                
                
            
                
            

