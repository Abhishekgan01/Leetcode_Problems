from typing import List

class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        output = []
        for num in nums:
            for digit in str(num):
                output.append(int(digit)) 
        return output
