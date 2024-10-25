from typing import List

class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        max = 0 
        for i in strs:
            # check if we can convert string into integer
            try:
                if int(i)>max:
                    max = int(i)
            # other wise take the length of string
            except:
                if len(i) > max:
                    max = len(i)         
        return max
                