from typing import List
import itertools
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ele = itertools.permutations(nums)
        list_ele = []
        for i in ele:
            list_ele.append(i)
        return list_ele

# a = [1,2,3]
# b = list(itertools.permutations(a))
# lists = []
# for i in b:
#     lists.append(list(i))
# print(lists)
