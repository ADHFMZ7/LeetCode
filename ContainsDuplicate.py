class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
      li = set()
      for i in nums:
        if i in li:
          return True
        li.add(i)
      return False
