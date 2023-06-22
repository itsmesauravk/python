def deposite():
    while True:
        try:
            deposite_money = int(input("enter the deposite you want to : "))
            if deposite_money <= 0 :
                print("must be greater then 0 ")
            else:
                break
        except ValueError:
            print("enter The digits")
    return(deposite_money)


def bet_money(deposite_money):
    while True:
        try:
            bet = int(input("enter the money you want to bet on : "))
            if bet <= 0 or bet > deposite_money:
                print("invalid input ")
            else:
                break
        except ValueError:
            print("enter The digits")
    return (bet)

def num_lines():
    while True:
        try:
            lines = int(input("enter the number of lines you want to bet on (1-3) : "))
            if lines <= 0 or lines > 3:
                print("invalid numbers of lines ")
            else:
                break
            
        except ValueError:
            print("enter The digits")
    return (lines)

def total_bet(bet,lines,deposite_money):
    money = lines * bet
    while True:
        if money < deposite_money :
            print("invlaid input")
        else:
            break



