class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
      if not head:
        return False
      s = set()
      curr = head
      while curr.next:
        if curr in s:
          return True
        s.add(curr)
        curr = curr.next
      return False
