class Solution:
    def sortColors(self, nums: List[int]) -> None:
        length = len(nums)
        last_red = last_white = last_blue = 0
        for index, value in enumerate(nums):
            if value == 0:
                nums.insert(last_red, nums.pop(index))
                last_red += 1
                last_white += last_red
                last_blue += last_white
            elif value == 1:
                nums.insert(last_white, nums.pop(index))
                last_white += 1
                last_blue += last_white
            else:
                nums.insert(last_blue, nums.pop(index)) 
                last_blue += 1
              
