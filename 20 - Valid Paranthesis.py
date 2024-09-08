class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = {
            "}" : "{",
            "]" : "[",
            ")" : "("
        }

        stack = []
        for i in s:
            if i in hashmap.values():
                stack.append(i)
                #stack = ["("]
            elif i in hashmap.keys():
                if stack == []:
                    return False
                # "(" 
                if stack.pop() != hashmap[i]:
                    return False
        return stack == []
            