class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        if not grid:
            return 0
        
        ROWS, COLS = len(grid), len(grid[0])
        visit, res = set(), 0

        def dfs(r, c, grid, visit):

            if (min(r,c) < 0 or r >= ROWS or c >= COLS or grid[r][c] == 0
            or (r,c) in visit):
                return 0
            
            visit.add((r, c))
            
            return (1 + dfs(r + 1, c, grid, visit) +
            dfs(r, c + 1, grid, visit) + 
            dfs(r - 1, c, grid, visit) +
            dfs(r, c - 1, grid, visit))

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 or (r, c) not in visit:
                    res = max(res, dfs(r, c, grid, visit))
                
        return res


            


        