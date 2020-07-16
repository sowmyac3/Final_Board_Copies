#Functions that need to be imported:(using random.sample in my code)
import random

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




if __name__ == "__main__":
    row = 10
    column = 10
    board_ = board(row,column)
    #print("Moving to set pattern")optional to the code
    board_.setPattern(row,column)
