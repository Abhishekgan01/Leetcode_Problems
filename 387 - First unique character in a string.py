class Solution:
    def firstUniqChar(self, s: str) -> int:
        dicts = {}
        for i in s:
            if i in dicts:
                dicts[i] += 1
            else:
                dicts[i] = 1

        key = None
        for i, j in dicts.items():
            if j == 1:
                key = i
                break

        if key is None:
            return -1

        for k in range(len(s)):