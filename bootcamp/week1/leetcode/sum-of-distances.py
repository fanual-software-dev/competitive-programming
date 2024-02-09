class Solution:
    def distance(self, nums: List[int]) -> List[int]:

        seen = defaultdict(list)
        ans = [0]*len(nums)
        for i in range(len(nums)):
            seen[nums[i]].append(i)
        for i in seen:
            if len(seen[i])>1:
                presum = [0]*(len(seen[i])+1)
                for k in range(len(seen[i])):
                    presum[k+1] = seen[i][k] + presum[k]
                for j in range(len(seen[i])):
                    ans[seen[i][j]] = (seen[i][j])*j-presum[j]+ presum[-1]-presum[j+1]-(seen[i][j])*(len(seen[i])-j-1)

            else:
                ans[seen[i][0]] = 0
        return ans


        