from typing import List

class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        output = []
        nums.sort()
        for i in range(0,len(nums)):
            if nums[i] == target:
                output.append(i)
        if output == []:
            return []
        else:
            return output