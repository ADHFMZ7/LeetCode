class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        if not grid:
            return 0
        marked = [[0 for i in range(COLS)] for j in range(ROWS)]

        def dfs(x, y):
            if x < 0 or x >= ROWS or y < 0 or y >= COLS or marked[x][y] or grid[x][y] == "0":
                return 0

            marked[x][y] = 1
            offsets = [(0, 1), (0, -1), (-1, 0), (1, 0)]
            for dx, dy in offsets:
                dfs(x + dx, y + dy)
            return 1

        islands = 0
        for xx in range(ROWS):
            for yy in range(COLS):
                islands += dfs(xx, yy)
        return islands
