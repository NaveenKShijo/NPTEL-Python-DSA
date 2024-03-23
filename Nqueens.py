
def initialize(num):
    """ This function creates a chess board on which 'queens' are put """
    board['queens'] = {}
    board['rows'] = {}
    board['columns'] = {}
    board['decDiag'] = {}
    board['incDiag'] = {}
    for i in range(0,num):
        board['rows'][i] = 0
        board['columns'][i] = 0
        board['queens'][i] = -1
    for i in range(-(num-1), num):
        board['decDiag'][i] = 0
    for i in range(0,(2*num)+1):
        board['incDiag'][i] = 0

def free(i,j):
    """ To check whether the cell(i,j) is free from the attacks of any queen """
    return (board['rows'][i] == 0 and board['columns'][j] == 0 and board['decDiag'][j-i] == 0 and board['incDiag'][j+i] == 0)

def addQueen(i,j):
    """To add queen into a cell(i,j) """
    board['queens'][i] = j
    board['rows'][i] = 1
    board['columns'][j] =1
    board['decDiag'][j-i] =1
    board['incDiag'][j+i] =1

def undoQueen(i,j):
    """This function is for making the cell(i,j) free """
    board['queens'][i] = -1
    board['rows'][i] = 0
    board['columns'][j] = 0
    board['decDiag'][j-i] = 0
    board['incDiag'][j+i] = 0

def placeQueens(i):
    """ This function recieves the 'rows''s no. as parameter and manages the handling of 'queens' in the chess board"""
    global size
    for j in range(0,size):
        if(free(i,j)):
            addQueen(i,j)
            if(i == size-1):
                return True
            else:
                extSol = placeQueens(i+1)
                if(extSol):
                    return True
                else:
                    undoQueen(i,j)
    return False

def printBoard():
    global size
    for i in range(0,size):
        print(i,board['queens'][i])


board = {}
size = int(input("Enter the No. of queens"))
initialize(size)
if(placeQueens(0)):
    printBoard()