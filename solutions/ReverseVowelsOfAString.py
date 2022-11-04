class Solution:
    def reverseVowels(self, s: str) -> str:
        a = []
        s = list(s)
        for i, letter in enumerate(s):      
            if letter in "aeiouAEIOU":
                a.append(letter)
                s[i] = ''
        for i, letter in enumerate(s):
            if not letter:
                s[i] = a.pop()
        return ''.join(s)
        
