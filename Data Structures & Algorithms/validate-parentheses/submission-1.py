class Solution:
    def isValid(self, s: str) -> bool:
        opens = ['{', '[','(']
        closes = ['}', ']',')']
        index = 0
        length = len(s)
        if len(s) % 2 != 0:
            return False
        while index < len(s) // 2:
            if opens.index(s[index]) != closes.index(s[len(s) - index - 1]):
                return False
            index += 1
        return True
