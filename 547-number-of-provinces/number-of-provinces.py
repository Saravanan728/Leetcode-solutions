
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n=len(isConnected)
        visited=[0]*n
        count=0
        def dfs(i):
            visited[i]=1
            for m in range(n):
                if isConnected[i][m]==1 and visited[m]==0:
                    dfs(m)
        for i in range(n):
            if visited[i]==0 :
                count+=1
                dfs(i)
        return count
        

        