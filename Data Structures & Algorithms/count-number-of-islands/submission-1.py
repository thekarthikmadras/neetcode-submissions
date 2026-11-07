class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        islands = 0

        def bfs(r, c):
            q = deque()
            q.append((r, c))
            grid[r][c] == "0"

            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    r, c = dr + row, dc + col 
                    if (r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] == "0"):
                        continue
                    q.append((r, c))
                    grid[r][c] = "0"

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    bfs(r, c)
                    islands += 1
        return islands