
matrix = [
    [1, 2, 3],
    [4, 5, 6]
]


def matrix_dfs():
    M, N = len(matrix), len(matrix[0])
    visited = set()

    def dfs(r, c):
        if not (0 <= r < M and 0 <= c < N) or matrix[r][c] != 1 or (r, c) in visited:  # 終止條件
            return
        # 中間處理
        visited.add((r, c))
        matrix[r][c] = 0

        for nr, nc in ((r+1, c), (r-1, c), (r, c+1), (r, c-1)):
            dfs(nr, nc)

    # 依條件開始dfs
    for i in range(M):
        for j in range(N):
            if i == 0 or j == 0 or i == M-1 or j == N-1:  # 開始條件
                dfs(i, j)


def matrix_dfs_stack():
    M, N = len(matrix), len(matrix[0])
    visited = set()

    def dfs(r, c):
        st = [(r, c)]
        while st:
            r, c = st.pop()
            if not (0 <= r < M and 0 <= c < N) or matrix[r][c] != 1 or (r, c) in visited:  # 終止條件
                continue
            # 中間處理
            visited.add((r, c))
            matrix[r][c] = 0
            for nr, nc in ((r+1, c), (r-1, c), (r, c+1), (r, c-1)):
                st.append(nr, nc)

    # 依條件開始dfs
    for i in range(M):
        for j in range(N):
            if i == 0 or j == 0 or i == M-1 or j == N-1:  # 開始條件
                dfs(i, j)
