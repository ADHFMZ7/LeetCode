class Solution:
    def isPalindrome(self, s: str) -> bool:
      s = s.lower()
      l = 0
      r = len(s)-1
      while l < r:
        while not isa(s[l]) and l < r:
          l += 1
        while not isa(s[r]) and l < r:
          r -= 1
        if s[l] != s[r]:
          return False
        l += 1
        r -= 1
      return True
    
def isalphabetic(c):
  num = ord(c)
  if (num >= 48 and num <= 57) or (num >= 97 and num <= 122):
    return True
  return False
