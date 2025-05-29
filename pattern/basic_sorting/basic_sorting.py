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
            a[j] = a[j-1]  # a[j] 原有的元素右移，讓出空位給 val
            j -= 1
        a[j] = val
    return a


def quick(a):
    """
    快速排序法 O(N log N)

    基於分治思想。
    - 選擇隨機值 pivot，將陣列 a 劃分成兩塊
        - 小於 pivot 放到左半
        - 大於等於 pivot 放到右半
    - 遞迴處理左半和右半

    退出遞迴後，左右半都已經排序。且劃分時就保證左半的值都小於等於右半，故 a 已經完成排序。
    """
    N = len(a)

    def _partition(left, right):
        idx = random.randint(left, right)  # 隨機選一個位置當樞紐
        pivot = a[idx]  # 劃分樞紐值

        # 先把 pivot 丟到最右邊
        swap(a, idx, right)
        # 開始劃分
        i = left
        for j in range(left, right):
            if a[j] < pivot:
                swap(a, i, j)
                i += 1
        # 把 pivot 換回中間
        swap(a, i, right)
        return i  # 回傳 pivot 所在位置

    def _qs(left, right):
        if left < right:
            idx = _partition(left, right)
            _qs(left, idx-1)  # 左半邊都小於 pivot
            _qs(idx+1, right)  # 右半邊都大於等於 pivot

    _qs(0, N-1)
    return a


def merge(a):
    """
    合併排序法 O(N log N)

    基於分治思想。
    - 將陣列 a 正好切兩半
    - 遞迴排序左半、右半
    - 兩右半都有序，只需進行簡單的合併
    """

    def _ms(sub):
        N = len(sub)
        if N == 1:
            return sub
        # 劃分成兩半，分別排序
        M = N // 2
        sub_left, sub_right = _ms(sub[:M]), _ms(sub[M:])
        # 合併左右半
        res = []
        i = j = 0
        while i < len(sub_left) and j < len(sub_right):
            if sub_left[i] <= sub_right[j]:
                res.append(sub_left[i])
                i += 1
            else:
                res.append(sub_right[j])
                j += 1
        res.extend(sub_left[i:])
        res.extend(sub_right[j:])
        return res

    return _ms(a)
