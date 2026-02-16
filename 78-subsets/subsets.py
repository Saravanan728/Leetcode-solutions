class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        n=len(nums)
        for num in range(1<<n):
            subset=[]
            for i in range(n):
                if num &(1<<i):
                    subset.append(nums[i])
            res.append(subset)
        return res
        