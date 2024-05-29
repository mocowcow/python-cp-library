

# 構造滿足限制的極值
# 維護前綴 bitmask，從最高位元開始填答案
# LC 421 https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/
# LC 2935 https://leetcode.com/problems/maximum-strong-pair-xor-ii/
# LC 3022 https://leetcode.com/problems/minimize-or-of-remaining-elements-using-operations/


def build(nums):
    M = max(nums).bit_length()
    res = 0
    prefix = 0
    for i in reversed(range(M)):
        try_mask = res | (1 << i)  # 試著把答案第 i 位填 1
        prefix |= (1 << i)  # 需要考慮的前綴位元
        for x in nums:
            x &= prefix  # 清除不要的位元
            # 檢查條件，若滿足則更新答案
            if True:
                res = try_mask

    return res
