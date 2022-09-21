class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = set()
        nums.sort()
        for i, num in enumerate(nums):
            if i > 0 and nums[i-1] == num:
                continue
            l, r = i+1, len(nums)-1
            target = -num
            while l < r:
                if nums[l] + nums[r] == target:
                    result.add(tuple([num, nums[l], nums[r]]))
                    l += 1
                elif nums[l] + nums[r] > target:
                    r -= 1
                else:
                    l += 1
        return result
                
