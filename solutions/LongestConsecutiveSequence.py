class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        res = 0
        for i in nums:
            if i-1 not in s:
                temp = 0
                while i + temp in s:
                    temp += 1
                res = max(temp, res)
        return res
