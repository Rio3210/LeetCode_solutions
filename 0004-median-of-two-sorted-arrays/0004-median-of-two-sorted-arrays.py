class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        nums1.extend(nums2)
        nums1.sort()
        l = len(nums1)
        mid1 = l // 2
        if l % 2 == 1:
            return nums1[mid1]
        else:
            mid2 = (l // 2) -1
            return (nums1[mid1] + nums1[mid2])/2
        