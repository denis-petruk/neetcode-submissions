class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        candidate1 = candidate2 = int()
        count1 = count2 = 0
        for i in nums:
            if count1 == 0:
                candidate1 = i
            if count2 == 0 and i != candidate1:
                candidate2 = i
            if i == candidate1:
                count1 += 1
            elif i == candidate2:
                count2 += 1
            else: 
                count1 -= 1
                count2 -= 1
            print((candidate1, count1), (candidate2 , count2))
        res = []
        if nums.count(candidate1) > len(nums) / 3:
            res.append(candidate1)
        if nums.count(candidate2) > len(nums) / 3:
            res.append(candidate2)
        return res
