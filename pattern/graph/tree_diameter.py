
def diameter_dfs(edges):
    N = len(edges) + 1
    g = [[] for _ in range(N)]
    for a, b in edges:
        g[a].append(b)
        g[b].append(a)

    farthest = None
    mx_dist = -1

    def dfs(i, fa, dist):
        nonlocal farthest, mx_dist
        if dist > mx_dist:
            mx_dist = dist
            farthest = i
        for j in g[i]:
            if j == fa:
                continue
            dfs(j, i, dist + 1)

    dfs(0, -1, 0)

    mx_dist = -1
    dfs(farthest, -1, 0)
    return mx_dist


def diameter_bfs(edges):
    N = len(edges) + 1
    g = [[] for _ in range(N)]
    for a, b in edges:
        g[a].append(b)
        g[b].append(a)

    def bfs(start):
        dist = [-1] * N
        dist[start] = 0
        q = [start]
        while q:
            q2 = []
            for i in q:
                for j in g[i]:
                    if dist[j] == -1:
                        dist[j] = dist[i] + 1
                        q2.append(j)
            q = q2

        farthest = None
        mx_dist = -1
        for i, d in enumerate(dist):
            if d > mx_dist:
                mx_dist = d
                farthest = i
        return farthest, mx_dist

    u, dist = bfs(0)
    v, dist = bfs(u)
    return dist
