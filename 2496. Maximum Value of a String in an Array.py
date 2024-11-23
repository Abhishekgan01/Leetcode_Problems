from typing import List

class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        max_value = 0  
        for s in strs:
            if s.isdigit():
                value = int(s)
            else:
                value = len(s)
            if value > max_value:
                max_value = value
                
        return max_value 