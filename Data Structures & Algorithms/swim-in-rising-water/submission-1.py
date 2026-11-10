class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N = len(grid)
        minHeap = [[grid[0][0], 0, 0]]
        visit = set()
        visit.add((0, 0))
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        while minHeap:
            t, r, c = heapq.heappop(minHeap)
            if r == N - 1 and c == N - 1:
                return t
            visit.add((r, c))
            for dr, dc in directions:
                neiR, neiC = r + dr, c + dc
                if (neiR < 0 or neiC < 0 or neiR >= N or neiC >= N or (neiR, neiC) in visit):
                    continue
                visit.add((neiR, neiC))
                heapq.heappush(minHeap, [max(t, grid[neiR][neiC]), neiR, neiC])