# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        store=[]
        
        current=head
        while current!=None:
            store.append(current.val)
            current=current.next
        temp=store[:left-1] + store[left-1:right][::-1] + store[right:]
        print(temp)
        
        head=ListNode()
        m=head
        n=len(temp)
        for i in range(n):
            m.next=ListNode(temp[i])
            m=m.next
        return head.next