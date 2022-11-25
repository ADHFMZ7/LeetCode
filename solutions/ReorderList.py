# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        # finding the middle point
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # reversing the second half  
        middle = slow.next
        slow.next = None
        
        def reverse(head: Optional[ListNode]) -> Optional[ListNode]:
            if not head or not head.next:
                return head

            node = reverse(head.next) 
        
            head.next.next = head 
            head.next = None 
            return node
        
        middle = reverse(middle)
        curr = head
        while middle:
            temp = curr.next
            curr.next = middle
            middle = middle.next
            curr = curr.next
            curr.next = temp
            curr = curr.next

