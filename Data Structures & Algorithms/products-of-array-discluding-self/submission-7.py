class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        
        prefix = [1]
        suffix = [1]
        
        rev = list(reversed(nums))
        
        for i in range(1, length):
            prefix.append(prefix[i-1] * nums[i - 1])
            suffix.append(suffix[i-1] * rev[i - 1])
            
        suffix.reverse()
            
        for index in range(length):
            nums[index] = prefix[index] * suffix[index]
            
        return nums
