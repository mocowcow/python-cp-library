

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
# 在a中找第一個不小於x的元素位置
# -1可得到最後一個小於x的元素位置
def bs_left(a, x):
    lo = 0
    hi = len(a)-1
    while lo < hi:
        mid = (lo+hi) // 2
        if a[mid] < x:
            lo = mid+1
        else:
            hi = mid
    return lo


# bisect_right() in Python
# upper_bound() in C++
# 在a中找第一個大於x的元素位置
# -1可得到最後一個不大於x的元素位置
def bs_right(a, x):
    lo = 0
    hi = len(a)-1
    while lo < hi:
        mid = (lo+hi) // 2
        if a[mid] <= x:
            lo = mid+1
        else:
            hi = mid
    return lo


# 用特定函數確認是否在有效範圍內
# 依情況調整上界
# 依函數邏輯調整排除條件
# 排除條件不同，有時需改變中位數取向避免死循環
def bs_with_function(a, x):

    def isValid(val):
        pass

    lo = 0
    hi = 10000000
    while lo < hi:
        mid = (lo+hi) // 2
        if isValid(mid):
            lo = mid
        else:
            hi = mid-1
    return lo


a = [1, 4, 5, 6, 6, 10, 11, 15, 20, 55, 99]
i = bs_right(a, 6)-1  # 最後一個<=6的位置
print('idx=', i, ', nums=', a[i])
