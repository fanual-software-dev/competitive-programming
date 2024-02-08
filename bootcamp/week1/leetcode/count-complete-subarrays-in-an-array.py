class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        leng = len(set(nums))
        ans = 0
        seen = defaultdict(int)
        left = 0
        for right in range(len(nums)):
            seen[nums[right]]+=1
            while len(seen)==leng:
                ans+=len(nums)-right
                seen[nums[left]]-=1
                if seen[nums[left]]==0:
                    seen.pop(nums[left])
                left+=1
            
        return ans