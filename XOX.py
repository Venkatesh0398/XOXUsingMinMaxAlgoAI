def analyseboard(board):
  win = [[0,1,2] , [3,4,5] , [6,7,8] , [0,3,6] , [1,4,7] , [2,5,8] , [0,4,8] , [2,4,6]]
  for i in range(0,8):
    if(board[win[i][0]] != 0 and
       board[win[i][0]] == board[win[i][1]] and
       board[win[i][1]] == board[win[i][2]]):
      return board[win[i][0]]

  return 0

def ConstBoard(board):
  print("The current state of the board: ")
  for i in range(0,9):
    if((i!=0) and (i%3==0)):
      print("\n")
    if(board[i] == 0):
      print("_ ", end=" ")
    if(board[i] == 1):
      print("O ", end=" ")
    if(board[i] == -1):
      print("X ", end=" ")

  print("\n\n")

def User1Turn(board):
  pos = input("Enter 'X' pos [1-9]: ")
  pos = int(pos)
  if(board[pos-1]!=0):
    print("Wrong move!")
    exit(0)
  board[pos-1] = -1

def User2Turn(board):
  pos = input("Enter 'O' pos [1-9]: ")
  pos = int(pos)
  if(board[pos-1]!=0):
    print("Wrong move!")
    exit(0)
  board[pos-1] = 1

def minmax(board, player):
  x = analyseboard(board)
  if(x != 0):
    return (x * player)
  pos = -1
  value = -2
  for i in range (0,9):
    if(board[i] == 0):
      board[i] = player
      score = -minmax(board, -player)
      board[i] = 0
      if(score > value):
        value = score
        pos = i
  if(pos == -1):
    return 0
  return value

def CompTurn(board):
  pos = -1
  value = -2
  for i in range (0,9):
    if(board[i] == 0):
      board[i] = 1
      score = -minmax(board,-1)
      board[i] = 0
      if(score > value):
        value = score
        pos = i
  board[pos] = 1

def main():
  choice = input("Enter 1 for Single-Player or 2 for Multi-Player")
  choice = int(choice)
  board = [0, 0, 0, 0, 0, 0, 0, 0 , 0]
  if(choice==1):
    print("Computer 'O' vs You 'X': \n")
    player = input("Enter to play 1st('1') or 2nd('2'): ")
    player = int(player)
    for i in range(0,9):
      if(analyseboard(board) != 0):
        break
      if((i+player)%2 == 0):
        CompTurn(board)
      else:
        ConstBoard(board)
        User1Turn(board)

  else:
    for i in range(0,9):
      if(analyseboard(board) != 0):
        break
      if(i%2 == 0):
        ConstBoard(board)
        User1Turn(board)
      else:
        ConstBoard(board)
        User2Turn(board)

  if(analyseboard(board) == 0):
    print("Draw!")
  elif(analyseboard(board) == -1):
    print("Player-1 has won!")
  else:
    print("Player-2 has won!")

main()
