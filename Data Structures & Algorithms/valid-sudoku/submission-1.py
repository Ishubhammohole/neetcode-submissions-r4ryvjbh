class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = {}
        
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                box_key = (r // 3, c // 3)
                if box_key not in boxes:
                    boxes[box_key] = set()
                if board[r][c] in rows[r]:
                    return False
                if board[r][c] in cols[c]:
                    return False
                
                if board[r][c] in boxes[box_key]:
                    return False
                
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                boxes[box_key].add(board[r][c])
        return True


        