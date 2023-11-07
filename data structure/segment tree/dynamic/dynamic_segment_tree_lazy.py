
class LazyNode:
    """
    動態開點線段樹
    區間更新
    區間查詢
    """
    __slots__ = ["L", "R", "M", "val", "left", "right", "lazy"]
    default_value = 0

    def __init__(self, L, R):
        self.L = L
        self.R = R
        self.M = (L+R)//2
        self.val = self.default_value
        self.left = self.right = None
        self.lazy = 0

    def op(self, a, b):
        """
        任意符合結合律的運算
        """
        return a+b

    def push_down(self):
        """
        動態開點
        下放懶標
        """
        if not self.left:
            self.left = LazyNode(self.L, self.M)
            self.right = LazyNode(self.M+1, self.R)
        if self.lazy:
            self.left.val += (self.M-self.L+1)*self.lazy
            self.left.lazy += self.lazy
            self.right.val += (self.R-self.M)*self.lazy
            self.right.lazy += self.lazy
            self.lazy = 0

    def push_up(self):
        """
        以左右節點更新當前節點值
        """
        self.val = self.op(self.left.val, self.right.val)

    def update(self, i, j, val):
        """
        區間更新
        對[i, j]每個索引都增加val
        """
        if i <= self.L and self.R <= j:
            self.val += val*(self.R-self.L+1)
            self.lazy += val
            return
        self.push_down()
        if i <= self.M:
            self.left.update(i, j, val)
        if self.M < j:
            self.right.update(i, j, val)
        self.push_up()

    def query(self, i, j):
        """
        區間查詢
        回傳[i, j]的總和
        """
        if i <= self.L and self.R <= j:
            return self.val
        self.push_down()
        res = self.default_value
        if i <= self.M:
            res = self.op(res, self.left.query(i, j))
        if self.M < j:
            res = self.op(res, self.right.query(i, j))
        return res
