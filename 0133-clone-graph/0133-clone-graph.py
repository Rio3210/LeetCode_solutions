"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        
        store={}
        def helper(node):
            if node in store:
                return store[node]
            cp=Node(node.val)
            store[node]=cp
            
            for neighbor in node.neighbors:
                cp.neighbors.append(helper(neighbor))
            return cp
        if node:
            return helper(node)
        else:
            return None