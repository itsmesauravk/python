import random

#example 1
fruits_name = ["mango",'apples','banana','pineapple']
result = random.choice(fruits_name)
print(result)

#example 2
class Dice:
    def __init__(self):
        pass
    def roll(self):
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)
        # print(f'({dice1},{dice2})')
        return dice1,dice2


output = Dice()
print(output.roll())