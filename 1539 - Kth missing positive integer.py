from typing import List

class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        missing = []
        for i in range(1, arr[-1] + k + 1):  
            if i not in arr:
                missing.append(i)
            if len(missing) == k:  
                return missing[-1] 
        return missing[k - 1]  

