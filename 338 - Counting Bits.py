from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:
        # decimal  binary  val
        #   0       0       0
        #   1       1       1
        #   2       10      1
        #   3       11      2
        #   4       100     1
        #  even: 2=10, 4=100, 6=110, 8=1000, 10=1010; x/2
        #  odd:  1=01, 3=011, 5=101, 7=0111, 9=1001; x/2 + 1
        counter = [0]
        for i in range(1,n+1):
            counter.append(counter[i>>1] + i%2)
        return counter