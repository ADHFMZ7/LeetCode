class Solution:
    def numPairsDivisibleBy60(self, time: list[int]) -> int:
        d = [0]*60
        result = 0
        for i in time:
            duration = i % 60
            nduration = duration if duration else 60
            result += d[60-nduration]     
            d[duration] += 1
        return result