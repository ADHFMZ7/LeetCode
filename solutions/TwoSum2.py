class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lo = 0
        hi = len(nums) - 1
        while lo < hi:
            if nums[hi] + nums[lo] > target:
                hi -= 1
            elif nums[hi] + nums[lo] < target:
                lo += 1
            else:
                return [lo+1, hi+1]
        
