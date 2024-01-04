class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        total = (sum(nums[:k]))
        ans = total
        left = 0
        
        for right in range(k,len(nums)):

            total-=nums[left]
            total+=nums[right]
            left+=1
            ans = max(ans,total)
        return ans/k