class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        total = 0
        ans = -float('inf')

        for right in nums:
            total+=right
            ans = max(ans,total)
            if total<0:
                total=0
        return ans
        