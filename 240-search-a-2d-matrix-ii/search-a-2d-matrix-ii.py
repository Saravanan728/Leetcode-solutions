class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m,n=len(matrix),len(matrix[0])
        for row in matrix:
            if target<row[0] or target>row[-1]:
                    continue
            low=0
            high=n-1
            while low<=high:
                mid=(high+low)//2
            
                if row[mid]==target:
                    return True
                elif row[mid]<target:
                    low=mid+1
                else:
                    high=mid-1
        return False

        