class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        prefix = [nums[0]]
        rev = list(reversed(nums))
        suffix = [nums[0]]
        for i in range(1, length):
            prefix.append(prefix[i-1] * nums[i - 1])
            suffix.append(suffix[i-1] * rev[i - 1])
        for index, value in enumerate(nums):
            nums[index]= prefix[index] * suffix[length - index - 1]    
        return nums    