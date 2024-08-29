def print_board(board):
    for index, item in enumerate(board):
        if (index % 3 == 0):
            print()
        else:
            print(item)


def board_checker(board):
    for item in board:
        for placement in item:
            if placement.isaplha():
                continue
            else:
                return False
    return True


def turns(board):
    for i in range(9):
        turn = int(input("Enter the choice: "))
        board[turn-1] = "X"


board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

# player1_turn = int(
#     input("PLayer-1, Enter your choice b/w (1 - 9): ").upper())
# PLayer2 = input("PLayer-2, Enter your choice b/w (1 - 9): ")

print_board(board)

while (board_checker(board) != True):

    turn = input("Enter you choice b/w (1 - 9): ")
    if (board[turn]).isaplha():
        print("The vacancy is already aquired!")
        continue
    else:
        board[turn] == "X"
