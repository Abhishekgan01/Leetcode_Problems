from typing import List
class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        result = []
        for word in words:
            for i in words:
                if word in i and word != i: #Not equal 
                    result.append(word)
                    break

        return result