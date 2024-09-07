from typing import List
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sum=0
        sums=0
        for i in nums:
            sum+=i
        for j in range(len(nums)+1):
            sums+=j
        return sums-sum