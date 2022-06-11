#This problem is solved with a time compleity of O(N)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
      d = {}
      sub = 0
      for i, j in enumerate(nums):
        sub = target - j
        if d.get(sub, None) != None:
          return [d.get(sub), i]
        else:
          d[j] = i
        
