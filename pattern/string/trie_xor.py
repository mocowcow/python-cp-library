from collections import defaultdict


# XOR字典樹
# 求val與任意元素的最大XOR值
# LC421 https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/
# LC1907 https://leetcode.com/problems/maximum-xor-with-an-element-from-array/
# LC1938 https://leetcode.com/problems/maximum-genetic-difference-query/
# LC2935 https://leetcode.com/problems/maximum-strong-pair-xor-ii/


class TrieNode:
    def __init__(self) -> None:
        self.child = defaultdict(TrieNode)
        self.cnt = 0


class Trie:
    def __init__(self, MX=20):
        self.MX = MX  # 最大位元數
        self.root = TrieNode()

    def add(self, val) -> None:
        curr = self.root
        for i in reversed(range(self.MX)):
            bit = (val >> i) & 1
            curr = curr.child[bit]
            curr.cnt += 1

    def find(self, val):
        curr = self.root
        res = 0
        for i in reversed(range(self.MX)):
            bit = (val >> i) & 1
            rev = bit ^ 1
            if curr.child[rev].cnt > 0:
                curr = curr.child[rev]
                res |= (1 << i)
            else:
                curr = curr.child[bit]
        return res

    def kill(self, val) -> None:
        curr = self.root
        for i in reversed(range(self.MX)):
            b = (val >> i) & 1
            curr = curr.child[b]
            curr.cnt -= 1
