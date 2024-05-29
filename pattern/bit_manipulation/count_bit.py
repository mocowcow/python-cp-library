

# 計算區間 [0, num] 中有多少個 1 位元
# LC 3007 https://leetcode.com/problems/maximum-number-that-sum-of-the-prices-is-less-than-or-equal-to-k/
# LC 3145 https://leetcode.com/problems/find-products-of-elements-of-big-array/


def count(num):
    num += 1
    bit_cnt = 0
    for i in range(num.bit_length()):
        rep_size = 1 << (i + 1)
        rep_cnt, extra = divmod(num, rep_size)

        # rep_cnt are complete
        bit_cnt += rep_size * rep_cnt

        # extra numbers are lonely
        # but only last half part are 1s
        extra -= rep_size // 2
        if extra > 0:
            bit_cnt += extra
    return bit_cnt
