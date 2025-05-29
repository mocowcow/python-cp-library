import random


def swap(nums, i, j):
    nums[i], nums[j] = nums[j], nums[i]


def selection(a):
    """
    選擇排序法 O(N^2)

    - 從左到右枚舉要填的位置 i
    - 從 a[i..] 找到最小元素的位置 mn_i
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
    """
    泡沫排序法 O(N^2)

    - 從左到右檢查所有數對 (i, i+1)
    - 若 a[i] > a[i+1] 則交換

    每次都會讓最大的的元素浮到最右邊，循環 N 次後必定有序。
    """
    N = len(a)
    for rep in range(N):
        for i in range(N-1-rep):  # 優化：最後 rep 個元素已經排序
            if a[i] > a[i+1]:
                swap(a, i, i+1)
    return a


def insertion(a):
    """"
    插入排序法 O(N^2)

    - 枚舉當前要插入的第 i 個元素 val
    - 在左方已排序的 a[..i-1] 找到適合的位置 j  
    - 把 a[j..i-1] 的元素都右移到 a[j+1..i]
    - 最後在 a[j] 插入 val
    """
    N = len(a)
    for i in range(1, N):
        val = a[i]
        j = i  # val 目前預定要放到 a[j]
        while j > 0 and a[j-1] > val:  # 若 a[j-1] 比 val 大，則 val 更應該放 a[j-1]
            a[j] = a[j-1]  # 原有的元素像右移，讓出空位給 val
            j -= 1
        a[j] = val
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
