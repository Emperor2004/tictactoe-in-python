__author__ = 'bma'

field = [[".", ".", "."],
         [".", ".", "."],
         [".", ".", "."]]

def displayField():
    for x in field:
        print(x[0], x[1], x[2])

displayField()
def Xturn():
    print("X Turn")
    a = int(input("Please write number of your row: "))
    b = int(input("Please write number of your column: "))
    field [a-1][b-1] = "X"

def Oturn():
    print("0 Turn")
    a = int(input("Please write number of your row: "))
    b = int(input("Please write number of your column: "))
    field [a-1][b-1]= "0"


 # Hello, my friend dude
Xturn()
displayField()

Oturn()
displayField()
Xturn()
displayField()

Oturn()
displayField()
Xturn()
displayField()

Oturn()
displayField()
Xturn()
'''
board = range(1,10)

def draw_board(board):
    print ("-------------")
    for i in range(3):
        print ("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")
        print ("-------------")

draw_board(board)'''
