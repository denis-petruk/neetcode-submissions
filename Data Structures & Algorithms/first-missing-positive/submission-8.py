class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        setter = sorted(set(nums))
        if 1 not in setter:
            return 1
        print(setter)
        for i in setter:
            if i + 1 not in setter and i + 1 > 1:
                return i + 1
             