class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        nums.sort()
        l=0
        r=len(nums)-1
        ans=[]
        while l<r:
            mid=(float(nums[l]+nums[r])/2)
            ans.append(mid)
            l+=1
            r-=1
        return min(ans)

        