class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique = list()
        current = 0
        length = len(nums)
        while current < length:
            if nums[current] in unique:
                nums.pop(current)
                length -= 1
            else:
                unique.append(nums[current])
                current +=1
        return length
        