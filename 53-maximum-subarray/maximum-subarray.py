class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        start=0
        end=0
        s=0
        cur_sum=0
        max_sum=nums[0]
        for i,num in enumerate(nums):
            cur_sum+=num
            if cur_sum>max_sum:
                max_sum=cur_sum
                start=s
                end=i
            if cur_sum<0:
                cur_sum=0
                s=i+1
        return max_sum
