class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        
        print(nums2[:n])
        for i in range(n):
            nums1.remove(0)
        nums1.extend(nums2)
        nums1.sort()
        """
        Do not return anything, modify nums1 in-place instead.
        """
        