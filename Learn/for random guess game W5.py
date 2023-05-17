"""importaing random to take random number from the computer
    taking input as a guess from user
    comparing the results
    giving output to users."""
import random
def guess_game():
    random_num=random.randint(1,20)
    print(random_num)
    for i in range(5):
        guess=int(input("enter your guess here by entering btwn 1=20 :"))
        if guess>random_num :
            print("sir,please think a bit lower.")
        elif guess<random_num :
            print("sir,please think a bit higher.")
        elif guess == random_num :
            print("boom-sakalaka,correct guess.")
            break
    else:
        ("sorry,try again!!!.")
