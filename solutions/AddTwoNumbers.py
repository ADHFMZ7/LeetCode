# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        carry = 0
        dummy = ListNode()
        curr = dummy
        
        while l1 or l2:
            if not l1:
                x = l2.val + carry
                l2 = l2.next
            elif not l2:
                x = l1.val + carry
                l1 = l1.next
            else:     
                x = l1.val + l2.val + carry
                l1 = l1.next
                l2 = l2.next
                
            carry = ceil((x) // 10)
            add = x % 10
            curr.next = ListNode(add)
            curr = curr.next
        if carry > 0:
            curr.next = ListNode(carry)
        
        return dummy.next
