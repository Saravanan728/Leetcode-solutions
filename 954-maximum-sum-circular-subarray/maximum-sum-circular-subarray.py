class Solution:
    def maxSubarraySumCircular(self, nums):
        total_sum = 0
        max_sum = nums[0]
        cur_max = 0
        
        min_sum = nums[0]
        cur_min = 0
        
        for num in nums:
            # Kadane max
            cur_max = max(num, cur_max + num)
            max_sum = max(max_sum, cur_max)
            
            # Kadane min
            cur_min = min(num, cur_min + num)
            min_sum = min(min_sum, cur_min)
            
            total_sum += num
        
        # Edge case: all negative
        if max_sum < 0:
            return max_sum
        
        return max(max_sum, total_sum - min_sum)