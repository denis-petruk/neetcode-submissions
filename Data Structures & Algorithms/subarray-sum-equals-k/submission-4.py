class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_counts = {0: 1}
        current_sum = 0
        counter = 0
        for num in nums:

            current_sum += num
            goal = current_sum - k

            if goal in prefix_counts:
                counter += prefix_counts[goal]
                
            prefix_counts[current_sum] = prefix_counts.get(current_sum, 0) + 1
    
        return counter
