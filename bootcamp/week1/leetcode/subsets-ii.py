class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = set()
        ans.add(tuple([]))
        def backtrack(nums,k,path = []):
            if len(path)==k:
                ans.add(tuple(path[:]))
            for i in range(len(nums)):
                path.append(nums[i])
                backtrack(nums[i+1:],k)
            if path:path.pop()
        for i in range(1,len(nums)+1):
            backtrack(nums,i)
        return ans

        