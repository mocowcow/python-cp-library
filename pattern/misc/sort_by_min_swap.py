

"""
置換環
將 a 中每個元素 x 指向其排序後的正確位置 (x 在 b 中位置)，會形成若干個環。
若元素已在正確位置，則自成一環。

---

一個陣列 a 按照某種規則排序後的結果為 b。
求選擇任意 a[i], a[j] 進行交換，使得 a 等於 b 的最小次數。

交換只會發生在環內。
每次交換，將元素放到正確位置後，環的大小會減 1。

對於大小為 sz 的環，交換 sz - 1 次後會把最後一個元素也移到正確位置上。
若陣列中存在 cnt 個環，則需交換 N - cnt 次。
可用模擬、dfs、併查集找環。

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


"""
逆序對 (Inversion)
若陣列 a 存在正整數 i, j 滿足 i < j 且 a[i] > a[j]，則稱 (i, j) 為逆序對。

---

一個陣列 a 按照某種規則排序後的結果為 b。
求選擇相鄰的兩個元素 a[i], a[i+1] 交換，使得 a 等於 b 的最小次數。

交換相鄰元素排序，實際上就是泡沫排序 (bubble sort)。
泡沫排序每次比較相鄰的數對 a[i], a[i+1]，只要逆序就交換，每次交換逆序對數減 1。

所需交換次數即為逆序對總數。
可用離散化 + BIT 、線段樹或 merge sort 求逆序對。

"""


# UVa 10810 https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=1751


# 做法一
# 從左到右遍歷 a 的每個元素 x
# 用 BIT 維護各元素頻率，區間查詢左方大於 x 的元素個數
def BIT_inversion(a):
    class BIT:
        """
        tree[0]代表空區間，不可存值，基本情況下只有[1, n-1]可以存值。
        offset為索引偏移量，若設置為1時正好可以對應普通陣列的索引操作。
        """

        def __init__(self, n, offset=1):
            self.offset = offset
            self.tree = [0]*(n+offset)

        def update(self, pos, val):
            """
            將tree[pos]增加val
            """
            i = pos+self.offset
            while i < len(self.tree):
                self.tree[i] += val
                i += i & (-i)

        def query(self, pos):
            """
            查詢[1, pos]的前綴和
            """
            i = pos+self.offset
            res = 0
            while i > 0:
                res += self.tree[i]
                i -= i & (-i)
            return res

        def query_range(self, i, j):
            """
            查詢[i, j]的前綴和
            """
            return self.query(j)-self.query(i-1)

    N = len(a)
    # 離散化
    b = sorted(a)
    mp = {x: i for i, x in enumerate(b)}
    for i in range(N):
        a[i] = mp[a[i]]

    bit = BIT(N)
    cnt = 0
    for i, x in enumerate(a):
        cnt += bit.query_range(x+1, N-1)  # 左方比 x 大的元素個數
        bit.update(x, 1)
    return cnt


# 做法二
# 合併排序
# 當兩個有序陣列 L, R 合併
# L 剩餘最小元素為 min(L)，R 剩餘最小元素為 min(R)
# 若 min(L) > min(R) 則代表 L 剩餘所有的元素都大於 min(R)，每個都可以和 min(R) 構成逆序對
def merge_sort_inversion(src):

    def f(a):
        nonlocal cnt
        N = len(a)
        if N == 1:
            return a
        M = N // 2
        L, R = f(a[:M]), f(a[M:])
        res = []
        i = j = 0
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                res.append(L[i])
                i += 1
            else:
                res.append(R[j])
                cnt += len(L) - i  # 左方 L 比有幾個數比 R[j] 大
                j += 1
        res.extend(L[i:])
        res.extend(R[j:])
        return res

    cnt = 0
    f(src)
    return cnt


# 測試泡沫排序的交換次數與以上方法統計逆序對相同
def bubble(a):
    N = len(a)
    cnt = 0
    for _ in range(N):
        for i in range(1, N):
            if a[i-1] > a[i]:
                a[i-1], a[i] = a[i], a[i-1]
                cnt += 1
    return cnt


a = list(range(100))
for _ in range(1000):
    import random
    random.shuffle(a)
    bubble_swap = bubble(a.copy())
    assert bubble_swap == BIT_inversion(a.copy())
    assert bubble_swap == merge_sort_inversion(a.copy())
