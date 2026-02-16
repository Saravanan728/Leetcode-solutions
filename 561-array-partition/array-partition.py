class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        ans=0
        i=0
        j=1
        while j<len(nums):
            a=min(nums[i],nums[j])
            ans+=a
            i+=2
            j+=2
        return ans

        