class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:

        nums = [1,2,3,4,5,6,7,8,9]
        ans = set()

        def backtrack(i,path,total = 0):

            if len(path)==k and total==n:
                ans.add(tuple(path[:]))
                return
            if len(path)==k:
                return
            if total>=n:
                return
            for j in range(i,len(nums)):
                path.append(nums[j])
                total+=nums[j]
                backtrack(j+1,path,total)
                total-=path.pop()
        backtrack(0,[])
        return ans
        