class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        ans = nums[0]
        
        maxcount = 1

        for i in range(1,len(nums)):

            if ans == nums[i]:

               maxcount+=1
            else:

                maxcount-=1

                if maxcount == 0:

                    ans = nums[i]
                    maxcount = 1

           
           
        return ans
        