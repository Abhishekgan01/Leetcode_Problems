from typing import List 
class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        freq = {}
        for i in range(len(names)):
            freq[heights[i]] = names[i]
        b = list(freq.keys())
        b.sort(reverse = True)

        sd = {i:freq[i] for i in b}
        final = []
        for i,j in sd.items():
            final.append(j)
        return finalgit 