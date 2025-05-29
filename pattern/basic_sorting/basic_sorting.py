import random


def swap(nums, i, j):
    nums[i], nums[j] = nums[j], nums[i]


def selection(a):
    """
    選擇排序法

    枚舉要填的位置 i
    - 從 a[i..] 找到最小元素位置 mn_i
    - 把 a[mn_i] 填入 a[i]
    """
    N = len(a)
    for i in range(N):
        mn_i = i
        for j in range(i+1, N):
            if a[j] < a[mn_i]:
                mn_i = j
        swap(a, i, mn_i)
    return a


def bubble(a):
    # 泡沫排序法
    # 將較大的元素不斷右移
    N = len(a)
    for i in range(N):
        for j in range(1, N-i):
            if a[j-1] > a[j]:
                swap(a, j-1, j)
    return a


def insertion(a):
    # 插入排序法
    # 將當前元素插入左方有序部分
    N = len(a)
    for i in range(1, N):
        val = a[i]
        j = i-1
        while j >= 0 and a[j] > val:
            a[j+1] = a[j]
            j -= 1
        a[j+1] = val
    return a


def quick(a):
    N = len(a)

    def partition(nums, left, right):
        idx = random.randint(left, right)
        pivot = nums[idx]
        # move pivot to right most
        swap(nums, idx, right)
        # partition
        i = left
        for j in range(left, right):
            if nums[j] < pivot:
                swap(nums, i, j)
                i += 1
        # move pivot to middle
        swap(nums, i, right)
        return i

    def qs(nums, left, right):
        if left < right:
            idx = partition(nums, left, right)
            qs(nums, left, idx-1)
            qs(nums, idx+1, right)

    qs(a, 0, N-1)
    return a


def merge(a):

    def f(a):
        N = len(a)
        if N == 1:
            return a
        M = N // 2
        L, R = f(a[:M]), f(a[M:])
        res = []
        i = j = 0
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                res.append(L[i])
                i += 1
            else:
                res.append(R[j])
                j += 1
        res.extend(L[i:])
        res.extend(R[j:])
        return res

    return f(a)
