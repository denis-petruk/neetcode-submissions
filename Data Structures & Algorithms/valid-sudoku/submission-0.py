class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Automatically initializes missing keys with an empty set
        checker = {
            "rows": defaultdict(set), 
            "cols": defaultdict(set), 
            "squares": defaultdict(set)
        }
        
        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val == ".":
                    continue
                
                square_idx = (i // 3) * 3 + (j // 3)
                
                if val in checker["rows"][i] or val in checker["cols"][j] or val in checker["squares"][square_idx]:
                    return False
                
                checker["rows"][i].add(val)
                checker["cols"][j].add(val)
                checker["squares"][square_idx].add(val)
                
        return True