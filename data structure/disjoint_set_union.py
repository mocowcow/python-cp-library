from collections import defaultdict


class UnionFind:
    def __init__(self, n):
        self.parent = [0]*n
        for i in range(n):
            self.parent[i] = i

    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)
        if px != py:
            self.parent[px] = py

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]


uf = UnionFind(6)
uf.union(1, 2)
uf.union(1, 5)
uf.union(3, 4)
uf.union(5, 2)
uf.union(1, 3)


print(uf.parent)
print(uf.find(3))
