from typing import List

class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        common = []
        output = []

        #common elements from nums1 that exist in nums2
        for i in nums1:
            if i in nums2:
                common.append(i)

        #If there are no common elements, return [0, 0]
        if len(common) == 0:
            return [0, 0]

        #Count how many elements in nums1 exist in nums2 (answer1)
        answer1 = len(common)

        # Count how many elements in nums2 exist in nums1 (answer2)
        answer2 = 0
        for i in nums2:
            if i in nums1:
                answer2 += 1

        # Return the result as [answer1, answer2]
        return [answer1, answer2]
