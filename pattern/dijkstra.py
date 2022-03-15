from collections import defaultdict
from heapq import heappop, heappush
import math


def dijkstra(graph, N, src): #graph with N nodes
    g = defaultdict(dict)
    for a, b, time in graph:
        g[a][b] = time

    visited = set()
    table = [math.inf]*(N+1)
    heap = [(0, src)]
    while heap:
        time, curr = heappop(heap)
        if curr in visited:
            continue
        visited.add(curr)
        table[curr] = time
        for adj in g[curr].keys():
            newTime = time+g[curr][adj]
            heappush(heap, (newTime, adj))

    return table


t = dijkstra([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2)
print(t)
