class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashset = {}
        for i in range(0, len(nums), 1):
            looking = target - nums[i]
            if hashset.get(looking) != None:
                return [hashset[looking], i]
            hashset[nums[i]] = i