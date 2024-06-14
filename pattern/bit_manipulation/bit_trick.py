from collections import Counter


# LC 898 https://leetcode.com/problems/bitwise-ors-of-subarrays/
# LC 1521 https://leetcode.com/problems/find-a-value-of-a-mysterious-function-closest-to-target/
# LC 2411 https://leetcode.com/problems/smallest-subarrays-with-maximum-bitwise-or/
# LC 3171 https://leetcode.com/problems/find-subarray-with-bitwise-or-closest-to-k/


def bit_trick(nums):

    class item:
        def __init__(self, val, first, last) -> None:
            self.val = val  # 子陣列按位運算結果
            self.first = first  # 第一個滿足的端點
            self.last = last  # 最後一個滿足的端點

    d = Counter()
    op_res = []
    for i, x in enumerate(nums):
        op_res.append(item(x, i, i))
        tail = 0
        for it in op_res:
            it.val |= x  # 按位運算操作
            if op_res[tail].val != it.val:
                tail += 1
                op_res[tail] = it
            else:
                op_res[tail].last = it.last  # 更新最後端點
        del op_res[tail + 1:]  # op_res = op_res[:tail + 1]

        # 依按位運算結果統計子陣列個數
        for it in op_res:
            d[it.val] += it.last - it.first + 1
    return d
