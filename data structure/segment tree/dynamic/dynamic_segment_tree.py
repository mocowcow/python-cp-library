
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

    def push_down(self):
        """
        動態開點
        """
        if not self.left:
            self.left = TreeNode(self.L, self.M)
            self.right = TreeNode(self.M+1, self.R)

    def push_up(self):
        """
        以左右節點更新當前節點值
        """
        assert self.left is not None and self.right is not None
        self.val = self.op(self.left.val, self.right.val)

    def update(self, pos, val):
        """
        單點更新
        將tree[pos]增加val
        """
        if self.L == self.R:
            self.val += val
            return
        self.push_down()
        assert self.left is not None and self.right is not None
        if pos <= self.M:
            self.left.update(pos, val)
        else:
            self.right.update(pos, val)
        self.push_up()

    def query(self, i, j):
        """
        區間查詢
        回傳[i, j]的總和
        """
        if i <= self.L and self.R <= j:
            return self.val
        res = self.default_value
        if i <= self.M and self.left:
            res = self.op(res, self.left.query(i, j))
        if self.M < j and self.right:
            res = self.op(res, self.right.query(i, j))
        return res
