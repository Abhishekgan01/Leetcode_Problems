from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        """
        if k=2
        Eg:1 2 3 4 5
        1st:5 4 3 2 1
        2nd:4 5 3 2 1
        3rd:4 5 1 2 3
        """

        #To reverse the total array
        k = k % len(nums)
        l,r = 0, len(nums)-1
        while l<r:
         nums[l], nums[r] = nums[r], nums[l]
         l,r = l+1, r-1

        #To reverse k elements
        l,r = 0, k-1
        while l<r:
         nums[l], nums[r] = nums[r], nums[l]
         l,r = l+1, r-1

        #To reverse remaining elements
        l,r = k, len(nums)-1
        while l<r:
         nums[l], nums[r] = nums[r], nums[l]
         l,r = l+1, r-1