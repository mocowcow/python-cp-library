
# n Choose k
# Pascal's triangle
# C(n,k) with MOD 10^9+7
# O(n^2)
def conbination_table(n):
    MOD = 10**9+7
    C = [[0]*(n+1) for _ in range(n+1)]
    C[0][0] = 1
    for i in range(1, n+1):
        C[i][0] = 1
        for j in range(1, i+1):
            C[i][j] = (C[i-1][j-1]+C[i-1][j]) % MOD
    return C


print(conbination_table(3))
# [[1, 0, 0, 0],
#  [1, 1, 0, 0],
#  [1, 2, 1, 0],
#  [1, 3, 3, 1]]
