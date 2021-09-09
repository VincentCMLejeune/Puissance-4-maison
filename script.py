board = []
for i in range(7):
  row = []
  for j in range(7):
    row.append(".")
  board.append(row)

def print_board(board):
  print(" 1 2 3 4 5 6 7")
  for i in range(7):
    line = "|"
    for j in board[i]:
      if j == "X":
        line += "X|"
      elif j == "O":
        line += "O|"
      else:
        line += " |"
    print(line)
  print("+-+-+-+-+-+-+-+")

def add_piece(board, pawn):
  str_row = input("Please enter a row (1-7) \n> ")
  row = int(str_row) - 1
  try:
    test = row*2
  except:
    print("ERROR : write a number")
  else:
    if row < 0 or row > 6:
      print("ERROR : index out of range")
      return -1
    if board[0][row] != ".":
      print("ERROR : row already full")
      return -1
    else:
      for i in range(6, -1, -1):
        if board[i][row] == ".":
          board[i][row] = pawn
          break

def board_full(board)

for i in range(7):
  board[i][3] = "O"
for i in range(6, 2, -1):
  board[i][4] = "X"
board[6][2] = "X"

print(board)
print("\n")
print_board(board)
print("\n")



  




add_piece(board, "X")

print("\n")
print(board)
print("\n")
print_board(board)