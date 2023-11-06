
class BIT:
    """
    tree[0]代表空區間，不可存值，基本情況下只有[1, n-1]可以存值。
    offset為索引偏移量，若設置為1時正好可以對應普通陣列的索引操作。
    """

    def __init__(self, n, offset=1):
        self.offset = offset
        self.tree = [0]*(n+offset)

    def update(self, pos, val):
        """
        將tree[pos]增加val
        """
        i = pos+self.offset
        while i < len(self.tree):
            self.tree[i] += val
            i += i & (-i)

    def query(self, pos):
        """
        查詢[1, pos]的前綴和
        """
        i = pos+self.offset
        res = 0
        while i > 0:
            res += self.tree[i]
            i -= i & (-i)
        return res

    def query_range(self, i, j):
        """
        查詢[i, j]的前綴和
        """
        return self.query(j)-self.query(i-1)

    def set(self, pos, val):
        """
        將tree[pos]設成val
        """
        old = self.query_range(pos, pos)
        diff = val-old
        self.update(pos, diff)
