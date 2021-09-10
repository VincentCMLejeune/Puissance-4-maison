def print_board(board):
  print("\n 1 2 3 4 5 6 7")
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
  checking = False
  while checking == False:
    str_row = input(f"Player {pawn}, please enter a row (1-7) \n> ")
    try:
      row = int(str_row) - 1
    except:
      print("ERROR : write a number")
      checking = False
      continue
    else:
      if row < 0 or row > 6:
        print("ERROR : index out of range")
        checking = False
        continue
      if board[0][row] != ".":
        print("ERROR : row already full")
        checking = False
        continue
    checking = True
  for i in range(6, -1, -1):
    if board[i][row] == ".":
      board[i][row] = pawn
      break

def board_full(board):
    for i in range(7):
        if board[0][i] == ".":
            return False
    print("Board full, game over")
    return True

def horizontal_win(board, pawn):
  for row in board:
    for j in range(4):
      if row[j] == pawn:
        if row[j+1] == pawn:
          if row[j+2] == pawn:
            if row[j+3] ==pawn:
              return True
  return False

def vertical_win(board, pawn):
  for i in range(4):
    for j in range(7):
      if board[i][j] == pawn:
        if board[i+1][j] == pawn:
          if board[i+2][j] == pawn:
            if board[i+3][j] == pawn:
              return True
  return False

def diagonal_down_win(board, pawn):
  for i in range(4):
    for j in range(4):
      if board[i][j] == pawn:
        if board[i+1][j+1] == pawn:
          if board[i+2][j+2] == pawn:
            if board[i+3][j+3] == pawn:
              return True
  return False

def diagonal_up_win(board, pawn):
  for i in range(3, 7):
    for j in range(4):
      if board[i][j] == pawn:
        if board[i-1][j+1] == pawn:
          if board[i-2][j+2] == pawn:
            if board[i-3][j+3] == pawn:
              return True
  return False

def check_winner(board, pawn):
  if horizontal_win(board, pawn) == True:
    print(pawn + " wins !")
    return True
  if vertical_win(board, pawn) == True:
    print(pawn + " wins !")
    return True
  if diagonal_down_win(board, pawn) == True:
    print(pawn + " wins !")
    return True
  if diagonal_up_win(board, pawn) == True:
    print(pawn + " wins !")
    return True
  return False

print("Welcome to Connect Four !")

replay = "yes"
while replay.lower() == "yes":
  board = []
  for i in range(7):
    row = []
    for j in range(7):
      row.append(".")
    board.append(row)
  print_board(board)
  print("\n")
  turn = 0
  piece = ""
  game_over = False

  while game_over == False:
    turn += 1
    if turn % 2 == 0:
      piece = "X"
    else:
      piece = "O"
    while add_piece(board, piece) == False:
      pass
    print_board(board)
    if board_full(board) == True:
      game_over = True
    if check_winner(board, "X") == True:
      game_over = True
    if check_winner(board, "O") == True:
      game_over = True
  
  replay = input("Do you want to play another game ? (answer yes if you do, anything else if you don't) \n> ")

print("Thanks for playing !")