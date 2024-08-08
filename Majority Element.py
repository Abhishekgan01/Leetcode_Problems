from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        values = {}
        for num in nums:  
            if num in values: 
                values[num] += 1
            else:
                values[num] = 1
        return max(values, key=values.get)  