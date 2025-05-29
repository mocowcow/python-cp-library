import random
from basic_sorting import selection, bubble, insertion, quick, merge

TEST_CASES = 1000
TEST_CASE_SIZE = 1000


def get_random_arr():
    return [random.random() for _ in range(TEST_CASE_SIZE)]


def test_same():
    arr = get_random_arr()
    target = sorted(arr)
    for _ in range(TEST_CASES):
        random.shuffle(arr)
        assert target == selection(arr.copy())
        assert target == bubble(arr.copy())
        assert target == insertion(arr.copy())
        assert target == quick(arr.copy())
        assert target == merge(arr.copy())
