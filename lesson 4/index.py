import random
from colorama import Fore,init  
init(autoreset=True)  
board = [" "]*9
def show_board():
     for i  in range (0,9,3):
        row=[]
        for j in range(3):
               cell = board[i+j]
               if cell == "x":
                    row.append(Fore.GREEN+"x")
               elif cell == "o":
                    row.appened(Fore.GREEN+"o")
               else:
                    row.append(str(i+j+1))
        print(" | ".join(row))
        if i < 6 :
             print("--+---+--")
def check_winner(player): 
     wins = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
     for a, b, c, in wins:
          if board[a]==board[b]==board[c]== player:
               return True
     return False
print(Fore.CYAN+"tic tac toe game")
print("you are x and the computer is o\n")
for turn in range(9):
     show_board()
     if turn % 2==0:
          move =int(input(Fore.YELLOW +"\nEnter your move (1-9)"))-1
          while board[move] !=" ":
               move=int(input("try again :"))-1
          board[move]="x"
          if check_winner("x"):
               show_board()
               print(Fore.GREEN +"\nyou win!")
               break
     else:
          move= random.choice([i for i in range(9) if board[1]==" "])
          board[move]= "o"
          print(Fore.BLUE + f"\ncomputer chose{move+1}")
          if check_winner("o"):
               show_board()
               print(Fore.RED +"\ncomputer wins !")
               break
else:
    show_board()
    print(Fore.CYAN+"\nits a draw!")
                              
