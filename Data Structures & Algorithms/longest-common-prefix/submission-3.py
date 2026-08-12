class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        shortest = min(strs, key=len)

        for i in range(len(shortest), -1, -1):
            prefix = shortest[:i]

            if all(word.startswith(prefix) for word in strs):
                return prefix

        return ""
