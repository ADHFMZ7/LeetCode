class Solution:
    def canJump(self, nums: List[int]) -> bool:
        nums = list(reversed(nums))
        if len(nums) <= 1:
            return True

        def helper(end):

            if end == len(nums)-1:
                return nums[end] != 0
            
            for step, num in enumerate(nums[end:]):
                if step <= num and step:
                    return helper(end + step)
            return 0
        return helper(0)
