
class Node:
    __slots__ = ['L', 'R', 'sm', 'left', 'right']

    def __init__(self, L, R, sm):
        self.L = L
        self.R = R
        self.sm = sm
        self.left = self.right = None


class SegmentTree:
    def __init__(self, L, R):
        self.root = Node(L, R, 0)

    def query(self, i, j):
        return self._q(self.root, i, j)

    def _q(self, node, i, j):
        if not node:
            return 0
        if i > node.R or j < node.L:  # out of range
            return 0
        if i <= node.L and j >= node.R:  # fully covered
            return node.sm
        return self._q(node.right, i, j) + self._q(node.left, i, j)

    def update(self, i, j, val):
        self._u(self.root, i, j, val)

    def _u(self, node, i, j, val):
        if i > node.R or j < node.L:  # out of range
            return
        if node.L == node.R:  # single index
            node.sm += val
            return
        M = (node.L+node.R)//2
        if not node.left:
            node.left = Node(node.L, M, 0)
            node.right = Node(M+1, node.R, 0)
        if M >= i:
            self._u(node.left, i, j, val)
        if M < j:
            self._u(node.right, i, j, val)
        node.sm = node.left.sm + node.right.sm


st = SegmentTree(0, 10**9+5)
st.update(1, 1000, 1)
assert st.query(1, 1000) == 1000
assert st.query(1, 900) == 900
assert st.query(900, 900) == 1
assert st.query(890, 900) == 11
st.update(500, 10000, 1)
assert st.query(900, 999) == 200
