from math import factorial
from collections import Counter

# n Choose k
# Pascal's triangle
# C(n,k) with MOD 10^9+7
# O(n^2)

# print(combination_table(3))
# [[1, 0, 0, 0],
#  [1, 1, 0, 0],
#  [1, 2, 1, 0],
#  [1, 3, 3, 1]]


def combination_table(n):
    MOD = 10**9+7
    C = [[0]*(n+1) for _ in range(n+1)]
    C[0][0] = 1
    for i in range(1, n+1):
        C[i][0] = 1
        for j in range(1, i+1):
            C[i][j] = (C[i-1][j-1]+C[i-1][j]) % MOD
    return C

# 求第 k 小的排列方法
#
# 不盡相異物的排列數
# s = "aabbc", sz = len(s)
# 共有 sz! / (cnt["a"]! cnt["b"]! cnt["c"]!) 種

# 但如果 sz! 太大會溢位，可改從組合的角度思考
# s = "aabbc", sz = len(s)
# 從 6 格中選 2 格填 "a"
# 剩 4 格中選 2 格填 "b"
# 剩 1 格中選 1 格填 "c"

# space 代表剩餘空格，v 代表各元素的出現個數
# 排列數 = prod(comb(space, v) for v in values)
# 計算途中排列數超過目標值 LIMIT 後一律視作 LIMIT，直接退出循環


def get_ways(s):
    sz = len(s)
    cnt = Counter(s)
    ways = factorial(sz)
    for v in cnt.values():
        ways //= factorial(v)
    return ways


LIMIT = 10000


def get_comb(n, k):
    k = min(k, n-k)
    res = 1
    for i in range(1, k+1):
        res *= n-i+1  # from n to n-k+1
        res //= i  # from 1 to k
        if res >= LIMIT:  # 超過 LIMIT 無意義
            return LIMIT
    return res


def get_ways_by_comb(s):
    sz = len(s)
    cnt = Counter(s)
    space = sz
    ways = 1
    for v in cnt.values():
        ways *= get_comb(space, v)
        if ways >= LIMIT:  # 超過 LIMIT 無意義
            return LIMIT
    return ways
