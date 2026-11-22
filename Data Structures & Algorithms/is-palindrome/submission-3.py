class Solution:
    def isPalindrome(self, s: str) -> bool:
        start = 0
        end = len(s)-1
        while start<end:
            if self.alphaNum(s[start]) and self.alphaNum(s[end]):
                if s[start].lower() != s[end].lower():
                    return False
                if s[start].lower() == s[end].lower():
                    start += 1
                    end -= 1
            if not self.alphaNum(s[start]):
                start += 1
            if not self.alphaNum(s[end]):
                end -= 1
        return True
        

    def alphaNum(self, s: str):
        return (
            ord('A') <= ord(s) <= ord('Z') or
            ord('a') <= ord(s) <= ord('z') or
            ord('0') <= ord(s) <= ord('9')
        )




        
