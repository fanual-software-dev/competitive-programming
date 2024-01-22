class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:

        ans = {}

        for i in nums:
            if i in ans:
                print(sum(range(1,len(nums)+1)))
                return [i,sum(range(1,len(nums)+1))-sum(nums)+i] 
            ans[i] = 1+ ans.get(i,0)

        