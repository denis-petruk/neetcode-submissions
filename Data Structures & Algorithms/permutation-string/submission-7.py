class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_len = len(s1)
        s2_len = len(s2)
        s_long = ""
        s_small = ""
        if s1_len > s2_len:
            s_long = s1
            return False
            s_small = s2
        else:
            s_long = s2
            s_small = s1
        checker = dict()
        char_count = dict()
        left = 0
        for right in range(len(s_long)):
            if sum(checker.values()) < len(s_small):
                checker[s_small[right]] = checker.get(s_small[right], 0) + 1
                char_count[s_long[right]] = char_count.get(s_long[right], 0) + 1
            else:
                if checker.items() == char_count.items():
                    return True
                char_count[s_long[right]] = char_count.get(s_long[right], 0) + 1
                if char_count[s_long[left]] == 1:
                    del char_count[s_long[left]]
                else:
                    char_count[s_long[left]] -= 1
                left += 1
                
        if checker.items() == char_count.items():
            return True     
        else:
            return False        