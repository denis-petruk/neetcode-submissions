class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        checker = set(nums)
        maximum = 0
        for i in nums:
            if (i-1) not in checker:
                length = 0
                while (i + length) in checker:
                    length += 1
                maximum = max(maximum,length)
        return maximum
