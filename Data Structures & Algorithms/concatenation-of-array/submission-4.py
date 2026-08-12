class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        length = len(nums)
        ans = []
        for i in range(0,length,1):
            ans.insert(i,nums[i])
            ans.insert(i+length,nums[i])
        return ans