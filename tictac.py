

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
    print_board()

    while True:
        place=int(input("PLAYER X: please choose a number from 1 to 9: "))-1
        try:    #start of try block, to create a custom message instead of ending up with an error
            if 0<=place<=8 and board[place]=="-":
                board[place]=player_x
                break

            else:
                print("invalid choice")
        except ValueError: #end of try block
            print("please select a valid number")



#player O's turn
def player_o_turn():

    print_board()
    while True:
        place=int(input("PLAYER O: please choose a number from 1 to 9: "))-1
        try:    #try block, same as player x
            if 0<=place<=8 and board[place]=="-":
                board[place]=player_o
                break

            else:
                print("invalid choice")
        except ValueError: #end of try except block
            print("please select a valid number")

#AI program
def bot():
    print_board()
    for place in range(len(board)):
        if board[4]=="-": #if the center is empty, take it
            board[4]=player_o
            break

        elif board[0]=="-": #if top left corner is empty, take it
            board[0]=player_o
            break

        elif board[2]=="-": #if top right corner is empty, take it
            board[2]=player_o
            break

        elif board[6]=="-": #if bottom left corner is empty, take it
            board[6]=player_o
            break

        elif board[8]=="-": #if bottom right corner is empty, take it
            board[8]=player_o
            break

        else:       #otherwise, take the nearest empty spot
            board[place]=player_o
            break

    #end of AI program



def win_check(): #check if win conditions are fulfilled
    global game_running
    for square in board:
        #horizontal start
        for i in [0, 3, 6]: #0, 3, 6 are the indexes of the first horizontal squares
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

    turn_count=0

    ai=input("VS mode | AI mode").lower()

    #vs AI mode
    if ai=="ai" or ai=="ai mode" or ai==" ai" or ai==" ai mode":
        while game_running==True:

            if turn:
                player_x_turn()
                win_check()
                turn=False
                turn_count+=1
                print(f"TURN: {turn_count}")


            else:
                bot()
                win_check()
                turn=True
                turn_count+=1
                print(f"TURN: {turn_count}")

    #vs human mode
    else:
        while game_running==True:

            if turn:
                player_x_turn()
                win_check()
                turn=False
                turn_count+=1
                print(f"TURN: {turn_count}")

            else:
                player_o_turn()
                win_check()
                turn=True
                turn_count+=1
                print(f"TURN: {turn_count}")

    print_board()

    retry=input("wanna try again? ").lower()
    if retry=="yes" or retry =="y":
        game_running=True
        game_start()

    elif retry=="no" or retry=="no":
        game_running=False
        print("see ya!")


game_start()

















