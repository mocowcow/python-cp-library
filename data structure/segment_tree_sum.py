
class SegmentTree:
    def __init__(self, nums):
        self.N = len(nums)
        self.nums = nums
        self.st = [0]*(self.N*4)
        self.build(0, self.N-1, 1)

    def build(self, start, end, id):
        if start == end:
            self.st[id] = self.nums[start]
        else:
            mid = (start+end)//2
            self.build(start, mid, id*2)
            self.build(mid+1, end, id*2+1)
            self.st[id] = self.st[id*2]+self.st[id*2+1]

    def query(self, start, end):
        def _query(l, r, L, R, id):
            if l == L and r == R:
                return self.st[id]
            M = (L+R)//2
            if r <= M:
                return _query(l, r, L, M, id*2)
            elif l > M:
                return _query(l, r, M+1, R, id*2+1)
            else:
                return _query(l, M, L, M, id*2)+_query(M+1, r, M+1, R, id*2+1)

        return _query(start, end, 0, self.N-1, 1)

    def set(self, idx, val):
        def _set(idx, val, id, L, R):
            if L == R:
                self.st[id] = val
            else:
                M = (L+R)//2
                if idx <= M:
                    _set(idx, val, id*2, L, M)
                else:
                    _set(idx, val, id*2+1, M+1, R)
                self.st[id] = self.st[id*2] + self.st[id*2+1]

        _set(idx, val, 1, 0, self.N-1)


st = SegmentTree([1, 2, 3, 4, 5, 0, 1, 2])  # total 18
st.set(0, 12)  # [11, 2, 3, 4, 5, 0, 1, 2]
print(st.query(0, 7))
