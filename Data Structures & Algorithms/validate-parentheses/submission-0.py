class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 0:
            if s[len(s)//2] != s[len(s) // 2+1: -1]:
                return True
            return False
        return False