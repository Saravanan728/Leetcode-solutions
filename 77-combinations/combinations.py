class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        path=[]
        result=[]
        def recursion(start):
            if len(path)==k:
                result.append(path[:])
                return 
            for num in range(start,n+1):
                path.append(num)
                recursion(num+1)
                path.pop()
        recursion(1)
        return result
        