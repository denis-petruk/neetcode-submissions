class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        sorti = sorted(nums)
        response = list()
        point1 = 0
        point2 = point1 + 1
        current = 0
        while point1 < len(sorti) - 1:
            if point2 < len(sorti) - 1:
                point2 += 1
                l = point1 + 1
                r = point2 - 1
                while l < r:
                    if sorti[point1] + sorti[point2] + sorti[l] + sorti[r] == target:
                        if [sorti[point1],sorti[l],sorti[r],sorti[point2]] not in response:
                            response.append([sorti[point1],sorti[l],sorti[r],sorti[point2]])
                        l += 1
                        r -= 1
                    elif sorti[point1] + sorti[point2] + sorti[l] + sorti[r] < target:
                        l += 1
                    else:
                        r -= 1
            else:
                point1 += 1
                point2 = point1 + 1
        return response