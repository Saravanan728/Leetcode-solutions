class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_product=nums[0]
        cur_max=nums[0]
        cur_min=nums[0]

        for i in range(1,len(nums)):
            num=nums[i]
            tamp=max(num,cur_max*num,cur_min*num)
            cur_min=min(num,cur_max*num,cur_min*num)
            cur_max=tamp
            max_product=max(cur_max,max_product)
        return max_product
        