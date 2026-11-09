class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        candidate1 = candidate2 = None
        count1 = count2 = 0
        
        for i in nums:
            if i == candidate1:
                count1 += 1
            elif i == candidate2:
                count2 += 1
            elif count1 == 0:
                candidate1 = i
                count1 = 1
            elif count2 == 0:
                candidate2 = i
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1
        
        res = []
        for candidate in set([candidate1, candidate2]):
            if candidate is not None and nums.count(candidate) > len(nums) // 3:
                res.append(candidate)
                
        return res
