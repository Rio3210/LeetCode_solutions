# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        s1=set()
        temp=head
        while temp:
            if temp in s1:
                return True
            s1.add(temp)
            temp=temp.next
        return False