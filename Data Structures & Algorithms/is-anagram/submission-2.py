class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        containers = {}
        containert = {}
        for i in range(0, len(s), 1):
            containers[s[i]] = containers.get(s[i], 0) + 1
            containert[t[i]] = containert.get(t[i], 0) + 1
            
        return containers == containert