class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        uniques = dict()
        for i in nums:
            if i not in uniques:
                uniques[i] = 1
            else:
                uniques[i] += 1 
        return sorted(uniques, reverse=True)[:k]