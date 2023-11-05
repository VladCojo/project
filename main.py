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
        pass
    
    