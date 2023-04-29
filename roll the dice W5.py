import random
def roll_dice():
    new_game=input("start game(press any)or Exit(E) ? :")
    total_game = 0
    win = 0
    loose = 0
    while new_game!="E":
        print("note :Random guess is generated, its your turn sir.")
        total_game += 1
        dice1=random.randint(1,6)
        dice2=random.randint(1,6)
        total_sum = dice1 + dice2
        guess = int(input("enter your guess here :"))
        if guess == total_sum:
                    win += 1
                    print("BOOYAHHHHH")
        else :
            loose += 1
            print("play next game,to win")
        new_game=input("start another game(press enter)or Exit(E) ?")
    print("your total game ,win and looses are :",total_game," ,",win," ,",loose)
    print("your win percentage is :",win/total_game *100,"%")
        
                    
                    
        
