from typing import List

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i in nums:
            ind = abs(i) - 1
            nums[ind] = -abs(nums[ind])
        return [index+1 for index,number in enumerate(nums) if number>0]
    
#2nd method
# class Solution:
#     def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
#         d = {}
#         for i in range(1, len(nums)+1):  
#             d[i] = 0
#         for i in nums:
#             d[i] += 1
#         result = []
#         for key, val in d.items():
#             if val == 0:
#                 result.append(key)
#         return result