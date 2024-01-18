MOD = 10**9+7


def mat_pow(base, p):
    res = [[1, 0], [0, 1]]  # identity matrix
    while p > 0:
        if p & 1:
            res = mat_mul(res, base)
        p >>= 1
        base = mat_mul(base, base)
    return res


def mat_mul(a, b):
    c = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                c[i][j] += a[i][k]*b[k][j]
            c[i][j] %= MOD
    return c


# 轉移矩陣trans
# trans^k * f(0) = f(0+k)

# f(i)  = [ arg1, _ ]
#         [ arg2, _ ]

# trans = [ A, B ]
#         [ C, D ]

# f(i+1)  = [ arg1*A + arg2*B, _ ]
#           [ arg1*C + arg2*D, _ ]

# A = f(i).arg1 對 f(i+1).arg1 的貢獻
# B = f(i).arg2 對 f(i+1).arg1 的貢獻
# C = f(i).arg1 對 f(i+1).arg2 的貢獻
# D = f(i).arg2 對 f(i+1).arg2 的貢獻

# 練習題：矩陣快速冪優化DP
# - [70. Climbing Stairs](https://leetcode.com/problems/climbing-stairs/)
# - [1220. Count Vowels Permutation](https://leetcode.com/problems/count-vowels-permutation/)
# - [2851. String Transformation](https://leetcode.com/problems/string-transformation/)
