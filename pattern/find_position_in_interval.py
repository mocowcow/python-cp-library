from sortedcontainers import SortedList
from bisect import bisect_right
import math

# [start,end)
sl = SortedList()
sl.add([1, 3])
sl.add([3, 4])
sl.add([4, 5])
sl.add([5, 7])
sl.add([7, 11])


# 查找位置n被哪一個區間包含
def find(n):
    # idx = bisect_right(sl, [n, math.inf])-1
    idx = sl.bisect_right([n, math.inf])-1
    print(n, 'in', sl[idx])


for n in range(1, 11):
    find(n)
