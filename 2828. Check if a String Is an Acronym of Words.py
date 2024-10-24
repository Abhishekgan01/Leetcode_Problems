from typing import List

class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        str1 = ""
        for i in words:
            a = i[0]
            str1 = str1+a
        if str1 == s:
            return True
        else:
            return False