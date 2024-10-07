from typing import List

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s3 = s1 + " " + s2
        s4 = s3.split()
        output = {}
        for i in s4:
            if i in output:
                output[i] += 1
            else:
                output[i] = 1

        result = []
        for i,j in output.items():
            if j == 1:
                result.append(i)

        return result