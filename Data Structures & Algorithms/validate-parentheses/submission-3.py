class Solution:
    def isValid(self, s: str) -> bool:
        opens = ['{', '[','(']
        closes = ['}', ']',')']
        l = list()
        index = 0
        length = len(s)
        if length % 2 != 0:
            return False
        for i in s:
            if i in opens:
                l.append(i)
            elif opens.index(l.pop(-1)) != closes.index(i):
                return False
        return True
            
