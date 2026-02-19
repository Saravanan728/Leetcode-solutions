class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        sumA=sum(aliceSizes)
        sumB=sum(bobSizes)
        diff=(sumB-sumA)//2
        bobSizes.sort()

        for a in aliceSizes:
            b=a+diff
            low=0
            high=len(bobSizes)-1
            while low<=high:
                mid=(low+high)//2
                if bobSizes[mid]==b:
                    return [a,b]
                elif bobSizes[mid]<b:
                    low=mid+1
                else:
                    high=mid-1

        