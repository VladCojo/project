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
            return range(n) 
        
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
            
        return candidates
    
    
    def search(self, state, solutions, n):
        if self.is_valid_state(state, n):
            state_string = self.state_to_string(state)
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
            
opt = 0 
     
while True:
    print("\n Choose: \n")
    print("1. N Queen problem\n")
    print("2. Exit program\n")
    opt = input("Option: ")
    
    if opt == 1:
        pass
    elif opt == 2:
        break;
    else:
        print("\nINVALID OPTION\n")