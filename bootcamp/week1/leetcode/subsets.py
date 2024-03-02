class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def backtrack(candidates,k,path = []):
            if len(path)==k:
                ans.append(path[:])
            for i in range(len(candidates)):
                path.append(candidates[i])
                backtrack(candidates[i+1:],k)
            if path:path.pop()
        for i in range(1,len(nums)+1):
            backtrack(nums,i)
        return ans+[[]]
        