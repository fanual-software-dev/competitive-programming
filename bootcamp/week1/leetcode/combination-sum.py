class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        def backtrack(j,path,total = 0):

            if total==target:
                ans.append(path[:])
            if total>target:
                return
            for i in range(j,len(candidates)):

                path.append(candidates[i])
                total+=path[-1]
                backtrack(i,path,total)
                total-=path.pop()
        backtrack(0,[])
        return ans
                