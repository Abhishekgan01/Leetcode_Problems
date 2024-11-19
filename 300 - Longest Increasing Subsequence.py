from typing import List

import bisect
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
         sub = []
         for num in nums:
            i = bisect.bisect_left(sub, num) #finds the index where the value should be inserted
            if i < len(sub):
                sub[i] = num
            else:
                sub.append(num)
    
         return len(sub)