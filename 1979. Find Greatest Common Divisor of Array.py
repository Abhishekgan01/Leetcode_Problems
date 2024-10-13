from typing import List
import numpy as np

class Solution:
    def findGCD(self, nums: List[int]) -> int:
        nums.sort()
        gcd_num = np.gcd(nums[0], nums[-1])
        return gcd_num