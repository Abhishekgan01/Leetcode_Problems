from typing import List

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        length = len(words)
        for i in words:
            for j in i:
                if j not in allowed:
                    length-=1
                    break
        return length

