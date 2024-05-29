

# 計算區間 [0, num] 中有多少個 1 位元
# LC 3007 https://leetcode.com/problems/maximum-number-that-sum-of-the-prices-is-less-than-or-equal-to-k/
# LC 3145 https://leetcode.com/problems/find-products-of-elements-of-big-array/


"""
num binary
0   0000
1   0001
2   0010
3   0011
4   0100
5   0101
6   0110
7   0111
8   1000
9   1001
10  1010
11  1011
..
"""

# 第 i = 0 位的規律是 01 01 ..
# 第 i = 1 位的規律是 0011 0011 ..
# 第 i = 2 位的規律是 00001111 00001111 ..

# 發現 0/1 的出現規律：
# 對於第 i 位來說，以 size = 2^(i + 1) 個元素為一次循環
# 每次循環中，前半 2^i 個元素都是 0，後半 2^i 個元素都是 1
# 剩餘 size 個不屬於循環的元素額外處理


def count(num):
    num += 1
    bit_cnt = 0
    for i in range(num.bit_length()):
        rep_size, rep_half_size = 1 << (i + 1), 1 << i
        rep_cnt, extra = divmod(num, rep_size)

        # rep_cnt are complete
        bit_cnt += rep_half_size * rep_cnt

        # extra numbers are lonely
        # but only last half part are 1s
        extra -= rep_half_size
        if extra > 0:
            bit_cnt += extra
    return bit_cnt
