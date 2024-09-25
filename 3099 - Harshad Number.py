class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        sum=0
        org = x
        while (x!=0):
            r = x%10
            sum = sum+r
            x = x//10
        if org%sum == 0:
            return sum
        else:
            return -1
