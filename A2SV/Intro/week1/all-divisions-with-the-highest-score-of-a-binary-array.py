class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:

       
        pref = [0]*(len(nums)+1)
        post = [0]*(len(nums)+1)

        for i in range(len(nums)):

            if nums[i] == 0:
                pref[i+1] = pref[i]+1
            else:
                pref[i+1] = pref[i]

            if nums[len(nums)-i-1] == 1:
                post[len(nums)-i-1] = post[len(nums)-i]+1
            else:
                post[len(nums)-i-1] = post[len(nums)-i]
                
        ans = []

        for i in range(len(nums)+1):

            ans.append(pref[i]+post[i])

        maxi = max(ans)
        ans_arr = [i for i in range(len(ans)) if ans[i]== maxi]

        return ans_arr
        