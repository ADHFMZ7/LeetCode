class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.q = list(reversed(sorted(nums)))
        self.k = k
        
    def add(self, val: int) -> int:
        self.q.append(val) 
        self.q = list(reversed(sorted(self.q)))
        return self.q[self.k-1]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
