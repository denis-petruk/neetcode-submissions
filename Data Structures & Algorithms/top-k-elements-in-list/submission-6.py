class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        uniques = dict()
        length = len(nums)
        for i in nums:
            if i not in uniques:
                uniques[i] = 1
            else:
                uniques[i] += 1 
        for i in sorted(uniques.items(), key=lambda x: x[1],reverse=True)[:k]:
            nums.append(i[0])
        return nums[length:]