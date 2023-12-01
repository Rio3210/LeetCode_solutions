# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        
        current = head
        store = []

        while current is not None:
            store.append(current.val)
            current = current.next

        # Perform partitioning
        left_values = [val for val in store if val < x]
        right_values = [val for val in store if val >= x]

        # Create a new linked list using the partitioned values
        new_head = ListNode(0)
        current = new_head

        for val in left_values + right_values:
            current.next = ListNode(val)
            current = current.next

        return new_head.next