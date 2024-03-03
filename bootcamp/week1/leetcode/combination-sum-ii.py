class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates.sort()
        def backtrack(i,path,total = 0):
            if total==target:
                
                ans.append(path[:])
                return
            if total>target:
                return
            
        
            for j in range(i,len(candidates)):
                if j>i and candidates[j]==candidates[j-1]:
                    continue 
                path.append(candidates[j])
                backtrack(j+1,path,total+candidates[j])
                path.pop()

        backtrack(0,[])
        return ans