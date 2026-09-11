class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        elements_frequency = dict()
        for i in nums:
            if i not in elements_frequency:
                elements_frequency[i] = 1
            elif elements_frequency[i] + 1 >= len(nums) / 2:
                return i
            else:
                elements_frequency[i] += 1
        return nums[0]