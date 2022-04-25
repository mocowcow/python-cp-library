from itertools import accumulate


def prefix_sum(nums):
    N = len(nums)
    psum = [0]*(N+1)
    for i, n in enumerate(nums):
        psum[i+1] = psum[i]+n
    return psum


def prefix_sum_with_append(nums):
    psum = [0]
    for n in nums:
        psum.append(psum[-1]+n)
    return psum


def prefix_sum_with_accumulate(nums):
    return [0]+list(accumulate(nums))


psum = prefix_sum([1, 2, 3, 4, 6, 7, 10])
print(psum)
left, right = 3, 5  # nums[3]連加至nums[5]
print(psum[right+1]-psum[left])  # 17
left, right = 0, 2  # nums[0]連加至nums[2]
print(psum[right+1]-psum[left])  # 6
left, right = 1, 1  # nums[1]
print(psum[right+1]-psum[left])  # 2
