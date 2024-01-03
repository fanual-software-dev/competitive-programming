class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:

        nums.sort()
        ans = 0

        for right in range(1,len(nums)):

            if nums[right-1]+nums[right]<target:
                ans+=right
            else:
                left = right-2
                while left>=0:

                    if nums[left]+nums[right]<target:
                        ans+=1
                    left-=1
            
        return ans
     