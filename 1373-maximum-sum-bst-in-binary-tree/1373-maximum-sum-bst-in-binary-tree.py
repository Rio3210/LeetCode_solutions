# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        max_sum=0
        def dfs(root):
            nonlocal max_sum
            if not root:
                 return True, inf, -inf, 0
            is_l, min_l, max_l, sum_l = dfs(root.left)
            is_r, min_r, max_r, sum_r = dfs(root.right)
            
            if is_l and is_r and max_l < root.val < min_r:
                cur = sum_l + sum_r + root.val
                max_sum = max(cur, max_sum)
                min_l = min(min_l, root.val)
                max_r = max(max_r, root.val)
                return 1, min_l, max_r, cur
            else:
                return False, 0, 0, 0
                
        dfs(root)
        return max_sum