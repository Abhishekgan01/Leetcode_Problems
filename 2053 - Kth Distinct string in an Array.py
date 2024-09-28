class Solution(object):
    def kthDistinct(self, arr, k):
        count = {}
        for i in arr:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1
        temp = []
        for i in arr:
            if count[i] == 1:
                temp.append(i)
        if len(temp) < k:
            return ""
        else:
            return temp[k-1]
        
obj=Solution()
arr=["a","a","b","b","c"]   
k=2
print((obj.kthDistinct(arr,1)))    
            