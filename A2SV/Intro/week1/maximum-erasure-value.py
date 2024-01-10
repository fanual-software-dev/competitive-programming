class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:

        total = ans = left = 0
        seen = defaultdict(int)
        for right in range(len(nums)):
            seen[nums[right]]+=1
            total+=nums[right]
    
            while left<=right and seen[nums[right]]>1:

                total-=nums[left]
                seen[nums[left]]-=1
                if seen[nums[left]]==0:seen.pop(nums[left])
                left+=1
            ans = max(ans,total)
            
        return ans