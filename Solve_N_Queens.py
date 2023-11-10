import sys
"""
[1, 3, 0, 2]
. Q . .                    
. . . Q
Q . . .
. . Q .
"""
class Solution():
   
    
    def SolveNQueens(self, n):
        
        pass
            
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