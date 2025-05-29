from sortedcontainers import SortedList as SL
import random
from treap import Treap


TEST_CASES = 1000
TEST_CASE_SIZE = 1000


def get_random_arr():
    return [random.random() for _ in range(TEST_CASE_SIZE)]


def build():
    sl = SL()
    tree = Treap()
    for x in get_random_arr():
        sl.add(x)
        tree.add(x)
    return sl, tree


def test_min_max():
    sl, tree = build()
    for _ in range(TEST_CASES):
        x = random.random()
        sl.add(x)
        tree.add(x)
        assert sl[0] == tree.min()
        assert sl[-1] == tree.max()


def test_bisect():
    sl, tree = build()
    for _ in range(TEST_CASES):
        x = random.random()
        assert sl.bisect_left(x) == tree.lower_bound_index(x)
        assert sl.bisect_right(x) == tree.upper_bound_index(x)


def test_k_th():
    sl, tree = build()
    for _ in range(TEST_CASES):
        i = random.randint(0, len(sl)-1)
        assert sl[i] == tree.k_th(i)
