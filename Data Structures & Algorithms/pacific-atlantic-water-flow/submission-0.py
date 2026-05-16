class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # keep track of both atlantic and pacific cells
        rows, cols = len(heights), len(heights[0])
        pacific, atlantic = set(), set()

        # work reverse -> start from ocean edges and backtrack through equal or higher edges
        def dfs(r, c, visited, previous_height):
            # reversed -> going uphill
            if (((r, c)) in visited or 
                r < 0 or 
                c < 0 or 
                r == rows or 
                c == cols or
                heights[r][c] < previous_height
            ):
                return 
            
            visited.add((r, c))

            # check neighbors
            dfs(r + 1, c, visited, heights[r][c])
            dfs(r - 1, c, visited, heights[r][c])
            dfs(r, c + 1, visited, heights[r][c])
            dfs(r, c - 1, visited, heights[r][c])

        for c in range(cols):
            dfs(0, c, pacific, heights[0][c])                   # top row Pacific
            dfs(rows - 1, c, atlantic, heights[rows - 1][c])    # bottom row Atlantic

        for r in range(rows):   
            dfs(r, 0, pacific, heights[r][0])                   # left col Pacific
            dfs(r, cols - 1, atlantic, heights[r][cols - 1])    # right col Atlantic

        result = []

        for r in range(rows):
            for c in range(cols):
                if (r, c) in pacific and (r, c) in atlantic:
                    result.append([r, c])

        return result        