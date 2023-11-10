import sys
"""
[1, 3, 0, 2]
. Q . .                    
. . . Q
Q . . .
. . Q .
"""
class Solution():
   # posDiag: r+c
   # negDiag: r-c
    
    def SolveNQueens(self, n):
        col = set()
        posDiag = set() # r+c
        negDiag = set() # r-c
        
        res = []
        board = [["."]*n for i in range(n)]
        
        def backtrack(r):
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            
            for c in range(n):
                if c in col or (r + c) in posDiag or (r - c) in negDiag:
                    continue
                
                col.add(c) 
                posDiag.add(r + c)   
                negDiag.add(r - c)
                board[r][c] = "Q"
                
                backtrack(r+1)
                
                col.remove(c) 
                posDiag.remove(r + c)   
                negDiag.remove(r - c)
                board[r][c] = "."
          
            
opt = 0 
n = 0  
queens = Solution() 
while True:
    print("\n Choose: \n")
    print("1. N Queen problem\n")
    print("2. Exit program\n")
    opt = input("Option: ")
    
    if opt == '1':
        n = int(input("\nChoose the number of queens(the number must be 1 or >=4): "))
        
        solutions = queens.SolveNQueens(n)
        for solution in solutions:
            for row in solution:
                print(row) 
            print()   
            
    elif opt == '2':
        sys.exit()
        
    else:
        print("\nINVALID OPTION\n")
        print("\nXXXXXXXXXXXXXXXXXX\n")