class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]  # [set(1,2,3,...), set(),.....]
        cols = [set() for _ in range(9)]  # [set(1,4,5,7,.), set(2,9,.),]
        grids = defaultdict(set) # [set(1,2,4,9,8), set(),.....]        

        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue
                if board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in grids[(r//3, c//3)]:
                    return False

                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                grids[(r//3, c//3)].add(board[r][c])
                
        return True

