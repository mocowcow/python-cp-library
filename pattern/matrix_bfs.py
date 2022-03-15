
matrix = [
    [1, 2, 3],
    [4, 5, 6]
]


def matrix_bfs(matrix):

    M, N = len(matrix), len(matrix[0])
    dist = 0
    visited = set()
    q = []  # 固定起點

    # 依條件加入起點
    for i in range(M):
        for j in range(N):
            if matrix[i][j] == 1:
                q.append((i+1, j))
                q.append((i-1, j))
                q.append((i, j+1))
                q.append((i, j-1))

    # BFS
    while q:
        t = []
        for r, c in q:
            if not (0 <= r < N and 0 <= c < N) or matrix[r][c] != 0 or (r, c) in visited:  # 終止條件
                continue
            visited.add((r, c))
            # 中間處理
            t.append((r+1, c))
            t.append((r-1, c))
            t.append((r, c+1))
            t.append((r, c-1))

        dist += 1
        q = t

    return dist
