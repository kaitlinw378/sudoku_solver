class Board:
    def __init__(self):
        #Initializes an empty board array
        import numpy as np
        self.board = np.zeros((9,9))
        self.visited = []
        self.stack = [(8,0),(7,0),(6,0),(5,0),(4,0),(3,0),(2,0),(1,0),(0,0)]

    """
    check_rcg inputs:
    self - referring to the board object
    v - a value that needs to be checked
    r - a row index
    c - a column index 

    check_rcg outputs:
    False - the value was found within the given row,col or corr 3x3 grid
    True - the value was not found in the given row,col or corr 3x3 grid
    """
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

    """
    get_next_zero inputs:
    self - referring to the board object
    r - a row index
    c - a column index 

    get_next_zero outputs:
    False - there are no more 0s found in the board
    (i,j) - the index of the next 0 found in the board
    """
    def get_next_zero(self,r,c):
        #Returns the next zero found within the board if any
        if c >= 8 and r >= 8:
            r = 0
            c = 0
        elif c >= 9:
            c = 0
            r += 1
        elif c>=8 and r <= 8:
            c = 0
        for i in range(9):
            for j in range(9):
                if self.board[i,j] == 0 and j >= c and i >= r:
                    return (i,j)
        return False

    """
    dfs inputs:
    self - referring to the board object 

    dfs outputs:
    False - the potential solution did not work - must go back and try again
    True - the potential solution did work. If board complete end search, if not search next
    """
    def dfs(self):
        #Depth first seach algorithm adapted to solve sudoku puzzle
        if len(self.stack) > 0:
            if self.stack[len(self.stack)-1] == False:
                self.stack.pop()
            (r,c) = self.stack.pop()
        if not self.get_next_zero(r,c):
            return True
        for i in range(9):
            for j in range(9):
                if self.board[i,j] == 0 and i>=r and j>=c:
                    self.visited.append((i,j))
                    next = self.get_next_zero(i,j+1)
                    if next:
                        self.stack.append((next[0],next[1]))
                    for n in range(1,10):
                        if self.check_rcg(i,j,n):
                            self.board[i,j] = n
                            if self.dfs():
                                return True
                            self.visited.append((r,c))
                            self.stack.pop()
                            self.stack.append(next)
                    self.visited.pop()
                    if len(self.stack) > 0:
                        self.stack.pop()
                    (r,c) = self.visited.pop()
                    self.board[(r,c)] = 0
                    self.stack.append((r,c))
                    return False
        return False

    """
    set_board inputs:
    self - referring to the board object
    dict - a dictionary containing initialization values for a new puzzle

    set_board outputs:
    none - set_board fills the board with the initial values and returns nothing
    """
    def set_board(self,dict):
        #Takes an input dictionary and initializes the board
        for key, value in dict.items():
            self.board[key] = value

    """
    print_user_friendly_boardinputs:
    self - referring to the board object

    print_user_friendly_board outputs:
    none - function prints the board in a way that is easy for user to visualize
    """
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

    """
    solve_board inputs:
    self - referring to the board object
    dict - a dictionary containing initialization values for a new puzzle

    solve_board outputs:
    none - function calls initialization function, solve function, and prints the unsolved & solved board
    """
    def solve_board(self,dict):
        #Creates sudoku board using an unzolved puzzle input and calls solve function
        self.set_board(dict)
        print("unsolved board:")
        self.print_user_friendly_board()
        self.dfs()
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
