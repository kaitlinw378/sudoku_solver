class Board:
    def __init__(self):
        #Initializes an empty board array
        import numpy as np
        self.board = np.zeros((9,9))

    def check_rcg(self,r,c,v):
        #Checks if a given value (v) is in a row,col and 3x3 grid

        #Check if v is in row (r)
        for i in range(9):
            if self.board[r,i] == v:
                return False

        #Check if v is in col (c)
        for i in range(9):
            if self.board[i,c] == v:
                return False
        
        #r1,r2,r3 are the three rows found within a 3x3 grid
        r1 = []
        r2 = []
        r3 = []
        rc = r//3
        if rc == 0:
            rc = 0
        elif rc == 1:
            rc = 3
        elif rc == 2:
            rc = 6
        if c//3 == 0:
            r1 = self.board[rc,c//3:c//3+3]
            r2 = self.board[rc+1,c//3:c//3+3]
            r3 = self.board[rc+2,c//3:c//3+3]
        elif c//3 == 1:
            r1 = self.board[rc,c//3+2:c//3+5]
            r2 = self.board[rc+1,c//3+2:c//3+5]
            r3 = self.board[rc+2,c//3+2:c//3+5]
        elif c//3 == 2:
            r1 = self.board[rc,c//3+4:c//3+7]
            r2 = self.board[rc+1,c//3+4:c//3+7]
            r3 = self.board[rc+2,c//3+4:c//3+7]
        #Check if v is in the 3x3 grid
        if v in r1 or v in r2 or v in r3:
            return False
        
        return True

    def verify_board(self):
        #Checks if the board is complete solved or not
        for i in range(9):
            for j in range(9):
                if self.board[i,j] == 0:
                    return (True,i,j)

        for i in range(9):
            for j in range(9):
                if not self.check_rcg(i,j,self.board[i,j]):
                    return False
        return False
    
    def solve(self):
        #Solves entire puzzle
        a = self.verify_board()
        if not self.verify_board():
            return True
        for n in range(1,10):
            if self.check_rcg(a[1],a[2],n):
                self.board[a[1],a[2]] = n
                if self.solve():
                    return True
                self.board[a[1],a[2]] = 0
        return False

    def set_board(self,dict):
        #Takes an input dictionary and initializes the board
        for key, value in dict.items():
            self.board[key] = value

    def print_user_friendly_board(self):
        #Prints a version of the board that is easy for users to see
        line = "----------------------------------"
        print(line)
        rc = 1
        for i in range(9):
            v1 = str(self.board[i,0:3]).strip("[").strip("]")
            v2 = str(self.board[i,3:6]).strip("[").strip("]")
            v3 = str(self.board[i,6:9]).strip("[").strip("]")
            s = "| " + v1 + " | " + v2 + " | " + v3 + " | "
            print(s)
            if rc == 3:
                print(line)
                rc = 0
            rc += 1

    def solve_board(self,dict):
        #Creates sudoku board using an unzolved puzzle input and calls solve function
        self.set_board(dict)
        print("unsolved board:")
        self.print_user_friendly_board()
        self.solve()
        print("solved board:")
        self.print_user_friendly_board()

problem1 = {(0,2):3,(0,4):2,(0,6):6,(1,0):9,(1,3):3,(1,5):5,(1,8):1,(2,2):1,
            (2,3):8,(2,5):6,(2,6):4,(3,2):8,(3,3):1,(3,5):2,(3,6):9,(4,0):7,
            (4,8):8,(5,2):6,(5,3):7,(5,5):8,(5,6):2,(6,2):2,(6,3):6,(6,5):9,
            (6,6):5,(7,0):8,(7,3):2,(7,5):3,(7,8):9,(8,2):5,(8,4):1,(8,6):3}

problem2 = {(0,2):6,(0,3):7,(1,0):3,(1,2):2,(1,3):5,(1,6):8,(2,0):1,(2,7):2,
            (2,8):4,(3,4):2,(3,6):9,(4,0):8,(4,2):1,(4,5):4,(4,6):2,(4,7):7,
            (5,3):1,(5,5):7,(6,6):3,(7,0):7,(7,3):8,(7,4):5,(7,6):6,(8,7):4,
            (8,8):9}

problem3 = {(0,1):2,(0,3):5,(1,3):6,(1,4):2,(1,8):9,(2,4):9,(2,5):8,(2,6):5,
            (2,8):6,(3,0):5,(3,3):3,(3,5):9,(3,7):4,(4,0):3,(4,6):1,(5,0):1,
            (5,1):9,(5,3):4,(5,6):8,(5,8):3,(6,4):3,(7,0):7,(7,5):1,(7,8):8,
            (8,1):8,(8,3):9,(8,4):7,(8,5):4}

b = Board()
b.solve_board(problem1)
