class Board:
    def __init__(self):
        import numpy as np
        # self.num_count = {1:4,2:5,3:4,4:1,5:3,6:4,7:2,8:5,9:4}
        self.num_count = {1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}
        # self.num_count = {1:5,2:2,3:4,4:6,5:3,6:3,7:4,8:6,9:5}
        self.total_sum = 0
        self.board = np.zeros((9,9))
        # self.board[0,2] = 3
        # self.board[0,4] = 2
        # self.board[0,6] = 6
        # self.board[1,0] = 9
        # self.board[1,3] = 3
        # self.board[1,5] = 5
        # self.board[1,8] = 1
        # self.board[2,2] = 1
        # self.board[2,3] = 8
        # self.board[2,5] = 6
        # self.board[2,6] = 4
        # self.board[3,2] = 8
        # self.board[3,3] = 1
        # self.board[3,5] = 2
        # self.board[3,6] = 9
        # self.board[4,0] = 7
        # self.board[4,8] = 8
        # self.board[5,2] = 6
        # self.board[5,3] = 7
        # self.board[5,5] = 8
        # self.board[5,6] = 2
        # self.board[6,2] = 2
        # self.board[6,3] = 6
        # self.board[6,5] = 9
        # self.board[6,6] = 5
        # self.board[7,0] = 8
        # self.board[7,3] = 2
        # self.board[7,5] = 3
        # self.board[7,8] = 9
        # self.board[8,2] = 5
        # self.board[8,4] = 1
        # self.board[8,6] = 3

        self.board[0,2] = 6
        self.board[0,3] = 7
        self.board[1,0] = 3
        self.board[1,2] = 2
        self.board[1,3] = 5
        self.board[1,6] = 8
        self.board[2,0] = 1
        self.board[2,7] = 2
        self.board[2,8] = 4
        self.board[3,4] = 2
        self.board[3,6] = 9
        self.board[4,0] = 8
        self.board[4,2] = 1
        self.board[4,5] = 4
        self.board[4,6] = 2
        self.board[4,7] = 7
        self.board[5,3] = 1
        self.board[5,5] = 7
        self.board[6,6] = 3
        self.board[7,0] = 7
        self.board[7,3] = 8
        self.board[7,4] = 5
        self.board[7,6] = 6
        self.board[8,7] = 4
        self.board[8,8] = 9

        for v in self.board:
            for i in v:
                self.total_sum = self.total_sum + i

        for v in self.board:
            for i in v:
                if i > 0:
                    self.num_count[i] += 1
        print(self.total_sum)
        print(self.num_count)

        # self.board[0,0] = 4
        # self.board[0,2] = 7
        # self.board[0,3] = 8
        # self.board[0,5] = 5
        # self.board[0,8] = 9
        # self.board[1,2] = 3
        # self.board[1,3] = 7
        # self.board[1,5] = 1
        # self.board[1,7] = 5
        # self.board[2,1] = 1
        # self.board[2,4] = 4
        # self.board[2,6] = 7
        # self.board[2,7] = 8
        # self.board[2,8] = 6
        # self.board[3,0] = 1
        # self.board[3,2] = 2
        # self.board[3,7] = 7
        # self.board[3,8] = 4
        # self.board[4,1] = 9
        # self.board[4,2] = 8
        # self.board[4,3] = 4
        # self.board[4,4] = 3
        # self.board[5,1] = 6
        # self.board[5,3] = 9
        # self.board[5,4] = 1
        # self.board[5,6] = 8
        # self.board[5,8] = 5
        # self.board[6,7] = 4
        # self.board[7,0] = 3
        # self.board[7,2] = 9
        # self.board[7,5] = 8
        # self.board[7,6] = 6
        # self.board[8,0] = 2
        # self.board[8,3] = 3
        # self.board[8,5] = 4
        # self.board[8,6] = 1
        # self.board[8,7] = 9
        # self.board[8,8] = 8

    def check_square(self,r,c,n):
        r1 = []
        r2 = []
        r3 = []
        if c//3 == 0:
            r1 = self.board[r,c//3:c//3+3]
            r2 = self.board[r+1,c//3:c//3+3]
            r3 = self.board[r+2,c//3:c//3+3]
        elif c//3 == 1:
            r1 = self.board[r,c//3+2:c//3+5]
            r2 = self.board[r+1,c//3+2:c//3+5]
            r3 = self.board[r+2,c//3+2:c//3+5]
        elif c//3 == 2:
            r1 = self.board[r,c//3+4:c//3+7]
            r2 = self.board[r+1,c//3+4:c//3+7]
            r3 = self.board[r+2,c//3+4:c//3+7]
        if n not in r1 and n not in r2 and n not in r3:
            return True
        else:
            return False

    def check_rows(self,v):
        rows = 0
        cols = 0
        add = 0
        r = self.board[rows]
        # print("r", r)
        temp = []
        val = v
        for i in range(9):
            if val not in r:
                for j in range(len(r)):
                    if r[j] == 0:
                        c = self.board[:,j]
                        # print("c", c)
                        cols = j
                        if val not in c:
                            rc = i//3
                            if rc == 0:
                                rc = 0
                            elif rc == 1:
                                rc = 3
                            elif rc == 2:
                                rc = 6
                            test = self.check_square(rc,cols,val)
                            if test == True:
                                temp.append(val)
                                add = len(temp)
                            else:
                                temp.append(0)
                        else:
                            temp.append(0)
                    else:
                        temp.append(0)
                if sum(temp) == val:
                    self.board[rows,add-1] = val
                    n = self.num_count[val]
                    n += 1
                    self.num_count[val] = n
                    self.total_sum += val
                    # print(self.board)
                #ADD CASE HERE FOR IF HAVE TO GUESS
                
            temp = []
            # val += 1
            rows += 1
            if rows < 9:
                r = self.board[rows,:]
            else:
                rows = 0
                r = self.board[rows,:]
    # def check_rows(self):
    #     rows = 0
    #     cols = 0
    #     r = self.board[rows,:]
    #     temp = []
    #     val = 1
    #     for i in range(9):
    #         if val not in r:
    #             for j in range(len(r)):
    #                 if r[j] == 0:
    #                     c = self.board[:,i]
    #                     cols = i
    #                     if val not in c:
    #                         # temp.append(val)
    #                         test = self.check_square(r,cols,val)
    #                         if test == True:
    #                             temp.append(val)
    #                         else:
    #                             temp.append(0)
    #                     else:
    #                         temp.append(0)
    #                 else:
    #                     temp.append(0)
    #             if sum(temp) == 1:
    #                 self.board[rows,i] = val
    #                 n = self.num_count[val]
    #                 n += 1
    #                 self.num_count[val] = n
    #         temp = []
    #         val += 1
    #         rows += 1
    #         if rows < 9:
    #             r = self.board[rows,:]

    def check_rs(self):
        c = 1
        for i in range(9):
            self.check_rows(c)
            if c == 10 and self.total_sum != 405:
                c = 1
                i = 0
            else:
                # return self.total_sum
                c += 1

    def verify_board(self):
        final_check = 0
        for n in self.num_count:
            if self.num_count[n] == 9:
                final_check += 1
        if final_check == 9:
            print("board complete!")
        else:
            print("incomplete")

    # def solve_board(self):
    #     while 0 in self.board:
    #         self.check_rows()
    #     self.verify_board()

    def solve_board(self):
        print(self.board)
        while self.total_sum != 405:
            self.check_rs()
        print(self.board)

b = Board()
b.solve_board()    
