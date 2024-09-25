from typing import List

class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        contains = []
        for i,j in enumerate(words):
            if x in j:
                contains.append(i)
        return contains