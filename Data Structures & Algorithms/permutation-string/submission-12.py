class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_len = len(s1)
        s2_len = len(s2)
        if s1_len > s2_len:
            return False
        checker = dict()
        char_count = dict()
        left = 0
        for right in range(s2_len):
            if sum(checker.values()) <s1_len:
                checker[s1[right]] = checker.get(s1[right], 0) + 1
                char_count[s2[right]] = char_count.get(s2[right], 0) + 1
            else:
                if checker.items() == char_count.items():
                    return True
                char_count[s2[right]] = char_count.get(s2[right], 0) + 1
                if char_count[s2[left]] == 1:
                    del char_count[s2[left]]
                else:
                    char_count[s2[left]] -= 1
                left += 1
                
        if checker.items() == char_count.items():
            return True     
        else:
            return False        