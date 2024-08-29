def print_board(board):
    for index, item in enumerate(board):
        print(index, item)
        if index+1 % 3 == 0:
            print("\n")
        else:
            print(item, end=" ")

board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

print_board(board)




# turns(board)
