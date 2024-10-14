nums = [-4,-2,1,4,8]
nums1 = []
for i in nums:
    nums1.append(abs(i))
nums1.sort()
print(nums1)
for i in range(len(nums1)):
    if i > 0:
        