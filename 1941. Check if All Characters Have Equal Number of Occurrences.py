class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        freq = {}
        for i in s:
            if i not in freq:
                freq[i] = 1
            else:
                freq[i] += 1

        first_freq = list(freq.values())[0] 
        #or
        first_freq = next(iter(freq.values()))

        for count in freq.values():
            if count != first_freq:
                return False
        
        return True
