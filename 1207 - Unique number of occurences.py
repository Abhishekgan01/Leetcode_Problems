from typing import List

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dict={}
        for i in arr:
            if i in dict:
                dict[i] += 1
            else:
                dict[i] = 1

        setx = set(dict.values())
        if len(dict) == len(setx):
            return True
        else:
            return False