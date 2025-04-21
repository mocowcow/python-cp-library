
def segment_tree_discretization(queries):
    xs = set()
    for l, r in queries:
        xs.add(l)
        xs.add(r)
    xs = sorted(xs)
    mp = {x: i for i, x in enumerate(xs)}

    seg = SegmentTree(xs)
    for l, sz in queries:
        l, r = mp[l], mp[l+sz]-1


class Node:
    def __init__(self):
        self.l = 0
        self.r = 0
        self.val = 0
        self.lazy = 0


class SegmentTree:
    def __init__(self, xs):
        N = len(xs) - 1
        self.nodes = [Node() for _ in range(N * 4)]
        self.build(xs, 1, 0, N-1)

    def build(self, xs, id, l, r):
        o = self.nodes[id]
        o.l = l
        o.r = r
        if l == r:
            return

        m = (l + r) // 2
        self.build(xs, id*2, l, m)
        self.build(xs, id*2+1, m+1, r)
        self.push_up(id)

    def push_down(self, id):
        o = self.nodes[id]
        lc = self.nodes[id*2]
        rc = self.nodes[id*2+1]
        if o.lazy:
            lc.lazy = o.lazy
            lc.val = o.lazy
            rc.lazy = o.lazy
            rc.val = o.lazy
            o.lazy = 0

    def push_up(self, id):
        o = self.nodes[id]
        lc = self.nodes[id*2]
        rc = self.nodes[id*2+1]
        o.val = max(lc.val, rc.val)

    def query(self, id, i, j):
        o = self.nodes[id]
        if i <= o.l and o.r <= j:
            return o.val

        m = (o.l + o.r) // 2
        res = 0
        self.push_down(id)
        if i <= m:
            res = self.query(id*2, i, j)
        if m < j:
            res = max(res, self.query(id*2+1, i, j))
        return res

    def update(self, id, i, j, val):
        o = self.nodes[id]
        if i <= o.l and o.r <= j:
            o.val = val
            o.lazy = val
            return

        m = (o.l + o.r) // 2
        self.push_down(id)
        if i <= m:
            self.update(id*2, i, j, val)
        if m < j:
            self.update(id*2+1, i, j, val)
        self.push_up(id)
