"""
[1, 3, 0, 2]
. Q . .                    
. . . Q
Q . . .
. . Q .
"""
class Solution():
   
    #SOLVE
    def SolveNQueens(self, n):
        solutions = []
        state = []
        self.search(state, solutions, n)
        return solutions
    
    #IS VALID STATE
    def is_valid_state(self, state, n):
        return len(state) == n
    
    #GET CANDIDATES
    def get_candidates(self, state, n):
        pass 
    
    #SEARCH
    def search(self, state, solutions, n):
        pass
    
    