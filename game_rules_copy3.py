#Functions that need to be imported:(using random.sample in my code)
import random
from copy import copy,deepcopy

#Class to initialize objects
class board:
    def __init__(self, row, col):#constructor
        self.board = []
        for i in range(row):
            self.board.append([])
            for j in range(col):
                self.board[i].append(0)
        self.printboard()
        

#This function allows us to print variables, objects,
    def printboard(self):
        print("Print board")
        for list in self.board:
            print(list)
            #print("\n")optional to my board

    def setPattern(self, ro, co):
        indexlist = []
        for i in range(0,ro):
            for j in range(0,co):
                indexlist.append([i,j])
        print(indexlist)
        self.pattern = random.sample(indexlist,1)
        print("Randomly chosen coordinates" + str(self.pattern))
        self.changepattern(self.pattern)

    def changepattern(self, index):
        print("index", index)
        for p,q in index:
            self.board[p][q] = 1
        self.printboard()
        self.check_neighbours(self.pattern)
   
    def check_neighbours(self,index):
        listIndex = [[1, 1], [1, 0], [0, 1], [-1, 0], [0, -1], [-1, -1], [-1, 1], [1, -1]]
        for i, j in index:
            row = i
            column = j
            for elem in listIndex:
                row_inc, col_inc = elem[0], elem[1]
                new_row = row + row_inc
                new_row = int(new_row)
                new_column = column + col_inc
                new_column = int(new_column)
                if (new_row >= 0) and (new_row < 10) and (new_column >= 0) and (new_column < 10):
                    print("neighbour index:", new_row, new_column)
                    print("index value: ")
                    print(self.board[new_row][new_column])
    # a code modified by the help of a computing programming friend
    def game_rules(self):
        updateBoard = deepcopy(self.board)
        x = 0
        while(x<100):
           for i in range(len(self.board)):
               for j in range(len(self.board[0])):
                    value = self.board[i][j]
           if(value == '1'):
               countAlive = copy.copy(self.board[new_row][new_column])#take neighbours??
               if countAlive == 2 or countAlive ==3:
                    updateBoard[i][j] = 1
               else:
                    updateBoard[i][j] = 0
           if(value == '0'):
               countAlive = copy.copy(self.board[new_row][new_column])#take neighbours??
               if countAlive == 3:
                    updateBoard[i][j] = 1
               else:
                    updateBoard[i][j] = 0          

       #Updating The Board Information
        print("The updated board with the rules applied:", updateBoard)

    # another method with the help of someone but did not fully copy so still mistakes. 
    """def game_rules(self,rows,cols):
        neighbors = [(1,0), (1,-1), (0,-1), (-1,-1), (-1,0), (-1,1), (0,1), (1,1)]
        rows = len(board)
        cols = len(board[0])
        
        update_board = [[self.board[row][col] for col in range(cols)] for row in range(rows)]

        for row in range(rows):
            for col in range(cols):
                live_neighbors = 0
                for neighbor in neighbors:
                    r = (row + neighbor[0])
                    c = (col + neighbor[1])
                    if (r < rows and r >= 0) and (c < cols and c >= 0) and (update_board[r][c] == 1):
                        live_neighbors += 1
                if update_board[row][col] == 1 and (live_neighbors < 2 or live_neighbors > 3):
                    board[row][col] = 0
                if update_board[row][col] == 0 and live_neighbors == 3:
                    board[row][col] = 1"""
#Main Function:
if __name__ == "__main__":
    row = 10
    column = 10
    board_ = board(row,column)
    #print("Moving to set pattern")optional to the code
    board_.setPattern(row,column)
    board_.game_rules()
   #board._game_rules(rows,cols)
