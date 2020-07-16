#Import any python modules 
import random

#A class to initialize createboard:
class createBoard:

    def __init__(self,row,column):#constructor
        self.createboard= []
        #for loops to print individual columns and rows
        for i in range(row):
            self.createboard.append([])
            for j in range(column):
                self.createboard[i].append(0) #add zeros in the place of []

        self.printBoard()

    def printBoard(self):
        print("The Board here: ")
        for list in self.createboard:

            print(list)
            #print('\n'): optional to start a new line

    def innitPattern(self,rows,cols):
        indexlist = []
        for i in range(0,rows): #nested loops
                for j in range(0,cols):
                    indexlist.append([i,j])
        #print(indexlist)
        #print a pentamino pattern: 5 coordinates
        pattern = random.sample(indexlist, 1)
        print(pattern)
        
        #functions called in another function
        self.patternChange(pattern)#important
        #self.check_neighbour(row,column)
        
    
    def patternChange(self,index):
        print("index", index)
        for p,q in index:
            self.createboard[p][q]= 1
            
        #functions called in another function:
        self.printBoard()   

      #FIND NEIGHBOURS

#A function to check neighbours, find where they are:
    def check_neighbours(self, index):
        listindex = [[1,1], [1,0], [0,1], [-1,0], [0,-1], [-1,-1], [-1,1], [1,-1]]
        for i,j in index:
            row = i
            column = j
            for element in listindex:
                row_inc, col_inc = elem[0], elem[1]
                new_row = row + row_inc
                new_row = int(new_row)
                new_column = column + col_inc
                new_column = int(new_column)
                if (new_row >=0) and (new_row < 10) and (new_row >= 0) and (new_column < 10):
                    print("neighbour index:", new_row, new-column)
                    print("index value: ")
                    print(self.createboard[new_row][new_column])
       
        
        
#main function: necessary, in complex problems
if __name__ == "__main__":
            row= 10
            column= 10
            #index = [0,10] not sure what to do here confused???
            board1 = createBoard(row,column)
            board1.innitPattern(row,column)
            board1.check_neighbours(index)
            
