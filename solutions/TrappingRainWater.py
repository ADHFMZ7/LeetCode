class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = height[0], max(height)
        result = 0
        for i, h in enumerate(height):
            if r == h and i != len(height)-1:
                r = max(height[i+1:])
            if h <= min(l, r):
                result += min(l, r) - h
            l = max(l, h)
        return result
