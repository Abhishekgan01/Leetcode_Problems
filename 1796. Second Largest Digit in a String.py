class Solution:
    def secondHighest(self, s: str) -> int:
        num = set()
        for i in s:
            if i.isdigit():
                num.add(int(i))
        unique = sorted(num, reverse=True)
        
        if len(unique) >= 2:
            return unique[1]
        else:
            return -1
