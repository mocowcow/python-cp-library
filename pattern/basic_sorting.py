

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
        a[i], a[mn] = a[mn], a[i]
        print(a)
    return a


def bubble(src):
    # 泡沫排序法
    # 將較大的元素不斷右移
    print('bubble sort')
    print('origin=', src)
    a = src[:]
    N = len(a)
    for i in range(N-1, 0, -1):
        for j in range(i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
        print(a)
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


src = [5555, 456, 8, 7, 3, 21, 5, 6, 0, -5, 8, 56, 777, 88]
src=[3,2,1,0,-1]
# assert sorted(src) == selection(src)
assert sorted(src) == bubble(src)
# assert sorted(src) == insertion(src)
