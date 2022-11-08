# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        s1={}
        temp=head
        while temp:
            if temp in s1:
                return temp
            s1[temp]=0
            temp=temp.next
        return None