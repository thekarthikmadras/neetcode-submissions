from typing import List

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # Build adjacency list
        graph = {i: [] for i in range(n)}
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        # Visited set to track visited nodes
        visited = set()
        components = 0

        # DFS function to explore a component
        def dfs(node):
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    dfs(neighbor)

        # Explore all nodes
        for i in range(n):
            if i not in visited:  # Start a new DFS if node is unvisited
                components += 1
                dfs(i)

        return components
