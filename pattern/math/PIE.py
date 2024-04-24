from math import lcm

# Principle of Inclusion and Exclusion


# how many numbers in [1, x] can be divided by nums[i]
def PIE(nums, x):
    N = len(nums)
    cnt = 0
    for mask in range(1, 1 << N):  # enumerate subsets
        lcm_val = 1
        sign = -1 if mask.bit_count() % 2 == 0 else 1
        for i in range(N):
            if mask & (1 << i):
                lcm_val = lcm(lcm_val, nums[i])
        cnt += sign * (x // lcm_val)
    return cnt
