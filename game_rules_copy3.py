#Functions that need to be imported:(using random.sample in my code)
import random
import copy 


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
        print("Print board here:")
        for list in self.board:
            print(list)
            print("\n")#optional to my board
       
    #Randomly sets the pattern
    def setPattern(self, ro, col):
        indexlist = []
        for i in range(0,ro):
            for j in range(0,col):
                indexlist.append([i,j])

        #FUNCTIONS THAT ARE CALLED
        #print(indexlist)
        self.pattern = random.sample(indexlist,1)
        #print("Randomly chosen coordinates" + str(self.pattern))
        self.changepattern(self.pattern)

   #CREATING THE PATTERN
    def changepattern(self, index):
        print("index:", index)
        for p,q in index:
            self.board[p][q] = 1
        self.printboard()
        #self.check_neighbours(self.pattern)
   
    def check_neighbours(self,row,column):
        neighbourIndex = [[1, 1], [1, 0], [0, 1], [-1, 0], [0, -1], [-1, -1], [-1, 1], [1, -1]]
        list1=[]
        
        for elem in neighbourIndex:
                row_inc, col_inc = elem[0], elem[1]
                new_row = row + row_inc
                new_row = int(new_row)
                new_column = column + col_inc
                new_column = int(new_column)
                if (new_row >= 0) and (new_row < 5) and (new_column >= 0) and (new_column < 5):
                    #print("neighbour index:", new_row, new_column)
                   #print(" The index value: ")
                    #print(self.board[new_row][new_column])
                    list1.append(self.board[new_row][new_column])

                    
        self.game_rules(list1,row,column)        

    #Game Rules: 
    def game_rules(self,list1,row,column):
        
    #updating the board 
        self.update_board = copy.deepcopy(self.board)
        countAlive = list1.count(1)
        print("countAlive",countAlive)

            #Applying the Game Rules
        if self.board[row][column] == 1 and (countAlive < 2 or countAlive > 3):
            self.update_board[row][column] == 0
        else:
            self.update_board[row][column] == 1
        if self.board[row][column] == 0 and (countAlive == 3):
            self.update_board[row][column] == 1
        else:
            self.update_board[row][column] == 0

    
#Main Function:
if __name__ == "__main__":
    row = 5
    column = 5
    board_ = board(row,column)
    #print("Moving to set pattern")optional to the code
    board_.setPattern(row,column)
    x = 0
    while x < 2:
        for elem in range(0,row):
            for j in range(0,column):
                board_.check_neighbours(elem,j)
        board_.board = board_.update_board
        board_.printboard()
        x+= 1
            
 
