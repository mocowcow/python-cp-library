
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
            return False
        if i <= node.L and j >= node.R:  # fully covered
            return node.used
        if not node.left:
            return node.used
        return self._q(node.right, i, j) or self._q(node.left, i, j)

    def update(self, i, j):
        self._u(self.root, i, j)

    def _u(self, node, i, j):
        if i > node.R or j < node.L:  # out of range
            return
        if i <= node.L and j >= node.R:  # fully covered
            node.used = True
            node.left = node.right = None
            return
        M = (node.L+node.R)//2
        if not node.left:
            node.left = Node(node.L, M, node.used)
            node.right = Node(M+1, node.R, node.used)
        if M >= i:
            self._u(node.left, i, j)
        if M < j:
            self._u(node.right, i, j)
        node.used = node.left.used or node.right.used


def f(i, j):
    used = st.query(i, j-1)
    if not used:
        st.update(i, j-1)
        print('set', i, j-1, 'to True')
    else:
        print('!!!   FAILED', i, j-1)


st = SegmentTree(0, 10**9+5)

test = [[377791053, 395853223], [363789408, 379405233]]
for a, b in test:
    f(a, b)
