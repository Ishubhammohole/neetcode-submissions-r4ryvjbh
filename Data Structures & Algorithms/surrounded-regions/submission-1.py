class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        visit = set()

        #1. turn the Os (that are at the border) in Ts(dfs)
        def dfs(r, c, visit, board):
            if(min(r, c) < 0 or r >= ROWS or c >= COLS or (r, c) in visit
            or board[r][c] != "O"):
                return
            visit.add((r, c))
            board[r][c] = "T"
            dfs(r + 1, c, visit, board)
            dfs(r - 1, c, visit, board)
            dfs(r, c + 1, visit, board)
            dfs(r, c - 1, visit, board)

        for r in range(ROWS):
            if board[r][0]:
                dfs(r, 0, visit, board)
            if board[r][COLS - 1] == "O":
                dfs(r, COLS - 1, visit, board)
            
        for c in range(COLS):
            if board[0][c] == "O":
                dfs(0, c, visit, board)
            if board[ROWS - 1][c] == "O":
                dfs(ROWS - 1, c, visit, board)

        #2. Capture all the Os

        #3. Turn all the Ts in Os
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "T":
                    board[r][c] = "O"