import string
from typing import List

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = paragraph.lower()
        for char in string.punctuation:
            paragraph = paragraph.replace(char, ' ')
        modified = paragraph.split()
        
        output = {}
        for word in modified:
            if word not in banned:
                if word not in output:
                    output[word] = 1
                else:
                    output[word] += 1
        
        return max(output, key=output.get)