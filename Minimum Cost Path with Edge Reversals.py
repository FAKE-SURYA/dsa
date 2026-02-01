import heapq
from math import inf
from typing import List

class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        # 1. Build graph with both original and reversed edges
        graph = [[] for _ in range(n)]
        for u, v, w in edges:
            # original edge u -> v with cost w
            graph[u].append((v, w))
            # reversed edge v -> u with cost 2*w
            graph[v].append((u, 2 * w))

        # 2. Dijkstra from node 0
        dist = [inf] * n
        dist[0] = 0
        pq = [(0, 0)]  # (cost, node)

        while pq:
            curr_cost, u = heapq.heappop(pq)

            if curr_cost > dist[u]:
                continue

            for v, w in graph[u]:
                new_cost = curr_cost + w
                if new_cost < dist[v]:
                    dist[v] = new_cost
                    heapq.heappush(pq, (new_cost, v))

        return -1 if dist[n - 1] == inf else dist[n - 1]
