class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1
        s = s.lower()
        while l < r:
            while not self.alphaNum(s[l]) and l<r :
                l+=1
            while not self.alphaNum(s[r]) and r>l:
                r-=1

            if s[l] != s[r]:
                return False
            r-=1
            l+=1
        return True

    def alphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))