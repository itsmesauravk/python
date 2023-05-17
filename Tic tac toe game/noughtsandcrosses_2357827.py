import random
import os.path
import json
random.seed()

def draw_board(board):
    # getting the board structure for game tic tac toe
    # using for loop to create the board structure
    print(" -----------")
    for i in range(3):
        row = "| "
        for j in range(3):
            row += board[i][j] + " | "
        print(row)
        print(" -----------")

def welcome(board):
    #printing the welcome message
    print("Welcome to the 'Unbeataible Noughts and Crossess' game .")
    print("The board layout is shown below")
    draw_board(board)
    print("When prompted,enter the number corresponding to the square you want.")

def initialise_board(board):
    board = [['1', '2', '3'],
        ['4', '5', '6'],
        ['7', '8', '9']]

    for i in range(len(board)):
        for j in range(len(board[i])):
            board[i][j] =" "
    for row in board:
        print(row)
    return board
    
def get_player_move(board):
        #asking the user to input the square number where user want to put 'X' on the board and returning row and colums          
    while True:
        try:
            def square():
                result = ""
                for i in range(1, 10):
                    result += str(i) + " "
                    if i % 3 == 0:
                        result += "\n"
                return result
            move = int(input(f"Enter a square:{square()} :"))
            if move < 1 or move > 9:
                raise ValueError("move should be greater than 1 and lesser than of 9")
            row, col = (move-1)//3, (move-1)%3
            if board[row][col] != " ":
                raise ValueError("Position already taken")
            return row, col
        except ValueError as e:
            print(e)
        except Exception as e:
            print("An error occurred:", e)
            raise e

        
def choose_computer_move(board):
        # making the random move of computer to play against the user and returning the random generated row and column
    while True:
        try:
            random_move=random.randint(1,9)
            row,col=(random_move-1)//3,(random_move-1)%3
            if board[row][col] != " ":
                raise ValueError
            return row,col
        except Exception as e:
            print(e)


    
def check_for_win(board, mark):
    # checking weather the computer has won or user had won
    # Returning  True if user or computer has won, if not then returning False
    for row in board:
        if row.count(mark) == 3 and ' ' not in row:
            return True
    for i in range(3):
        column = [row[i] for row in board]
        if column.count(mark) == 3 and ' ' not in column:
            return True
    diagonal1 = [board[i][i] for i in range(3)]
    diagonal2 = [board[i][2-i] for i in range(3)]
    if diagonal1.count(mark) == 3 and ' ' not in diagonal1:
        return True
    if diagonal2.count(mark) == 3 and ' ' not in diagonal2:
        return True
    return False


def check_for_draw(board):
    # checking for all the squares either all of them are full or not 
    # if they all are full returning true otherwise returning false
    for row in board:
        if " " in row:
            return False
    return True
        
def play_game(board):
    # firstly initialise the board and displaying it
    welcome(board)
    board = initialise_board(board)
    
    for i in range(9):
        row, col = get_player_move(board)
        board[row][col] = "X"
        if check_for_win(board,"X"):
            print("You won!")
            draw_board(board)
            score=1
            return score
        if check_for_draw(board):
            print("Draw")
            score=0
            return score
        row, col = choose_computer_move(board)
        board[row][col] = "0"
        draw_board(board)
        
        if check_for_win(board,"0"):
            print("You lost!")
            draw_board(board)
            score=-1
            return score


def menu():
        #creatin the menu for user to make easy to play game

    while True:
        print("1-Play the game")
        print("2-Save your socre in the leaderboard")
        print("3-Load and display the leaderboard")
        print("q-quite the game")
        choice = input("Enter an input number between (1, 2, 3, q) : ")
        if choice in ['1', '2', '3', 'q']:
            return choice
        else:
            print("Invalid input. Please enter a valid option.")
    

def load_scores():
        #loading the win score and player name from the file name called leaderboard.txt
    try:
        filename="leaderboard_2357827.txt"
        if is_file(filename):
            with open('leaderboard_2357827.txt', 'r') as f:
                data = json.load(f)
                return data
        else:
            print("Leaderboard not found")
    except Exception as e:
        print(f"An error occurred while loading the scores: {e}")
        raise e
    

def save_score(score):
        #saving the win score to by entering the user name and storing it in the file name leaderboard.txt
    name = input("Enter your name: ")
    data = {}
    filename="leaderboard_2357827.txt"
    if is_file(filename):
        try:
            with open('leaderboard_2357827.txt', 'r') as f:
                data = json.load(f)
        except FileNotFoundError as e:
            raise e
        
        if name in data:
            data[name]=score+data[name]
        else:
            data[name] = score

        with open('leaderboard_2357827.txt', 'w') as f:
            json.dump(data, f)

        print("Score saved to leaderboard!")
    else:
        print("Leaderboard not found")

def is_file(filename):
    return os.path.exists(filename)




def display_leaderboard(leaders):
    for name, score in leaders.items():
        print(f"{name}: {score}")
