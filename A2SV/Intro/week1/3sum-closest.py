class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        ans = float('inf')
        tar=0
        nums.sort()
        
        for i in range(len(nums)-2):
            right=len(nums)-1
            left=i+1
            

            while left<right:
                total=nums[i]
                total+=nums[left]+nums[right]
                if abs(total-target)<ans:
                    tar=total
                    ans=abs(total-target)
                if total<=target:
                    
                    left+=1
                else:
                    
                    right-=1
                
                

        return tar