class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        y = sorted(s)
        z = sorted(t)
        for i in range(len(y)):
            if y[i] != z[i]:
                return z[i]
        return z[-1]
