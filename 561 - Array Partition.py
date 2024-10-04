from typing import List

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums = sorted(nums)
        sum1 = sum(nums[::2])
        return sum1