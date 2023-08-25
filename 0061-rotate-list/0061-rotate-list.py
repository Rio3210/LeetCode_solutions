# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if not head or not head.next or k == 0:
            return head
        temp = []
        current = head
        while current:
            temp.append(current.val)
            current = current.next
        
        n = len(temp)
        k = k % n  # Adjust k to the effective number of rotations
        
        if k == 0:
            return head
        
        temp = temp[n-k:] + temp[:n-k]
        new_head = ListNode(temp[0])
        current = new_head
        for i in range(1, n):
            current.next = ListNode(temp[i])
            current = current.next
        
        return new_head
        