from collections import defaultdict


class TrieNode:
    def __init__(self) -> None:
        self.child = defaultdict(TrieNode)
        self.cnt = 0


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add(self, s) -> None:
        curr = self.root
        for c in s:
            curr = curr.child[c]
            # curr.cnt += 1  # count prefix
        curr.cnt += 1  # count whole string

    def find(self, s) -> bool:
        curr = self.root
        for c in s:
            if c not in curr.child:
                return False
            curr = curr.child[c]
        return curr.cnt > 0

    def kill(self, s) -> None:
        curr = self.root
        for c in s:
            curr = curr.child[c]
            # curr.cnt -= 1  # count prefix
        curr.cnt -= 1  # coutn whole string
