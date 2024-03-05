
class PrefixSum2D:

    def __init__(self, matrix):
        M, N = len(matrix), len(matrix[0])
        ps = self.ps = [[0]*(N+1) for _ in range(M+1)]
        for r in range(M):
            for c in range(N):
                ps[r+1][c+1] = \
                    ps[r][c+1] + ps[r+1][c] - \
                    ps[r][c] + matrix[r][c]

    def range_sum(self, r1, c1, r2, c2):
        ps = self.ps
        return ps[r2+1][c2+1] - ps[r2+1][c1] - ps[r1][c2+1] + ps[r1][c1]
