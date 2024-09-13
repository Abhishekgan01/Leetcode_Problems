from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
       length  = 1
       for i in range(1,len(nums)):
        if nums[i] != nums[length-1]:
            nums[length] = nums[i]
            length += 1
       return length