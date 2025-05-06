# pylint: disable=pointless-string-statement

"""
倍增算法 (binary lifting 或 binary jumping)

核心思想：
知道每個點跳 1 次的位置，就可以遞推出跳 2 次的位置。
知道每個點跳 2 次的位置，就可以遞推出跳 4 次的位置。
知道每個點跳 4 次的位置，就可以遞推出跳 8 次的位置。以此類推。


定義 f[i][jump]：從 i 跳 2^jump 次的位置。
N 個點，最大跳躍次數 K。
每個點須預處理跳 2^jump 次的結果。約有 MX = O(log K) 跳法。
複雜度 O(N log K)。  

---

求 x 跳 k 次的結果：

任何整數都可由若干個 2 的冪次數 (即 2^jump) 組成。
若 k 的二進制表示中第 jump 個設置位為 1，代表需跳 2^jump 次。  
複雜度 O(log k)。

例如：
> k = 11
> k 的二進制 = 1011
> 可開分成跳 1 + 2 + 8 次


---


求 x 跳到 y 的最少次數：

限制：x 跳 k 次需抵達 (或超過) y。

- 基礎做法：
基於上述跳 k 次的方法，搭配二分搜，找 "第一個滿足限制" 的 k。
若跳 k 次可抵達 y，則 k+1 肯定也可以；若 k 次無法，則 k-1 肯定也無法。

二分區間 [0, K]，需判斷 O(log K) 次。
每次判斷需跳躍成本 O(log K)。
複雜度 O(log K * log K)。


- 優化做法：
基礎做法的難點在於：若 x 跳 k 步合法，則 k+1 步也合法。很難找最小值。

改變二分的目標，改成找 "最後一個不滿足限制" 的 k。即最大的 k 使得 x' < y。
根據定義，從 x' 再多跳 1 次正好抵達 y。
共 k+1 次跳躍。

從大到小枚舉 jump。
若當前 f[x][jump] < y，不滿足限制，從 x 跳到 f[x][jump]，得到規模更小的子問題。
最後再次跳 1 次，檢查是否滿足 x >= y。
複雜度 O(log K)。

"""


# LC 1483 (跳 k 次) https://leetcode.com/problems/kth-ancestor-of-a-tree-node/
# LC 2836 (跳 k 次) https://leetcode.com/problems/maximize-value-of-function-in-a-ball-passing-game/
# LC 3534 (最少跳幾次) https://leetcode.com/problems/path-existence-queries-in-a-graph-ii/


def binary_lifting():
    # 輸入
    positions = []
    parent = []

    N = len(positions)  # 有多少點
    MX = N.bit_length()  # 最大跳躍次數取 log

    # f[i][jump]: 從 i 跳 2^jump 次的位置
    # -1 代表沒有下一個點
    f = [[-1]*MX for _ in range(N)]

    # 初始化每個位置跳一次
    # 實作細節自行修改
    for i in range(N):
        f[i][0] = parent[i]

    # 倍增遞推
    for jump in range(1, MX):
        for i in range(N):
            temp = f[i][jump-1]
            if temp != -1:  # 必須存在中繼點
                f[i][jump] = f[temp][jump-1]

    # 從 x 跳 k 次
    # -1 表示不合法
    def k_jump(x, k):
        for jump in range(MX):
            if k & (1 << jump):
                x = f[x][jump]
                if x == -1:  # 不能跳
                    return -1
        return x

    # x >= y 最少要跳幾次
    # -1 表示跳不到
    def min_jump(x, y):
        if x == y:
            return 0

        if x > y:
            x, y = y, x

        # 最多先跳到 y-1
        step = 0
        for jump in reversed(range(MX)):
            temp = f[x][jump]
            if temp < y:
                x = temp
                step += 1 << jump

        # 再跳一次
        step += 1
        x = f[x][0]

        if x >= y:
            return step
        return -1


"""
樹上倍增求 LCA

先將 x, y 兩點調整到相同的深度。
然後往上找 "深度最低的非 LCA"，再跳 1 次就會抵達 LCA。
複雜度 O(log K)。

"""

# LC 2846 (前綴和) https://leetcode.com/problems/minimum-edge-weight-equilibrium-queries-in-a-tree/


def tree_LCA():
    # 輸入
    positions = []
    parent = []
    depth = []

    N = len(positions)  # 有多少點
    MX = N.bit_length()  # 最大跳躍次數取 log

    # f[i][jump]: 從 i 跳 2^jump 次的位置
    # -1 代表沒有下一個點
    f = [[-1]*MX for _ in range(N)]

    # 初始化每個位置跳一次
    # 實作細節自行修改
    for i in range(N):
        f[i][0] = parent[i]

    # 倍增遞推
    for jump in range(1, MX):
        for i in range(N):
            temp = f[i][jump-1]
            f[i][jump] = f[temp][jump-1]

    def get_LCA(x, y):
        if depth[x] > depth[y]:
            x, y = y, x

        # 把 y 調整到和 x 相同深度
        diff = depth[y]-depth[x]
        for jump in range(MX):
            if diff & (1 << jump):
                y = f[y][jump]

        # 已經相同
        if x == y:
            return x

        # 否則找最低的非 LCA
        for jump in reversed(range(MX)):
            if f[x][jump] != f[y][jump]:
                x = f[x][jump]
                y = f[y][jump]

        # 再跳一次到 LCA
        return f[x][0]
