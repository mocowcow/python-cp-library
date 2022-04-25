class PrefixSum2D:

    def __init__(self, matrix):
        M, N = len(matrix), len(matrix[0])
        self.psum = [[0]*(N+1) for _ in range(M+1)]
        for r in range(M):
            for c in range(N):
                self.psum[r+1][c+1] = self.psum[r][c+1] + \
                    self.psum[r+1][c]-self.psum[r][c]+matrix[r][c]

    def rangeSum(self, r1, c1, r2, c2):
        return self.psum[r2+1][c2+1]-self.psum[r2+1][c1]-self.psum[r1][c2+1]+self.psum[r1][c1]


mat = [[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]]

ps2d = PrefixSum2D(mat)
assert ps2d.rangeSum(0, 0, 2, 2) == 45
assert ps2d.rangeSum(0, 0, 1, 2) == 21
assert ps2d.rangeSum(0, 1, 2, 2) == 33
assert ps2d.rangeSum(2, 1, 2, 2) == 17
assert ps2d.rangeSum(1, 1, 1, 2) == 11
assert ps2d.rangeSum(2, 2, 2, 2) == 9
