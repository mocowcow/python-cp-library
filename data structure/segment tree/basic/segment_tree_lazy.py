
class SegmentTree:

    def __init__(self, n):
        self.tree = [0]*(4*n)
        self.lazy = [0]*(4*n)

    def build(self, init, id, L, R):
        """
        初始化線段樹
        若無初始值則不需執行
        """
        if L == R:  # 到達葉節點
            self.tree[id] = init[L]
            return
        M = (L+R)//2
        self.build(init, id*2, L, M)
        self.build(init, id*2+1, M+1, R)
        self.push_up(id)

    def op(self, a, b):
        """
        任意符合結合律的運算
        """
        return a+b

    def push_down(self, id, L, R):
        """
        將區間懶標加到答案中
        下推懶標記給左右子樹
        """
        M = (L+R)//2
        if self.lazy[id]:
            self.lazy[id*2] += self.lazy[id]
            self.tree[id*2] += self.lazy[id]*(M-L+1)
            self.lazy[id*2+1] += self.lazy[id]
            self.tree[id*2+1] += self.lazy[id]*(R-(M+1)+1)
            self.lazy[id] = 0

    def push_up(self, id):
        """
        以左右節點更新當前節點值
        """
        self.tree[id] = self.op(self.tree[id*2], self.tree[id*2+1])

    def query(self, id, L, R, i, j):
        """
        區間查詢
        回傳[i, j]的總和
        """
        if i <= L and R <= j:  # 當前區間目標範圍包含
            return self.tree[id]
        self.push_down(id, L, R)
        res = 0
        M = (L+R)//2
        if i <= M:
            res = self.op(res, self.query(id*2, L, M, i, j))
        if M+1 <= j:
            res = self.op(res, self.query(id*2+1, M+1, R, i, j))
        return res

    def update(self, id, L, R, i, j, val):
        """
        區間更新
        對[i, j]每個索引都增加val
        """
        if L == R:  # 當前區間目標範圍包含
            self.tree[id] += val
            return
        self.push_down(id, L, R)
        M = (L+R)//2
        if i <= M:
            self.update(id*2, L, M, i, j, val)
        else:
            self.update(id*2+1, M+1, R, i, j, val)
        self.push_up(id)
