import random


def create_board():
    return [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]


def display_board(board):
    for row in board:
        print(" | ".join(str(cell) for cell in row))


def player_move(board):

    while True:

        try:
            move = int(input("Enter your move (1-9): "))

            if move < 1 or move > 9:
                print("Enter a number between 1-9")
                continue

            move -= 1

            row = move // 3
            col = move % 3


            if board[row][col] not in ['O', 'X']:
                board[row][col] = 'O'
                break

            else:
                print("Field already occupied!")

        except ValueError:
            print("Please enter a number!")


def computer_move(board):

    empty = []

    for row in range(3):
        for col in range(3):

            if board[row][col] not in ['O', 'X']:
                empty.append((row, col))


    row, col = random.choice(empty)

    board[row][col] = 'X'


def check_winner(board):

    # rows
    for row in range(3):

        if board[row][0] == board[row][1] == board[row][2] \
        and board[row][0] in ['O', 'X']:

            return board[row][0]


    # columns
    for col in range(3):

        if board[0][col] == board[1][col] == board[2][col] \
        and board[0][col] in ['O', 'X']:

            return board[0][col]


    # diagonal 1
    if board[0][0] == board[1][1] == board[2][2] \
    and board[0][0] in ['O', 'X']:

        return board[0][0]


    # diagonal 2
    if board[0][2] == board[1][1] == board[2][0] \
    and board[0][2] in ['O', 'X']:

        return board[0][2]


    return None



def is_draw(board):

    for row in board:

        for cell in row:

            if cell not in ['O', 'X']:
                return False

    return True



# -------- GAME START --------


while True:

    board = create_board()

    winner = None


    while True:

        display_board(board)

        player_move(board)

        winner = check_winner(board)


        if winner:
            display_board(board)
            break


        if is_draw(board):
            display_board(board)
            break



        computer_move(board)

        winner = check_winner(board)


        if winner:
            display_board(board)
            break


        if is_draw(board):
            display_board(board)
            break



    # result

    if winner == "X":
        print("Computer wins!")

    elif winner == "O":
        print("You win!")

    else:
        print("It's a tie!")


    again = input("Do you want to play again? (y/n): ")


    if again.lower() != "y":
        print("Thanks for playing!")
        break