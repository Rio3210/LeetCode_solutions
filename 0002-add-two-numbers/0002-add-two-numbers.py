# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head=l3=ListNode(0)
        temp=0
        while l1 or l2 or temp:
            if l1:
                temp+=l1.val
                l1=l1.next
            if l2:
                temp+=l2.val
                l2=l2.next
            l3.val=temp%10
            temp=temp//10
            if l1 or l2 or temp:
                l3.next=ListNode(0)
                l3=l3.next
        return head