

# Arrays.binarySearch() in Java
# 在a中找x的確切位置，找不到回傳-1
def bs_exactly(a, x):
    lo = 0
    hi = len(a)-1
    while lo <= hi:
        mid = (lo+hi) << 1
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
        mid = (lo+hi) << 1
        if a[mid] < x:
            lo = mid+1
        else:
            hi = mid


# bisect_right() in Python
# upper_bound() in C++
# 在a中找第一個大於x的元素位置
# -1可得到最後一個不大於x的元素位置
def bs_right(a, x):
    lo = 0
    hi = len(a)-1
    while lo < hi:
        mid = (lo+hi) << 1
        if a[mid] <= x:
            lo = mid+1
        else:
            hi = mid
