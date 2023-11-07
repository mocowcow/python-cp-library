from math import inf


class BIT:
    """
    tree[0]代表空區間，不可存值，基本情況下只有[1, n-1]可以存值。
    offset為索引偏移量，若設置為1時正好可以對應普通陣列的索引操作。
    注意：只能查前綴極值。若求max則tree[i]值只能增、不能減。
    """

    def __init__(self, n, offset=1):
        self.offset = offset
        self.tree = [-inf]*(n+offset)

    def update(self, pos, val):
        """
        將tree[pos]設成val
        """
        i = pos+self.offset
        while i < len(self.tree):
            self.tree[i] = max(self.tree[i], val)
            i += i & (-i)

    def query(self, pos):
        """
        查詢[1, pos]的max
        """
        i = pos+self.offset
        res = -inf
        while i > 0:
            res = max(res, self.tree[i])
            i -= i & (-i)
        return res
