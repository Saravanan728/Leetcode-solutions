class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        low=0
        high=len(letters)-1
        ans=None
        while low<=high:
            mid=(low+high)//2
            if letters[mid]>target:
                ans=letters[mid]
                high=mid-1
            else:
                low=mid+1
        return ans if ans is not None else letters[0]