class Solution:
    def validPalindrome(self, s: str) -> bool:
        deletes = 0
        left = 0
        right = len(s) - 1
        while left < right:
            if s[left] != s[right]:
                deletes += 1
                if s[left + 1] == s[right]:
                    left += 1
                if s[left] == s[right - 1]:
                    right -= 1
            if deletes > 1:
                return False
            left, right = left + 1, right - 1
        return True
            