from typing import List

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        smaller = []
        for i in range(0,len(nums)):
            count = 0
            for j in range(0,len(nums)):
                if nums[i]>nums[j]:
                    count+=1
            smaller.append(count)
        return smaller