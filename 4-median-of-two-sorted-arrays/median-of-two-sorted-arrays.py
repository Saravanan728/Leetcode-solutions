class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        num = nums1 + nums2
        num.sort()
        l=0
        r=len(num)-1
        mid=(l+r)//2
        if len(num)%2==0:
            median=(num[mid+1]+ num[mid])/2.0
            return median
        else:
            median=num[mid]
            return median