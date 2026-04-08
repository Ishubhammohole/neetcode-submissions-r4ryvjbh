class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        time, fresh = 0, 0
        q = deque()
        ROWS, COLS = len(grid), len(grid[0])

        def makeRotten(a : int, b : int) -> None:
            nonlocal fresh
            if (min(a, b) < 0 or a >= ROWS or b >= COLS):
                return
            if grid[a][b] != 1:
                return       
            grid[a][b] = 2
            fresh -= 1
            q.append((a, b))


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r, c))
        
        while q and fresh > 0:
            length = len(q)
            for _ in range(length):
                r, c = q.popleft()
                makeRotten(r + 1, c)
                makeRotten(r, c + 1)
                makeRotten(r, c - 1)
                makeRotten(r - 1, c)
                
            time += 1
        return -1 if fresh > 0 else time
            


        

        