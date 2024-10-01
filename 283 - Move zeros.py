from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        l = 0
        for r in range(0,len(nums)):
            if nums[r]:
                nums[l] , nums[r] = nums[r], nums[l]
                l+=1
        return nums
