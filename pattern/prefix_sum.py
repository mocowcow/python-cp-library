from itertools import accumulate


def prefix_sum(nums):
    N = len(nums)
    psum = [0]*(N+1)
    for i, x in enumerate(nums):
        psum[i+1] = psum[i] + x
    return psum


def prefix_sum_with_append(nums):
    psum = [0]
    for x in nums:
        psum.append(psum[-1] + x)
    return psum


def prefix_sum_with_accumulate(nums):
    return list(accumulate(nums, initial=0))
