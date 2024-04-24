import random

# 求兩點之間最大曼哈頓距離
# max( |x1 - x2| + |y2 - y2| )

# 消除絕對值得到：
# (x1 - x2) + (y1 - y2)
# (x2 - x1) + (y1 - y2)
# (x1 - x2) + (y2 - y1)
# (x2 - x1) + (y2 - y1)

# 整理後：
# x1 + y1 - x2 - y2
# -x1 + y1 + x2 - y2
# x1 - y1 - x2 + y2
# -x1 - y1 + x2 + y2

# 根據對稱性，一和四式等價、二和三式等價。
# 去重後：
# (x1 + y1) - (x2 + y2)
# -(x1 - y1) + (x2 - y2)

# 分別代入 (x + y) 和 (x - y) 極值即可。


def max_manhattan(points):
    A = sorted([x + y, i] for i, (x, y) in enumerate(points))
    B = sorted([x - y, i] for i, (x, y) in enumerate(points))

    minA, maxA = A[0][0], A[-1][0]
    minB, maxB = B[0][0], B[-1][0]

    res = max(
        maxA - minA,  # max(x1 + y1) - min(x2 + y2)
        -minB + maxB  # -min(x1 - y1) + max(x2 - y2)
    )
    return res


def brute_force(points):
    N = len(points)
    res = 0
    for i in range(N):
        for j in range(i):
            dist = abs(points[i][0] - points[j][0]) + \
                abs(points[i][1] - points[j][1])
            res = max(res, dist)
    return res


def test_same():
    for _ in range(100):
        P = [[random.randint(-1e9, 1e9) for _ in range(2)] for _ in range(100)]
        assert max_manhattan(P) == brute_force(P)
    print('passed')


test_same()
