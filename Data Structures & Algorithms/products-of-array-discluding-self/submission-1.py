class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        response = { "total": 1 ,"zeros": list()}
        for index,value in enumerate(nums):
            if value != 0:
                response["total"] = response["total"] * value
            else:
                response["zeros"].append(index)
        if response["zeros"]:
            for index, value in enumerate(nums):
                nums[index] = 0
                if index in response["zeros"]:
                    nums[index] = response["total"]
        else:
            for index, value in enumerate(nums):
                nums[index] = response["total"] // nums[index]
        return nums

            
