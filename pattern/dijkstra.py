from collections import defaultdict
from heapq import heappop, heappush
import math


def dijkstra(g, n, src):  # graph with n nodes start from src
    table = [math.inf]*(n)
    heap = [(0, src)]
    while heap:
        time, curr = heappop(heap)
        if time < table[curr]:
            table[curr] = time
            for adj, cost in g[curr]:
                heappush(heap, (time+cost, adj))

    return table


# 6 nodes directed graph
edges = [[0, 2, 2], [0, 5, 6], [1, 0, 3], [1, 4, 5], [2, 1, 1], [2, 3, 3], [2, 3, 4], [3, 4, 2]]
n = 6
# build graph
graph = defaultdict(list)
for a, b, cost in edges:
    graph[a].append((b, cost))
# min distance from src=0 to all nodes
src = 0
t = dijkstra(graph, n, src)
print(t)
