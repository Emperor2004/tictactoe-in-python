__author__ = 'bma'

field = [[".", ".", "."],
         [".", ".", "."],
         [".", ".", "."]]

def displayField():
    for x in field:
        print(x[0], x[1], x[2])
        
def check_win():
    for row in range(0,3):
        if (field[row][0] == field[row][1] == field[row][2]) and (field[row][0] != "."):
            winner = field[row][0]
            print(winner,"won")
            exit()
    
    for col in range(0,3):
        if (field[0][col] == field[1][col] == field[2][col]) and (field[0][col] != "."):
            winner = field[0][col]
            print(winner,"won")
            exit()
    
            
    if (field[0][0] == field[1][1] == field[2][2]) and (field[0][0] != "."):
        winner = field[0][0]
        print(winner,"won")
        exit()
    
        
    if (field[2][2] == field[1][1] == field[0][0]) and (field[2][2] != "."):
        winner = field[2][2]
        print(winner,"won")
        exit()
    
        

def Xturn():
    print("X Turn")
    a = int(input("Please write number of your row: "))
    b = int(input("Please write number of your column: "))
    field [a-1][b-1] = "X"
    displayField()
    check_win()

def Oturn():
    print("0 Turn")
    a = int(input("Please write number of your row: "))
    b = int(input("Please write number of your column: "))
    field [a-1][b-1]= "0"
    displayField()
    check_win()

displayField()
while True:
    Xturn()
    Oturn()
