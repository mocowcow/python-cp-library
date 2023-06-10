
class Node:
    __slots__ = ['L', 'R', 'mx', 'left', 'right']

    def __init__(self, L, R, mx):
        self.L = L
        self.R = R
        self.mx = mx
        self.left = self.right = None


class SegmentTree:
    def __init__(self, L, R):
        self.root = Node(L, R, 0)

    def query(self, i, j):
        return self._q(self.root, i, j)

    def _q(self, node, i, j):
        if i > node.R or j < node.L:  # out of range
            return 0
        if i <= node.L and j >= node.R:  # fully covered
            return node.mx
        if not node.left:
            return node.mx
        return max(self._q(node.right, i, j), self._q(node.left, i, j))

    def update(self, i, j, val):
        self._u(self.root, i, j, val)

    def _u(self, node, i, j, val):
        if i > node.R or j < node.L:  # out of range
            return
        if i <= node.L and j >= node.R:  # fully covered
            node.mx = val
            node.left = node.right = None
            return
        M = (node.L+node.R)//2
        if not node.left:
            node.left = Node(node.L, M, node.mx)
            node.right = Node(M+1, node.R, node.mx)
        if M >= i:
            self._u(node.left, i, j, val)
        if M < j:
            self._u(node.right, i, j, val)
        node.mx = max(node.left.mx, node.right.mx)
