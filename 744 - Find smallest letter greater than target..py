from typing import List

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        if target >= letters[-1]:
            return letters[0]
        for i in range(len(letters)):
            if target < letters[i]:
                return letters[i]