class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        goals = dict()
        for i in numbers:
            seek = target - i
            if seek in goals:
                return [goals[seek], i]
            goals[i] = i
