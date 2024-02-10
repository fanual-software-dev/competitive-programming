class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        for i in range(len(nums)):
            if nums[i]%2:
                nums[i]=1
            else:
                nums[i]=0
        ans = 0
        total = 0
        hashmap={0:1}
        left=0
        for num in nums:
            total+=num
            diff = total-k
            ans+=hashmap.get(diff,0)
            hashmap[total] = 1 + hashmap.get(total,0)
            
        return ans