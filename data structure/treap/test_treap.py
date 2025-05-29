from sortedcontainers import SortedList as SL
import random
from treap import Treap


TEST_CASES = 1000
TEST_CASE_SIZE = 1000


def get_random_arr():
    return [random.random() for _ in range(TEST_CASE_SIZE)]


def test_min_max():
    for _ in range(TEST_CASES):
        sl = SL()
        tree = Treap()
        arr = get_random_arr()
        for x in arr:
            sl.add(x)
            tree.add(x)
            assert sl[0] == tree.min()
            assert sl[-1] == tree.max()


def test_bisect():
    sl = SL()
    tree = Treap()
    arr = get_random_arr()
    for x in arr:
        sl.add(x)
        tree.add(x)
    for _ in range(TEST_CASES):
        x = random.random()
        assert sl.bisect_left(x) == tree.lower_bound_index(x)
        assert sl.bisect_right(x) == tree.upper_bound_index(x)
