
class TreeNode:
    """
    動態開點線段樹
    單點更新
    區間查詢
    """
    __slots__ = ["L", "R", "M", "val", "left", "right"]
    default_value = 0

    def __init__(self, L, R):
        self.L = L
        self.R = R
        self.M = (L+R)//2
        self.val = self.default_value
        self.left = self.right = None

    def op(self, a, b):
        """
        任意符合結合律的運算
        """
        return a+b

    def get(self, o):
        if o is None:
            return self.default_value
        return o.val

    def maintain(self):
        self.val = self.op(self.get(self.left), self.get(self.right))

    def update(self, pos, val):
        if self.L == self.R:
            self.val = val
            return
        if pos <= self.M:
            if not self.left:
                self.left = TreeNode(self.L, self.M)
            self.left.update(pos, val)
        else:
            if not self.right:
                self.right = TreeNode(self.M+1, self.R)
            self.right.update(pos, val)
        self.maintain()

    def query(self, i, j):
        if i <= self.L and self.R <= j:
            return self.val
        res = self.default_value
        if i <= self.M and self.left:
            res = self.op(res, self.left.query(i, j))
        if self.M < j and self.right:
            res = self.op(res, self.right.query(i, j))
        return res
