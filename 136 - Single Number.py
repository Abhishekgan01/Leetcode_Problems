from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
       val = {}

       for i in nums:
        if i in val:
            val[i] += 1
        else:
            val[i] = 1

       for x, y in val.items():
        if y == 1:
            return x
            