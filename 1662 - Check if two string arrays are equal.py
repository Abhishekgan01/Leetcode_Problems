from typing import List

class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        joined1 = ''.join(word1)
        joined2 = ''.join(word2)
        if joined1 == joined2:
            return True
        else:
            return False