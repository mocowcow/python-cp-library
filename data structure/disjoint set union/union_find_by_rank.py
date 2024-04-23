
class UnionFind:
    def __init__(self, n):
        self.parent = [0] * n
        self.rank = [0] * n  # 可以是節點數或高度，此為高度
        for i in range(n):
            self.parent[i] = i

    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)
        if px == py:
            return

        if self.rank[px] > self.rank[py]:  # 限制 px <= py
            px, py = py, px

        self.parent[px] = py  # 將小的合併到大的
        if self.rank[px] == self.rank[py]:
            self.rank[py] += 1

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
