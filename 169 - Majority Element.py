from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = {}
        for num in nums:  
            if num in freq: 
                freq[num] += 1
            else:
                freq[num] = 1
        return max(freq, key=freq.get)  
