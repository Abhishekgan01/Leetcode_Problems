#Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
#Output: [1,2,2,3,5,6]

nums1 = [1, 2, 3, 0, 0, 0]
nums2 = [2, 5, 6]

# Remove zeros from nums1
nums1 = [i for i in nums1 if i != 0]

# Merge nums1 and nums2
nums1.extend(nums2)

# Sort the merged list
nums1 = sorted(nums1)

print(nums1)
