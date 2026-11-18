
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n = len(s)
        m = len(t)

        if m > n or m == 0:
            return ""

        t_counter = {}
        current_counter = {}

        for char in t:
            t_counter[char] = t_counter.get(char, 0) + 1

        required = len(t_counter)
        formed = 0

        left = 0
        min_left = 0
        min_length = float("inf")

        for right in range(n):
            char = s[right]

            if char in t_counter:
                current_counter[char] = current_counter.get(char, 0) + 1

                if current_counter[char] == t_counter[char]:
                    formed += 1

            while formed == required:
                window_length = right - left + 1

                if window_length < min_length:
                    min_length = window_length
                    min_left = left

                left_char = s[left]

                if left_char in t_counter:
                    current_counter[left_char] -= 1

                    if current_counter[left_char] < t_counter[left_char]:
                        formed -= 1

                left += 1

        if min_length == float("inf"):
            return ""

        return s[min_left:min_left + min_length]
