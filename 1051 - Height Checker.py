from typing import List

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        count = 0
        sorted_heights = sorted(heights)  

        for i in range(len(heights)):
            if heights[i] != sorted_heights[i]: 
                count += 1
        return count
