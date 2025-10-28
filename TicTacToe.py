board = [" "]*9
currentPlayer = "X"
gameOver = False


def create(board):
    #creates the board
    print(f"\n  {board[0]} | {board[1]} | {board[2]}")
    print(" ---+---+---")
    print(f"  {board[3]} | {board[4]} | {board[5]}")
    print(" ---+---+---")
    print(f"  {board[6]} | {board[7]} | {board[8]}\n")



def get_move(plr,board):
    while True:
        try:
            #checks if move is valid and returns move to be put in board
            move = int(input(f"{plr} enter your move (1-9): ")) - 1
            if 0<= move <= 8 and board[move] == " ":
                return move
            else:
                print("That is not a valid move")
        except ValueError:
            print("That is not a valid move")



def check_win(plr,board):
    #all possible win conditions of tic-tac-toe
    winConditions = [
        (0,1,2),(3,4,5),(6,7,8),
        (0,3,6),(1,4,7),(2,5,8),
        (0,4,8),(2,4,6)
    ]
    #checks if either X or O has fufilled any of the conditions
    for combination in winConditions:
        if board[combination[0]] == board[combination[1]]==board[combination[2]] != " ":
            return combination



def play_game(board):
    global currentPlayer, gameOver

    #initializes a labeled board for better user experience
    print("TicTacToe!")
    create(["1","2","3","4","5","6","7","8","9"])

    while not gameOver:
        move = get_move(currentPlayer,board)

        #adds the current players move to the board
        board[move] = currentPlayer
        create(board)

        #checks for a win
        result = check_win(currentPlayer,board)

        #if result exists then the winning player is displayed
        if result:
            print(f"Player {currentPlayer} wins!")
            gameOver = True
        if " " not in board and not result: #if result does not exist and the board is full then its a tie
            print(f"Its a tie!")
            gameOver = True

        #switches players
        if currentPlayer == "X":
            currentPlayer = "O"
        else:
            currentPlayer = "X"


play_game(board)

