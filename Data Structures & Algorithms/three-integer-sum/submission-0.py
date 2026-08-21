from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        answer = []

        for i in range(len(nums) - 2):
            target = -nums[i]
            left = i + 1
            right = len(nums) - 1

            while left < right:
                total = nums[left] + nums[right]

                if total == target:
                    triplet = [nums[i], nums[left], nums[right]]

                    if triplet not in answer:
                        answer.append(triplet)

                    left += 1
                    right -= 1

                elif total < target:
                    left += 1

                else:
                    right -= 1

        return answer
