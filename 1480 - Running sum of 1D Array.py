from typing import List

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        result=[]
        result.append(nums[0])
        sums = nums[0]
        for i in range(1,len(nums)):
            sums += nums[i]
            result.append(sums)
        return result