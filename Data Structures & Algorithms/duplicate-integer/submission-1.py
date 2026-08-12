class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        county = {}
        for i in nums:
            county[i] = county.get(i, 0) + 1
        for value in county.values():
            if (value > 1):
                return True
        return False