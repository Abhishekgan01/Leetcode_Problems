from typing import List

class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        freq ={}
        sum = 0
        for i in nums:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
        
        for i,j in freq.items():
            if j==1:
                sum+=i

        if sum!=0:
            return sum
        else:
            return 0