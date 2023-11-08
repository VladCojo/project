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
        solutions = []
        state = []
        self.search(state, solutions, n)
        return solutions
    
    
    def is_valid_state(self, state, n):
        # check if it is a valid solution
        return len(state) == n
    
    
    def get_candidates(self, state, n):
        if not state:
            return list(range(n)) 
        
        # find the next position in state to populate
        position = len(state)
        candidates = set(range(n))
        
        # prune downd candidates that place the queen into attacks
        for row, col in enumerate(state):
            # discard the column index if it's occupied by a queen
            candidates.discard(col)
            dist = position - row
            # discard diagonals
            candidates.discard(col + dist)  
            candidates.discard(col - dist)
            
        return list(candidates)
    
    
    def search(self, state, solutions, n):
        if self.is_valid_state(state, n):
            state_string = self.state_to_string(state, n)
            solutions.append(state_string)
            return
        
        for candidate in self.get_candidates(state, n):
            # recurse
            state.append(candidate)
            self.search(state,solutions,n)
            state.pop()
            
            
    def state_to_string(self, state, n):
        # ex: [1, 3, 0, 1]
        # output: [".Q..","...Q","Q...","..Q."]

        ret = []
        for i in state:
            string = '. ' * i + 'Q' + ' .' * (n - i - 1)
            ret.append(string)
        return ret
            
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
        