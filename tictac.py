

#global variable definitions
board=["-", "-","-",
        "-", "-", "-",
        "-", "-", "-"]


player_x="X"
player_o="O"

game_running=True

turn=True

#print game board to terminal
def print_board():
    print(board[0]+" | "+board[1]+" | "+board[2])
    print("---------")
    print(board[3]+" | "+board[4]+" | "+board[5])
    print("---------")
    print(board[6]+" | "+board[7]+" | "+board[8])

#player x's turn
def player_x_turn():
    #os.system("cls")
    print_board()

    while True:
        place=int(input("PLAYER X: please choose a number from 1 to 9: "))-1
        try:
            if 0<=place<=9 and board[place]=="-":
                board[place]=player_x
                break

            else:
                print("invalid choice")
        except ValueError:
            print("please choose a valid number that is not taken")



#player O's turn
def player_o_turn():
    #os.system("cls")
    print_board()
    while True:
        place=int(input("PLAYER O: please choose a number from 1 to 9: "))-1
        try:
            if 0<=place<=9 and board[place]=="-":
                board[place]=player_o
                break

            else:
                print("invalid choice")
        except ValueError:
            print("please print a valid number that is not taken")


def win_check():
    global game_running
    for square in board:
        #horizontal start
        for i in [0, 3, 6]:
            if board[i]==board[i+1]==board[i+2] and board[i]!="-":
                print(board[i], "WINS")
                game_running=False
                return
        #horizontal end

        #vertical start
        for i in [0, 1, 2]:
            if board[i]==board[i+3]==board[i+6] and board[i]!="-":
                print(board[i], "WINS")
                game_running=False
                return
        #vertical end

        #diagonal start
        if board[0]==board[4]==board[8] and board[0]!="-":
            print(board[0], "WINS")
            game_running=False
            return

        if board[2]==board[4]==board[6] and board[4]!="-":
            print(board[2], "WINS")
            game_running=False
            return

        if "-" not in board:
            print("DRAW")
            game_running=False
            return

#win check complete


#main game
def game_start():
    global game_running, board, turn

    board=["-", "-","-",
        "-", "-", "-",
        "-", "-", "-"]
    game_running=True

    while game_running==True:

        if turn:
            player_x_turn()
            win_check()
            turn=False

        else:
            player_o_turn()
            win_check()
            turn=True

    retry=input("wanna try again? ").lower()
    if retry=="yes" or retry =="y":
        game_running=True
        game_start()

    elif retry=="no" or retry=="no":
        game_running=False
        print("see ya!")




















