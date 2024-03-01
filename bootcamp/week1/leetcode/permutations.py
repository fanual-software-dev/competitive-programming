class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        leng = len(nums)
        def backtrack(n,k,path = []):

            if len(path)==k:
                ans.append(path[:])
    
            for i in range(len(n)):
                path.append(n[i])
                new = n[:i]+n[i+1:]
                backtrack(new,k)
            if path:path.pop()
        backtrack(nums,leng)
        return ans