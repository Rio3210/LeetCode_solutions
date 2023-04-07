# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        counter = defaultdict(int)
        counter[0]=1
        # print(counter)
        self.res = 0
        def helper(root, cursum):
            if not root:
                return
            cursum += root.val
            self.res += counter[cursum-targetSum]
            counter[cursum] += 1
            helper(root.left, cursum)
            helper(root.right, cursum)
            counter[cursum] -= 1
        helper(root, 0)
        return self.res
    
    
                
