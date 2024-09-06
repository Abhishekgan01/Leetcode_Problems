from typing import List

class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        sol = []
        if len(original) == m*n:
            for i in range(0,len(original),n):
                sol.append(original[i:i+n])
            return sol

