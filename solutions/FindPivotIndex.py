class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        rightsum = sum(nums[1::])     
        leftsum = 0
        for i in range(len(nums)):
            if i != 0:
                rightsum -= nums[i]
                leftsum += nums[i-1]
            if rightsum == leftsum:
                return i
        return -1
            
