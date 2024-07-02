
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
