from itertools import accumulate
import random

# 前綴和 求 距離和
# 有序陣列中所有元素改成 nums[mid] 的距離總和
# LC2602 https://leetcode.com/problems/minimum-operations-to-make-all-array-elements-equal
# LC2615 https://leetcode.com/problems/sum-of-distances
# LC2968 https://leetcode.com/problems/apply-operations-to-maximize-frequency-score
# LC3806 https://leetcode.com/problems/minimum-moves-to-pick-k-ones/submissions/


class PrefixSum:
    def __init__(self, nums):
        self.N = len(nums)
        self.nums = nums
        self.ps = list(accumulate(nums, initial=0))

    def distance_sum(self, mid, left=0, right=None):
        """
        nums[left, right] 全部改成 nums[mid] 的距離總和
        預設範圍為 [0, N - 1]
        """
        t = self.nums[mid]
        ps = self.ps
        if right is None:
            right = self.N - 1

        s1 = (mid - left + 1) * t  # [left, mid]
        s1 -= (ps[mid + 1] - ps[left])
        s2 = ps[right + 1] - ps[mid]  # [mid, right]
        s2 -= (right - mid + 1) * t
        return s1 + s2


def brute_sum(nums, i, left, right):
    res = 0
    for j in range(left, right + 1):
        res += abs(nums[j] - nums[i])
    return res


def test_same():
    N = 100
    nums = [random.randint(0, 114514) for _ in range(N)]
    nums.sort()
    for _ in range(1000):
        mid = random.randint(0, N - 1)
        left = random.randint(0, mid)
        right = random.randint(mid, N - 1)
        ps = PrefixSum(nums)
        sum1 = ps.distance_sum(mid, left, right)
        sum2 = brute_sum(nums, mid, left, right)
        assert (sum1 == sum2)
    print('passed')


test_same()
