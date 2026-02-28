class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        nums.sort()
        ans=set()
        l=0
        r=len(nums)-1
        while l<r:
            mid=(nums[l]+nums[r])/2
            ans.add(mid)
            l+=1
            r-=1
        return len(ans)
        