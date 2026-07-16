class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_set = defaultdict(set)
        col_set = defaultdict(set)
        box_set = defaultdict(set)
        
        for r, row in enumerate(board):
            for c, cell in enumerate(row):
                if cell != ".":
                    b = (r // 3) * 3 + (c // 3)
                    if cell in row_set[r] or cell in col_set[c] or cell in box_set[b]:
                        return False
                    row_set[r].add(cell)
                    col_set[c].add(cell)
                    box_set[b].add(cell)
        
        return True
                    

                    
