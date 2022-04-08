

class Node:
    def __init__(self, L, R, used):
        self.L = L
        self.R = R
        self.used = used
        self.left = self.right = None


class SegmentTree:
    def __init__(self, L, R):
        self.root = Node(L, R, False)

    def query(self, i, j):
        return self._q(self.root, i, j)

    def _q(self, node, i, j):
        if i > node.R or j < node.L:  # out of range
            return True
        if i <= node.L and j >= node.R:  # fully covered
            return node.used
        if not node.left:
            return node.used
        return self._q(node.right, i, j) and self._q(node.left, i, j)

    def update(self, i, j, used):
        self._u(self.root, i, j, used)

    def _u(self, node, i, j, used):
        if i > node.R or j < node.L:  # out of range
            return
        if i <= node.L and j >= node.R:  # fully covered
            node.used = used
            node.left = node.right = None
            return
        M = (node.L+node.R)//2
        if not node.left:
            node.left = Node(node.L, M, node.used)
            node.right = Node(M+1, node.R, node.used)
        if M >= i:
            self._u(node.left, i, j, used)
        if M < j:
            self._u(node.right, i, j, used)
        node.used = node.left.used and node.right.used
