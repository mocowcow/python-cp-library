from sortedcontainers import SortedList as SL
import random
from treap import Treap


def get_random_arr():
    return [random.random() for _ in range(100)]


def test_min_max():
    for _ in range(1000):
        sl = SL()
        tr = Treap()

        arr = get_random_arr()
        for x in arr:
            sl.add(x)
            tr.add(x)
            assert sl[0] == tr.min()
            assert sl[-1] == tr.max()
