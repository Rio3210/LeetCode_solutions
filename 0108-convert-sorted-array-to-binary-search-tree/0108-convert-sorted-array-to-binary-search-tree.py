# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def helper(nums,left,right):
            if left>right:
                return None
            mid=(left+right)//2
            root=TreeNode(nums[mid])
            root.left=helper(nums,left,mid-1)
            root.right=helper(nums,mid+1,right)
            return root
        return None if len(nums)==0 else helper(nums,0,len(nums)-1)
                
        # if not nums:
        #     return None
        # mid=len(nums)//2
        # root=TreeNode(nums[mid])
        # root.left=self.sortedArrayToBST(nums[:mid])
        # root.right=self.sortedArrayToBST(nums[mid+1:])
        # return root