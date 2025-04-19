

"""
找下一個字典序更大的排列
若不存在更大的排列，則重排成最小的排列

- step 1:
使字典序變大，需要找到滿足 nums[i] < nums[j] 的索引 i, j 進行交換。
為了使增加的量盡可能小，i 的位置應該越靠右越好。
故從右向左枚舉索引 i，只要有 nums[i] < nums[i+1]，則保證 j 一定存在。  

若有找到，進入 step 2，決定 j 的位置；
找不到則代表 nums 是遞減的，已經是最大排列，直接跳到 step 3 反轉整個陣列，得到最小的排列。

- step 2:
確定 nums[i] 的位置，再來要找交換的目標 nums[j]。
已知 i+1 <= j < N，且 nums[i+1..] 是遞減的。
為了使增加的量盡可能小，應從 i+1 向右找，找到最靠右、滿足 nums[i] < nums[j] 的 j。
交換 nums[i], nums[j]，進入 step 3。

- step 3:
交換 nums[i], nums[j] 後，已經變得比原本的排列大。
但是要求的是"正好下一個"，所以要保證 nums[i+1..] 這部分的字典序最小化。
交換 i, j 並不會破壞 nums[i+1..] 的遞減特性。
遞減同時也代表著最大的字典序，反轉 num[i+1..] 將字典序變成最小。

注意：若 nums 原本是最大字典序，則 step 1 找不到合法的 i 會停在 -1。  
此時 i+1 為 0，正好反轉整個陣列。
"""


def next_permutation(nums):
    N = len(nums)

    i = N-2
    while i >= 0:
        if nums[i] < nums[i+1]:
            break
        else:
            i -= 1

    if i >= 0:
        j = i+1
        while j+1 < N and nums[i] < nums[j+1]:
            j += 1
        nums[i], nums[j] = nums[j], nums[i]

    l, r = i+1, N-1
    while l < r:
        nums[l], nums[r] = nums[r], nums[l]
        l += 1
        r -= 1
