

"""
置換環
一個陣列 a 按照某種規則排序後的結果為 b。
求選擇任意 a[i], a[j] 進行交換，使得 a 等於 b 的最小次數。

將 a 中每個元素 x 指向其排序後的正確位置 (x 在 b 中位置)，會形成若干個環。
若元素已在正確位置，則自成一環。

交換只會發生在環內。
每次交換，將元素放到正確位置後，環的大小會減 1。

對於大小為 sz 的環，交換 sz - 1 次後會把最後一個元素也移到正確位置上。
若陣列中存在 cnt 個環，則需交換 N - cnt 次。

"""

# https://www.geeksforgeeks.org/minimum-number-swaps-required-sort-array/
# LC 2471 https://leetcode.com/problems/minimum-number-of-operations-to-sort-a-binary-tree-by-level/
# LC 3551 https://leetcode.com/problems/minimum-swaps-to-sort-by-digit-sum/


# 做法一
# 模擬換位：以位置 i 為主，把錯誤的元素換到正確位置 j
# 枚舉 a 中的位置 i，若 a[i] 當前元素不正確，則不斷把 a[i] 放到正確位置上
def swap_to_correct_pos(a):
    N = len(a)
    b = sorted(a)
    mp_b = {x: i for i, x in enumerate(b)}  # 元素 x 排序後位於 b 的位置

    cnt = 0
    for i in range(N):
        while a[i] != b[i]:
            j = mp_b[a[i]]  # 當前元素 a[i] 的正確位置
            a[i], a[j] = a[j], a[i]
            cnt += 1
    return cnt


# 做法二
# 模擬換位：以元素 x 為主，直接把 x 放到正確位置
# 枚舉所有元素 x，按照 x 排序後的位置調整原陣列
def swap_from_correct_pos(a):
    b = sorted(a)
    mp_a = {x: i for i, x in enumerate(a)}  # 元素 x 當前位於 a 的位置

    cnt = 0
    for i, x in enumerate(b):
        if a[i] != x:
            j = mp_a[x]  # x 當前位於 a[i] 的位置
            a[i], a[j] = a[j], a[i]
            mp_a[a[j]] = j  # a[j] 的元素換位過，記得更新
            cnt += 1
    return cnt


# 做法三
# dfs 找環 (可改成迭代)
def dfs_component(a):
    N = len(a)
    b = sorted(a)
    mp_b = {x: i for i, x in enumerate(b)}  # 元素 x 排序後位於 b 的位置

    def dfs(i):
        if vis[i]:
            return
        vis[i] = True
        dfs(mp_b[a[i]])

    vis = [False] * N
    cnt = 0
    for i in range(N):
        if not vis[i]:
            cnt += 1
            dfs(i)
    return N - cnt


# 做法四
# 併查集找連通塊
def union_find_component(a):
    class UnionFind:
        def __init__(self, n):
            self.parent = list(range(n))
            self.component_cnt = n  # 連通塊數量

        def union(self, x, y):
            px = self.find(x)
            py = self.find(y)
            if px != py:
                self.component_cnt -= 1  # 連通塊減少 1
                self.parent[px] = py

        def find(self, x):
            if x != self.parent[x]:
                self.parent[x] = self.find(self.parent[x])
            return self.parent[x]

    N = len(a)
    b = sorted(a)
    mp_b = {x: i for i, x in enumerate(b)}  # 元素 x 排序後位於 b 的位置

    uf = UnionFind(N)
    for i, x in enumerate(a):
        uf.union(i, mp_b[x])
    return N - uf.component_cnt
