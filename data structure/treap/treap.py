import random
import time
from typing import Optional


class TreapNode:
    def __init__(self, key, priority):
        self.key = key
        self.priority = priority
        self.key_cnt = 1
        self.size = 1
        self.left = None
        self.right = None


class Treap:
    def __init__(self):
        self.root = None
        self.rng = random.Random(time.time())

    def _maintain(self, o):
        if not o:
            return
        o.size = o.key_cnt
        if o.left:
            o.size += o.left.size
        if o.right:
            o.size += o.right.size

    def _rotate_right(self, p):
        q = p.left
        p.left = q.right
        q.right = p
        self._maintain(p)
        self._maintain(q)
        return q

    def _rotate_left(self, p):
        q = p.right
        p.right = q.left
        q.left = p
        self._maintain(p)
        self._maintain(q)
        return q

    def _add(self, o, key):
        if not o:
            return TreapNode(key, self.rng.random())
        if key == o.key:
            o.key_cnt += 1
        elif key < o.key:
            o.left = self._add(o.left, key)
            if o.left.priority > o.priority:  # type: ignore
                o = self._rotate_right(o)
        else:
            o.right = self._add(o.right, key)
            if o.right.priority > o.priority:  # type: ignore
                o = self._rotate_left(o)
        self._maintain(o)
        return o

    def add(self, key):
        self.root = self._add(self.root, key)

    def _remove(self, o, key):
        if not o:
            return None
        if key == o.key:
            if o.key_cnt > 1:
                o.key_cnt -= 1
            else:
                if not o.left:
                    return o.right
                if not o.right:
                    return o.left
                if o.left.priority > o.right.priority:
                    o = self._rotate_right(o)
                    o.right = self._remove(o.right, key)
                else:
                    o = self._rotate_left(o)
                    o.left = self._remove(o.left, key)
        elif key < o.key:
            o.left = self._remove(o.left, key)
        else:
            o.right = self._remove(o.right, key)
        self._maintain(o)
        return o

    def remove(self, key):
        self.root = self._remove(self.root, key)

    def min(self):
        assert self.root is not None
        o = self.root
        while o.left:
            o = o.left
        return o.key

    def max(self):
        assert self.root is not None
        o = self.root
        while o.right:
            o = o.right
        return o.key
