class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        res = 0
        for i in range(len(nums)):
            res += nums[i]
            nums[i] = res
        return nums
