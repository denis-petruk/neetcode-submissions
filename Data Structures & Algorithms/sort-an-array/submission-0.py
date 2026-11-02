class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        length = len(nums)
        if length <= 1:
            return nums
        left = self.sortArray(nums[:length // 2])
        right = self.sortArray(nums[length // 2:])

        return self.merge(left, right)
    def merge(self, left:List[int], right: List[int]) -> List[int]:
        merged = list()
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] > right[j]:
                merged.append(right[j])
                j += 1
            else:
                merged.append(left[i])
                i += 1
        merged.extend(left[i:])
        merged.extend(right[j:])
        return merged
