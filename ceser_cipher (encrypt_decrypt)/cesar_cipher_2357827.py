import os

def welcome():
    print("Welcome to the Caesar Cipher")
    print("This program encrypt and decrypts text with the Caesar Cipher")

def enter_message():
    while True:
        mode = input("What would you like to do encrypt (e) or decrypt (d)  ?:")
        if mode != "e" and mode !="d":
            print("Invalid Input")
        else:
            break
    message = input("What would you like to {} ?:".format
    ("encrypt" if mode == "e" else "decrypt"))
    message = message.upper()
    while True:
        try:
            shift = int(input("Enter the shift number :")) 
            break
        except ValueError:
            print("Invalid Shift")
    
    return(mode,message,shift)

def encrypt(message,shift):
    result = ""
    for char in message.upper():
        if char.isalpha():
            result += chr((ord(char) + shift -65) % 26 +65)
        else:
            result += char
    
    return(result)

def decrypt(message,shift):
    result = ""
    for char in message.upper():
       if char.isalpha():  
           result += chr((ord(char) - shift -65) % 26 +65)
       else:
           result += char
    
    # return(result)
    encrypt(message,-shift)

def process_file(filename,mode,shift):
    try:
        with open(filename,'r') as f:
            msg = f.read()
        if mode == 'e':
            EncryptedResult = ""
            for char in msg.upper():
                if char.isalpha():
                    EncryptedResult += chr(ord(char) + shift)
                else:
                    EncryptedResult += char
            write_message(EncryptedResult)
            print(EncryptedResult)
        elif mode == 'd':
            DecryptedResult =""
            for char in msg.upper():
                if char.isalpha():
                    DecryptedResult += chr(ord(char) - shift)
                else:
                    DecryptedResult += char
            write_message(DecryptedResult)
            print(DecryptedResult)
    except FileNotFoundError:
        print("File not found:",filename)

def write_message(msg):
    with open("result.txt",'w') as f:
        f.write(msg)

def is_file(filename):
    return os.path.isfile(filename)

def message_or_file():
    while True:
        ValidMode = ["e","d"]
        mode = input("What would you like to do encrypt (e) or decrypt (d)  ?:").lower()
        while mode not in ValidMode:
            print("Invalid mode.")
            mode =input("What would you like to do encrypt (e) or decrypt (d)  ?:").lower()
        while True:
            ReadingMode = input("Would you like to read from file (f) or the console (c)  ?:").lower()
            if ReadingMode not in ("f","c"):
                print("Invalid mode.")
                ReadingMode = input("Would you like to read from file (f) or the console (c)  ?:").lower()
            break
        while True:
            try:
                shift = int(input("What is the shift number :"))
                break
            except ValueError :
                print("Invalid shift")
        if ReadingMode == "c":
            message = input("What would you like to {} ?:".format
    ("encrypt" if mode == "e" else "decrypt"))
            if mode == "e":
                encrypted = encrypt(message, shift).upper()
                print(encrypted)
            elif mode == "d":
                decrypted = decrypt(message, shift).upper()
                print(decrypted)
        elif ReadingMode == "f":
            while True:
                filename = input("Enter file name :")
                if not is_file(filename):
                    print("File not found",filename)
                    continue
                else:
                    process_file(filename, mode, shift)
                    print("Result printed to result.txt")
                break
            break
        break

def main():
    welcome()
    while True:
        message_or_file()
        start_again = input("Would you like to encrypt or decrypt another message (Y/N)  ?:").upper()
        if start_again not in ("N","Y"):
            print("Invalid input.")
            start_again = input("Would you like to encrypt or decrypt another message (Y/N)  ?:").upper()
        if start_again == "N":
            print("Thank you for using program, Good bye !")
            break

main()


    

