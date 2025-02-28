"""

輸入陣列 xs 代表 x 軸上的有序座標點。  

N = len(xs)。  
xs 構成 N-1 個區間線段，初始化線段長度 = xs[i+1] s[i]。  

節點維護：  
- l：左端點對應的 xs[l]  
- r：右端點對應的 xs[r]  
- min_cnt：當前區間內的最小值  
- min_length：當前區間內最小值的長度
- lazy：min_cnt 懶標

LC 850 https://leetcode.com/problems/rectangle-area-ii/
LC 3454 https://leetcode.com/problems/separate-squares-ii/

"""


class Node:
    def __init__(self):
        self.l = 0
        self.r = 0
        self.min_cnt = 0
        self.min_length = 0
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
            o.min_length = xs[l+1] - xs[l]
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
            lc.lazy += o.lazy
            lc.min_cnt += o.lazy
            rc.lazy += o.lazy
            rc.min_cnt += o.lazy
            o.lazy = 0

    def push_up(self, id):
        o = self.nodes[id]
        lc = self.nodes[id*2]
        rc = self.nodes[id*2+1]
        o.min_cnt = min(lc.min_cnt, rc.min_cnt)
        o.min_length = 0
        if lc.min_cnt == o.min_cnt:
            o.min_length = lc.min_length
        if rc.min_cnt == o.min_cnt:
            o.min_length += rc.min_length

    def update(self, id, i, j, val):
        o = self.nodes[id]
        if i <= o.l and o.r <= j:
            o.min_cnt += val
            o.lazy += val
            return

        m = (o.l + o.r) // 2
        self.push_down(id)
        if i <= m:
            self.update(id*2, i, j, val)
        if m < j:
            self.update(id*2+1, i, j, val)
        self.push_up(id)

    def get_uncovered(self):
        root = self.nodes[1]
        if root.min_cnt > 0:
            return 0
        return root.min_length
