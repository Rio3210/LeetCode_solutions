# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue=[]
        queue.append(root)
        ans=[]
        while queue:
            lenn=len(queue)
            store=[]
            for i in range(lenn):
                node=queue.pop(0)
                store.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ans.append(store)
        n=len(ans)
        for i in range(n):
            if i%2!=0:
                ans[i]=ans[i][::-1]
        return ans