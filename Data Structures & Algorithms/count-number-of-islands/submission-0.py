class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
    
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()

        def dfs(grid, r, c, visit):
            if (min(r, c) < 0 or r >= ROWS or c >= COLS or (r, c) in visit
            or grid[r][c] == "0"):
                return
            
            visit.add((r, c))
            dfs(grid, r + 1, c, visit)
            dfs(grid, r, c + 1, visit)
            dfs(grid, r - 1, c, visit)
            dfs(grid, r, c - 1, visit)

        
        count = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r, c) not in visit:
                    count += 1
                    dfs(grid, r, c, visit)
        return count

                



        

        