class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        symbols = dict()
        maxi = 0
        
        for i in range(len(s)):
            if s[i] in symbols and symbols[s[i]] >= start:
                start = symbols[s[i]] + 1
            
            symbols[s[i]] = i
            maxi = max(maxi, i - start + 1)
            
        return maxi
