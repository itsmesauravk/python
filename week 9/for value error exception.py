def converter():
    try:
        user_input = input("enter the string :")
        result = int(user_input)
        print(type(result),result)
    except ValueError:
        print("value error ,string cannot be converted into intiger!")
        
