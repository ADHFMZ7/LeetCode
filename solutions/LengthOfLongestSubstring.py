class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lo, hi = 0, 0
        chars = set()
        largest = 0
        for i, ch in enumerate(s): 
            if ch not in chars:
                hi = i
            elif ch in chars:
                while ch in chars:   
                    chars.remove(s[lo])
                    lo+=1
            chars.add(ch)            
            largest = max(hi - lo + 1, largest) 
        return largest
            
            
            
            
