class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        seen = {0:1}
        total = 0
        ans = 0

        for i in nums:
            total+=i
            diff = total-k
            if diff in seen:
                ans+=seen[diff]
            seen[total] = 1 + seen.get(total,0)
        return ans


        