

class SegmentTree:

    def __init__(self, nums):
        self.nums = nums
        self.N = len(nums)
        self.tree = [0]*(self.N*4)
        self.lazy = [0]*(self.N*4)
        self.build(1, 0, self.N-1)

    def build(self, id, L, R):
        if L == R:
            self.tree[id] = self.nums[L]
            return
        M = (L+R)//2
        self.build(id*2, L, M)
        self.build(id*2+1, M+1, R)
        self.tree[id] = self.merge(self.tree[id*2], self.tree[id*2+1])

    def query(self, i, j):
        return self._q(1, 0, self.N-1, i, j)

    def _q(self, id, L, R, i, j):
        if L > j or R < i:
            return 0
        if self.lazy[id]:
            self.pushDown(id, L, R)
        if i <= L and R <= j:
            return self.tree[id]
        M = (L+R)//2
        lq = self._q(id*2, L, M, i, j)
        rq = self._q(id*2+1, M+1, R, i, j)
        return self.merge(lq, rq)

    def update(self, i, j, val):
        self._u(1, 0, self.N-1, i, j, val)

    def _u(self, id, L, R, i, j, val):
        if L > j or R < i:
            return
        if i <= L and R <= j:
            self.lazy[id] += val
            return
        self.pushDown(id, L, R)
        M = (L+R)//2
        if L <= M:
            self._u(id*2, L, M, i, j, val)
        if R > M:
            self._u(id*2+1, M+1, R, i, j, val)

    def merge(self, a, b):
        return a+b

    def pushDown(self, id, L, R):
        if self.lazy[id]:
            self.tree[id] += self.lazy[id]*(R-L+1)
            if L != R:
                self.lazy[id*2] += self.lazy[id]
                self.lazy[id*2+1] += self.lazy[id]
            self.lazy[id] = 0


nums = [1, 2, 3, 4, 5]
st = SegmentTree(nums)
print(st.query(0, 4))  # 15
st.update(0, 4, 10)  # all increase by 10
print('----------')
print(st.query(0, 4))  # 65
print('----------')
print(st.query(0, 0))     # 11
print(st.query(1, 1))  # 12
print(st.query(2, 2))  # 13
print(st.query(3, 3))  # 14
print(st.query(4, 4))  # 15
