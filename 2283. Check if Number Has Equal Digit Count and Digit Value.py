class Solution:
    def digitCount(self, num: str) -> bool:
        a =''
        for i in range(len(num)):
            a += str(num.count(str(i)))
        return a == num