
# 在有序陣列 求中位數
# 左中位數索引為 (N-1)/2
# 右中位數索引為 N/2
nums = []

# example:
# l = (N-1)/2 = 1, nums[l] = 2
# r = N/2 = 2, nums[r]= 3
# median = (2+3)/2 = 2.5

# example2:
# nums = [1,2,3], N = 3
# l = (N-1)/2 = 1, nums[l] = 2
# r = N/2 = 1, nums[r] = 2
# median = (2+3)/2 = 2

N = len(nums)
l = (N-1)//2
r = N//2
median = (nums[l]+nums[r])//2

# 簡短版本
N = len(nums)
median = (nums[(N-1)//2]+nums[N//2])//2
