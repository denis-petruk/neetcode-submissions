class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        midx = 0
        for i in range(k):
            if nums[i] >= nums[midx]:
                midx = i
        res = [nums[midx]]
        for i in range(k, len(nums)):
            if nums[i] >= nums[midx]:
                midx = i
            if i - k == midx:
                midx = i - k + 1
                for j in range(midx+1, i+1):
                    if nums[j] >= nums[midx]:
                        midx = j
            res.append(nums[midx])
        return res