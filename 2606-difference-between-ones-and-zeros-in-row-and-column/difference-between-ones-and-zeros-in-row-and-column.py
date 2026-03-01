class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        n=len(grid)
        m=len(grid[0])
        onesrow=[0]*n
        onescol=[0]*m
        for i in range(n):
            for j in range(m):
                if grid[i][j]==1:
                    onesrow[i]+=1
                    onescol[j]+=1
        diff =[[0]*m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                diff[i][j]=2*onesrow[i]+2*onescol[j]-m-n
        return diff
        