class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        ans=float('inf')
        for i in range(len(nums1)):
            low=0
            high=len(nums2)-1
            while low<=high:
                mid=(low+high)//2
                if nums1[i]==nums2[mid]:
                    ans=min(ans,nums2[mid])
                    break
                elif nums1[i]<nums2[mid]:
                    high=mid-1  
                else:
                    low=mid+1
                    
        return ans if ans != float('inf') else -1
        