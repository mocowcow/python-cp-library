from collections import defaultdict
from heapq import heappop, heappush
from math import inf


# bruteforce dijkstra
# O(V^2)
# better performance for dense graph
def dijkstra_bruteforce(g, n, src):
    vis = [False]*n
    dis = [inf]*n
    dis[src] = 0
    while True:  # at most loop for n times
        i = -1
        for j in range(n):  # find shortest unvisited node i
            if not vis[j] and (i < 0 or dis[j] < dis[i]):
                i = j
        if i < 0 or dis[i] == inf:  # no more path
            break
        vis[i] = True
        for j, c in g[i]:  # update adjacent nodes
            new_cost = cost+c
            if new_cost < dis[j]:
                dis[j] = new_cost
    return dis


# heap optimized dijkstra
# O(V + E log E)
def dijkstra(g, n, src):
    dis = [inf]*(n)
    dis[src] = 0
    heap = [(0, src)]
    while heap:
        cost, curr = heappop(heap)
        if cost > dis[curr]:
            continue
        dis[curr] = cost
        for adj, c in g[curr]:
            new_cost = cost+c
            if new_cost < dis[adj]:
                dis[adj] = new_cost  # important pruning
                heappush(heap, (new_cost, adj))
    return dis


# 6 nodes directed graph
edges = [[0, 2, 2], [0, 5, 6], [1, 0, 3], [1, 4, 5],
         [2, 1, 1], [2, 3, 3], [2, 3, 4], [3, 4, 2]]
n = 6

# build graph
graph = defaultdict(list)
for a, b, cost in edges:
    graph[a].append((b, cost))

# min distance from src=0 to all nodes
src = 0
t = dijkstra(graph, n, src)
print(t)
