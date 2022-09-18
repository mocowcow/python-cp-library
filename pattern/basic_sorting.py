import random


def swap(nums, a, b):
    nums[a], nums[b] = nums[b], nums[a]


def selection(src):
    # 選擇排序法
    # 找到後方最小元素與i交換
    print('selection sort')
    print('origin=', src)
    a = src[:]
    N = len(a)
    for i in range(N):
        mn = i
        for j in range(i+1, N):
            if a[j] < a[mn]:
                mn = j
        swap(a, i, mn)
        print(a)
    return a


def bubble(src):
    # 泡沫排序法
    # 將較大的元素不斷右移
    print('bubble sort')
    print('origin=', src)
    a = src[:]
    N = len(a)
    for i in range(N):
        for j in range(1, N-i):
            if a[j-1] > a[j]:
                swap(a, j-1, j)
    return a


def insertion(src):
    # 插入排序法
    # 將當前元素插入左方有序部分
    print('insertion sort')
    print('origin=', src)
    a = src[:]
    N = len(a)
    for i in range(1, N):
        val = a[i]
        j = i-1
        while j >= 0 and a[j] > val:
            a[j+1] = a[j]
            j -= 1
        a[j+1] = val
        print(a)

    return a


def quick(src):
    print('quick sort')
    print('origin=', src)
    a = src[:]
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


src = [5555, 456, 8, 7, 3, 21, 5, 6, 0, -5, 8, 56, 777, 88]
src = [3, 2, 1, 0, -1]
# assert sorted(src) == selection(src)
# assert sorted(src) == bubble(src)
# assert sorted(src) == insertion(src)
# assert sorted(src) == quick(src)
