from collections import Counter


# LC 898 https://leetcode.com/problems/bitwise-ors-of-subarrays/
# LC 1521 https://leetcode.com/problems/find-a-value-of-a-mysterious-function-closest-to-target/
# LC 2411 https://leetcode.com/problems/smallest-subarrays-with-maximum-bitwise-or/
# LC 3171 https://leetcode.com/problems/find-subarray-with-bitwise-or-closest-to-k/


def bit_trick(nums):

    class Item:
        """
        以索引 i 為固定右端點
        滿足子陣列 nums[j..i] 所有元素按位運算的結果等於 val
        其中 first <= j <= last
        """

        def __init__(self, val, first, last) -> None:
            self.val = val  # 子陣列按位運算結果
            self.first = first  # 最小的 j
            self.last = last  # 最大的 j

    freq = Counter()  # 依按位運算結果統計子陣列個數
    op_res = []
    for i, x in enumerate(nums):
        # 每個子陣列和 x 按位運算
        for it in op_res:
            it.val |= x  # OR, AND, GCD
        op_res.append(Item(x, i, i))

        # 去重合併，更新端點
        tail = 0
        for it in op_res:
            if op_res[tail].val != it.val:
                tail += 1
                op_res[tail] = it
            else:
                op_res[tail].last = it.last  # 更新最後端點
        del op_res[tail + 1:]  # op_res = op_res[:tail + 1]

        # 依按位運算結果更新答案
        for it in op_res:
            freq[it.val] += it.last - it.first + 1
    return freq
