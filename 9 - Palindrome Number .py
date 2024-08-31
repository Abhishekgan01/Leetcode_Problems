class Solution:
    def isPalindrome(self, x: int) -> bool:
        temp = x
        sum = 0
        
        while x > 0:
            r = x % 10
            sum = (sum * 10) + r
            x = x // 10  
        
        if temp == sum:
            return True 
        else:
            return False  