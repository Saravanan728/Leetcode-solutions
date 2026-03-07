from collections import deque
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph=[[]for _ in range(numCourses)]
        indegree=[0]*numCourses
        for a,b in prerequisites:
            graph[b].append(a)
            indegree[a]+=1

          
        q=deque()
        for i in range(numCourses):
            if indegree[i]==0:
                q.append(i)
        topo=[]
        while q:
            node=q.popleft()
            topo.append(node)
            for nei in graph[node]:
                indegree[nei]-=1
                if indegree[nei]==0:
                    q.append(nei)
        return len(topo) == numCourses
            


        