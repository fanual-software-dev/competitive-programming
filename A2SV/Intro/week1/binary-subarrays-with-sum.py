class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:

        ans = {0:1}
        total = 0
        result = 0
        for i in nums:
            total+=i
            diff = total-goal

            if diff in ans:
                result+=ans[diff]
            ans[total] = 1 + ans.get(total,0)
        return result