class Solution:
    def reverseWords(self, s: str) -> str:
       r = []
       k = s.split()
       for i in k:
        word = i[::-1]
        r.append(word)
       return " ".join(r)
