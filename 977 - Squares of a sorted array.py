from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ans =[]
        l,r = 0, len(nums)-1
        while l<r:
            left, right = abs(nums[l]), abs(nums[r])
            if left > right:
                #2.[16,100]
                ans.insert(0, left**2)
                l+=1
            else:
                #1.[100]
                ans.insert(0, right**2)
                r-=1
