from noughtsandcrosses_2357827 import *

    
def main():
    #displaying board
    board = [ ['1','2','3'],\
            ['4','5','6'],\
            ['7','8','9']]

    welcome(board)
    #checking the user input from the menu and giving result accordingly
    total_score = 0
    while True:
        choice = menu()
        if choice == '1':
            score = play_game(board)
            # total_score += score
            print(f'Your score is: {score} ',)
        if choice == '2':
            save_score(score)
        if choice == '3':
            leader_board = load_scores()
            display_leaderboard(leader_board)
        if choice == 'q':
            print('Thank you for playing the "Unbeatable Noughts and Crosses" game.')
            print('Good bye')
            return



# all the program start executing from here
if __name__ == '__main__':
    main()