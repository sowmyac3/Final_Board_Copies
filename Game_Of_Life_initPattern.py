#Functions that need to be imported:(using random.sample in my code)
import random
from copy import copy, deepcopy

#Class to initialize objects
class board:

    #Constructor Function - initializing the self.board here 
    def __init__(self, row, column):
        self.board = []
        for i in range(row):
            self.board.append([])
            for j in range(column):
                self.board[i].append(0)
        self.printboard()
        

   #Print Function - prints the board
    def printboard(self):
        print("Print board:")
        for list in self.board:
            print(list)
            #print("\n")#optional to my board
       
    def InputsetPattern(self,ro,col):
        self.pattern = []
        countIndex = int(input("How many indexes would you like to input: "))

        for i in range(countIndex):
            self.pattern.append([])
            xValue = int(input("Please input row value: "))
            yValue = int(input("Please input column value: "))
            self.pattern[i].append(int(xValue))
            self.pattern[i].append(int(yValue))

        print(self.pattern)
        self.changepattern(self.pattern)



   #CREATING THE PATTERN
    def changepattern(self, index):
        print("index:", index)
        for p,q in index:
            self.board[p][q] = 1
        self.printboard()
        self.game_rules()
   
    def check_neighbours(self,i,j):
        neighbourIndex = [[1, 1], [1, 0], [0, 1], [-1, 0], [0, -1], [-1, -1], [-1, 1], [1, -1]]
        self.list1=[]
        row = i
        column = j
        
        for elem in neighbourIndex:
                row_inc, col_inc = elem[0], elem[1]
                new_row = row + row_inc
                new_row = int(new_row)
                new_column = column + col_inc
                new_column = int(new_column)
                if (new_row >= 0) and (new_row < 10) and (new_column >= 0) and (new_column < 10): #change this when updating the board size**
                    #print("neighbour index:", new_row, new_column)
                   #print(" The index value: ")
                    #print(self.board[new_row][new_column])
                    self.list1.append(self.board[new_row][new_column])
       

    #Game Rules: 
    def game_rules(self):
        x = 15
        for y in range(x): 
            self.update_board = deepcopy(self.board)
            for i in range(len(self.board)):
                for j in range(len(self.board[0])):
                    value = self.board[i][j]
                    if (value == 1):
                        self.check_neighbours(i,j)
                        countAlive = self.list1.count(1)
                        countDead = self.list1.count(0)
                        if countAlive == 2 or countAlive == 3:
                            self.update_board[i][j] = 1
                        else:
                            self.update_board[i][j] = 0
                    if (value == 0):
                        self.check_neighbours(i,j)
                        countAlive = self.list1.count(1)
                        countDead = self.list1.count(0)
                        if countAlive == 3:
                            self.update_board[i][j] = 1
                        else:
                            self.update_board[i][j] = 0
            self.board = self.update_board
            self.printboard()
                        
#Main Function:
if __name__ == "__main__":
    row = 10 #remember to change this to change board size
    column = 10 #remember to change this to change board size
    board_ = board(row,column)
    print("Moving to set pattern")#optional to the code
    #board_.setPattern(row,column)
    board_.InputsetPattern(row,column)
    board_.printboard()
       
   
