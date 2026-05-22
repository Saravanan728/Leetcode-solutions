class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        path=[]
        result=[]
        def recursion(index,total):
            

            if total==target:
                result.append(path[:])
                return
            if index==len(candidates) or total>target:
                return
            #take path
            path.append(candidates[index])
            recursion(index,total+candidates[index])

            #Backtrack
            path.pop()

            #not Take
            recursion(index+1,total)
 
        recursion(0,0)
        return result


        