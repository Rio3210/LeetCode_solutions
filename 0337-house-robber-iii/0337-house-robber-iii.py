# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        def helper(root):
            if not root:
                return [0,0]
            left=helper(root.left)
            right=helper(root.right)
            
            maxx1=root.val + left[1] + right[1]
            maxx2=max(left) + max(right)
            return [maxx1,maxx2]
        return max(helper(root))
            
            
       
            
        
        
        