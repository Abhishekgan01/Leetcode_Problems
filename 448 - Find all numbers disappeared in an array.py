from typing import List

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i in nums:
            ind = abs(i) - 1
            nums[ind] = -abs(nums[ind])
        return [index+1 for index,number in enumerate(nums) if number>0]