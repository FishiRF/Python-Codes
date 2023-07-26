import random
def build_board():
    # This function creates the Tic Tac Toe board with empty cells ("_").
    board = [["_" for i in range(3)] for j in range(3)]
    # b=[]
    # for i in range(3):
    #     b.append([])
    #     for j in range(3):
    #         b[i].append('-')
    #
    # print(b)
    return board

def print_board(board):
    # This function prints the current state of the Tic Tac Toe board.
    for row in board:
        print(row)

def legal_input(board, row, col):
    # This function checks if the input (row, col) is legal.
    if 0 <= row <= 2 and 0 <= col <= 2 and board[row][col] == "_":
        return True
    else:
        return False

def switch_user(current_user, player1_name, player2_name):
    # This function switches the current user between the two players.
    if current_user == player1_name:
        return player2_name
    else:
        return player1_name

def check_winner(board, player):
    # This function checks if the given player has won the game.
    # We check for three in a row horizontally, vertically, and diagonally.
    for i in range(3):
        if all(board[i][j] == player for j in range(3)):  # Check horizontally
            return True
        if all(board[j][i] == player for j in range(3)):  # Check vertically
            return True
    if all(board[i][i] == player for i in range(3)):  # Check diagonally (top-left to bottom-right)
        return True
    if all(board[i][2 - i] == player for i in range(3)):  # Check diagonally (top-right to bottom-left)
        return True
    return False

def check_tie(board):
    # This function checks if the game is a tie (no winner and the board is full).
    for row in board:
        for cell in row:
            if cell == "_":
                return False
    return True

def get_player_names():
    # This function asks for and returns the names of the two players.
    player1_name = input("Enter the name of Player 1: ")
    player2_name = input("Enter the name of Player 2: ")
    return player1_name, player2_name

def main():    # main code for the game
    print("Welcome to Tic Tac Toe!")
    player1_name, player2_name = get_player_names()
    current_player = random.choice([player1_name, player2_name])    # Randomly decide which player goes
                                                                    # first and which one goes second
    while True:
        board = build_board()
        print_board(board)
        for i in range(9):  # The game can have a maximum of 9 moves
            print(f"{current_player}, it's your turn.")
            while True:     # Get user input for row and column
                row = int(input("Enter the row (0, 1, or 2): "))
                col = int(input("Enter the column (0, 1, or 2): "))
                if legal_input(board, row, col):
                    break
                else:
                    print("Illegal move. Try again.")
            board[row][col] = "X" if current_player == player1_name else "O"
            print_board(board)
            if check_winner(board, "X"):
                winner_name = player1_name
                print(f"Congratulations {winner_name}, you win!")
                break
            elif check_winner(board, "O"):
                winner_name = player2_name
                print(f"Congratulations {winner_name}, you win!")
                break
            if check_tie(board):
                print("It's a tie!")
                break
                # Switch to the other player
            current_player = switch_user(current_player, player1_name, player2_name)
        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() != "yes":
            break
if __name__ == "__main__":
    main()
