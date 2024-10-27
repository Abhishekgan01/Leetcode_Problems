class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        mn = min(a, b)
        ans = []

        for i in range(1, mn+1):
            if a % i == 0 and b % i == 0:
                ans.append(i)
        return len(ans)