from typing import List


class BinaryIndexedTree:

    def __init__(self, n):
        self.bit = [0]*(n+1)
        self.N = len(self.bit)

    def update(self, index, val):
        index += 1
        while index < self.N:
            self.bit[index] += val
            index = index + (index & -index)

    def prefixSum(self, index):
        index += 1
        res = 0
        while index > 0:
            res += self.bit[index]
            index = index - (index & -index)
        return res


class BinaryIndexedTreeWithList:

    def __init__(self, nums: List[int]):
        self.bit = [0]+nums  # restore range sum
        self.nums = nums  # original list
        self.N = len(self.bit)
        for i in range(1, self.N):
            j = i+(i & -i)
            if j < self.N:
                self.bit[j] += self.bit[i]

    # add value to a certain index
    def update(self, index: int, val: int) -> None:
        self.nums[index] += val
        index += 1
        while index < self.N:
            self.bit[index] += val
            index = index + (index & -index)

    # modify value to a certain index
    def set(self, index: int, val: int) -> None:
        diff = val-self.nums[index]
        self.update(index, diff)

    # get prefix sum from 0 to index
    def prefixSum(self, index: int) -> int:
        index += 1
        res = 0
        while index > 0:
            res += self.bit[index]
            index = index - (index & -index)
        return res

    # get prefix sum from left to right
    def sumRange(self, left: int, right: int) -> int:
        return self.prefixSum(right)-self.prefixSum(left-1)

    def getOriginalList(self) -> List:
        return self.nums


bit = BinaryIndexedTreeWithList([1, 3, 5, 7])
print(bit.getOriginalList())
print(bit.prefixSum(0))
print(bit.prefixSum(1))
print(bit.prefixSum(2))
bit.set(1, 9)
print(bit.getOriginalList())  # [1,9,5,7]
print(bit.prefixSum(0))
print(bit.prefixSum(1))
print(bit.prefixSum(2))
bit.update(0, 5)
print(bit.getOriginalList())  # [6,9,5,7]
print(bit.prefixSum(3))  # 27
print(bit.sumRange(1, 3))  # 21
