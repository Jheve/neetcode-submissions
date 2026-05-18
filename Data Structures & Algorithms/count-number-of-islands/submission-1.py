class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        rows = len(grid)
        cols = len(grid[0])
        islands = 0

        def dfs(r, c):
            # base case -> check if rows or cols are within bounds
            if (r < 0 or
               c < 0 or
               r >= rows or
               c >= cols or
               grid[r][c] == '0' 
            ):
                return
            
            # mark as visited by sinking the cell
            grid[r][c] = "0"
            
            # recursively flood-fill neighbors (connected land cells)
            for dr, dc in directions:
                dfs(r + dr, c + dc)
            
        for r in range(rows):
            for c in range(cols):
                # found an unvisted land cell
                if grid[r][c] == "1":
                    # sink cell and increment island count
                    dfs(r, c)
                    islands += 1
        
        return islands