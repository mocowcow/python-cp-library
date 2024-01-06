import bisect
import random


# Arrays.binarySearch() in Java
# 在a中找x的確切位置，找不到回傳-1
def bs_exactly(a, x):
    lo = 0
    hi = len(a)-1
    while lo <= hi:
        mid = (lo+hi) // 2
        if a[mid] == x:
            return mid
        elif a[mid] < x:
            lo = mid+1
        else:
            hi = mid-1
    return -1


# bisect_left() in Python
# lower_bound() in C++
# 找 第一個 "大於等於x" 的元素位置

# lb - 1可得 最後一個 "小於x" 的元素位置
# 注意：若a不存在 "大於等於x" 的元素，則lb = 0。此時lb - 1可能會越界
def bs_left(a, x):
    lo = 0
    hi = len(a)
    while lo < hi:
        mid = (lo+hi) // 2
        # 等價反向寫法
        # if not a[mid] >= x :
        if a[mid] < x:
            lo = mid+1
        else:
            hi = mid
    return lo


# bisect_right() in Python
# upper_bound() in C++
# 找 第一個 "大於x" 的元素位置

# rb - 1可得 最後一個 "小於等於x" 的元素位置
# 若a不存在 "大於x" 的元素，則rb = len(a)。可以此作為判斷標準
def bs_right(a, x):
    lo = 0
    hi = len(a)
    while lo < hi:
        mid = (lo+hi) // 2
        # 等價反向寫法
        # if not a[mid] > x :
        if a[mid] <= x:
            lo = mid+1
        else:
            hi = mid
    return lo


# 最大值最小化 / 最小值最大化
# 答案需具 "單調性"
# 若f(mid)不合法，則大於mid也不合法，更新上界為mid-1
# 若f(mid)合法，則小於mid也合法，更新下界為mid

# 排除條件不同，有時需改變中位數取向避免死循環
# 例如：
# 答案範圍是[F, F, .., T, T]時，取 左中位數，即(lo + hi) / 2
# 答案範圍是[T, T, .., F, F]時，取 右中位數，即(lo + hi + 1) / 2
def bs_with_function(a):

    def ok(mid):
        pass

    lo = 0
    hi = 10000000
    while lo < hi:
        mid = (lo+hi) // 2
        if not ok(mid):  # mid不合法，答案不可為mid
            hi = mid-1
        else:  # mid合法，答案至少為mid
            lo = mid
    return lo


def test_same(g, f):
    a = sorted([random.randint(0, 10000) for _ in range(10000)])
    for _ in range(10000):
        target = random.randint(0, 10000)
        assert (g(a, target) == f(a, target))
    print('passed')


test_same(bisect.bisect_left, bs_left)
test_same(bisect.bisect_right, bs_right)
