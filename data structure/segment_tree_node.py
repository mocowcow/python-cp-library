
class Node:
    def __init__(self, start, end):
        self.sum = 0
        self.start = start
        self.end = end
        self.left = self.right = None


class SegmentTree:
    def __init__(self, nums):
        self.nums = nums
        self.root = self.build(0, len(nums)-1)

    def build(self, start, end):
        if start > end:
            return None
        node = Node(start, end)
        if start != end:
            mid = (start+end)//2
            node.left = self.build(start, mid)
            node.right = self.build(mid+1, end)
            node.sum = node.left.sum+node.right.sum
        else:
            node.sum = self.nums[start]
        return node

    def query(self, start, end):
        def _query(node, start, end):
            if not node:
                return 0
            if node.start > end or node.end < start:
                return 0
            if start <= node.start and node.end <= end:
                return node.sum
            return _query(node.left, start, end)+_query(node.right, start, end)

        return _query(self.root, start, end)

    def update(self, idx, diff):
        def _update(node, idx, diff):
            if not node:
                return
            if node.start <= idx <= node.end:
                node.sum += diff
                _update(node.left, idx, diff)
                _update(node.right, idx, diff)
        if diff != 0:
            self.nums[idx] += diff
            _update(self.root, idx, diff)

    def set(self, idx, val):
        diff = val-self.nums[idx]
        self.update(idx, diff)


st = SegmentTree([1, 2, 3, 4, 5, 0, 1, 2])  # total 18
print(st.query(0, 2))  # 6
st.update(0, 10)  # [11, 2, 3, 4, 5, 0, 1, 2]
print(st.query(0, 2))  # 16
print(st.query(0, 7))  # 28
st.set(0, 0)  # [0, 2, 3, 4, 5, 0, 1, 2]
print(st.query(0, 7))  # 17
