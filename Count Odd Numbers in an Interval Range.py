class Solution:
    def countOdds(self, low: int, high: int) -> int:
        oddCount=int(((high-low)/2)+1)
        evenCount=int((high-low)/2)
        if (low%2!=0 and high%2!=0) or (low%2==0 and high%2!=0) or (low%2!=0 and high%2==0):
            return oddCount
        return evenCount
class Solution:
    def countOdds(self, low: int, high: int) -> int:
        oddCount=int(((high-low)/2)+1)
        evenCount=int((high-low)/2)
        if (low%2!=0 and high%2!=0) or (low%2==0 and high%2!=0) or (low%2!=0 and high%2==0):
            return oddCount
        return evenCount
