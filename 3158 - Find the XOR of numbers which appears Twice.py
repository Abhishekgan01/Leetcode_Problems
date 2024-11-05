from typing import List

class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        count = {}
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        
        duplicates_xor = 0
        for num, freq in count.items():
            if freq == 2:
                duplicates_xor ^= num
        
        return duplicates_xor