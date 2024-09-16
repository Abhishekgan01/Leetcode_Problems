from typing import List

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums.sort(reverse = True)
        remove_dup = []
        for i in nums:
            if i not in remove_dup:
                remove_dup.append(i)
        size = len(remove_dup)
        if size < 3 :
            return remove_dup[0]
        else:
            return remove_dup[2]