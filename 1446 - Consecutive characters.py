class Solution:
    def maxPower(self, s: str) -> int:
        c  = m = 0
        if len(s) < 3:
            return len(s)
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                c += 1
            else:
                c = 1
            m = max(c, m)
        return m