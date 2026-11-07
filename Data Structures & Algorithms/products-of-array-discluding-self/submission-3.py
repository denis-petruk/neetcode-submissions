class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        response = { "total": 1 ,"zeros": length}
        for index,value in enumerate(nums):
            if not value and response["zeros"] == length:
                response["zeros"] = index
            else:
                response["total"] = response["total"] * value
        if response["zeros"] != length:
            nums = [0] * length
            nums[response["zeros"]] = response["total"]
        else:
            for index, value in enumerate(nums):
                nums[index] = response["total"] // nums[index]
        return nums

            
