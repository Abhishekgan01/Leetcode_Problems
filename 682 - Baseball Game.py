from typing import List

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        output = []

        for i in operations:
            if i not in ["C", "D", "+"]:
                output.append(int(i))
            elif i == "C" and output:
                output.pop()
            elif i == "D" and output:
                output.append(output[-1] * 2)
            elif i == "+" and output:
                output.append(output[-1] + output[-2])
        
        sum1 =sum(output)

        return sum1