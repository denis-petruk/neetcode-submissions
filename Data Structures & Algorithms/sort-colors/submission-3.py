class Solution:
    def sortColors(self, nums: List[int]) -> None:
        last_red = last_white = last_blue = 0
        for index, value in enumerate(nums):
            if value == 0:
                last_red += 1
                last_white += 1
                last_blue += 1
                nums.insert(last_red - 1, nums.pop(index))
            elif value == 1:
                last_white += 1
                last_blue += 1
                nums.insert(last_white - 1 , nums.pop(index))
            else:
                last_blue += 1
                nums.insert(last_blue - 1, nums.pop(index))               
