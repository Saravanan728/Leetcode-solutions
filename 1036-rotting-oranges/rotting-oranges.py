from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n=len(grid)
        m=len(grid[0])
        q=deque()
        fresh=0
        for i in range(n):
            for j in range(m):
                if grid[i][j]==2:
                    q.append((i,j,0))
                elif grid[i][j]==1:
                    fresh +=1
        drow=[1,0,-1,0]
        dcol=[0,-1,0,1]
        time=0
        rotten_count=0
        while q:
            r,c,t=q.popleft()
            time=max(time,t)
            for k in range(4):
                nr=r+drow[k]
                nc=c+dcol[k]
                if 0<=nr<n and 0<=nc<m and grid[nr][nc]==1:
                    grid[nr][nc]=2
                    rotten_count+=1
                    q.append((nr,nc,t+1))
        if rotten_count != fresh:
            return -1
        return time




        