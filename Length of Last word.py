class Solution(object):
    def lengthOfLastWord(self, s):
        length=s.split()
        return len(length[-1])
