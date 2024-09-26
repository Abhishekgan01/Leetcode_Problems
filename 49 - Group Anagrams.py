from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = {}
        
        for s in strs:
            sorted_str = ''.join(sorted(s)) 
            if sorted_str in anagram_map:
                anagram_map[sorted_str].append(s)
            else:
                anagram_map[sorted_str] = [s] 

        return list(anagram_map.values())  
  
# strs = ["eat","tea","tan","ate","nat","bat"]
# for i in strs:
#     print(i)

# for s in strs:
#     sorted_str = ''.join(s)
#     print(sorted_str)

# str1 = "eat tea tan ate nat"
# x = str1.split()
# print(x)  