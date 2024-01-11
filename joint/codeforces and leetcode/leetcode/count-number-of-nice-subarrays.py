class Solution(object):
    def numberOfSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        ans = count = total = curr = 0
        left=[]
        right = 0
        while right <len(nums):
            if nums[right]%2!=0:
                count+=1
                left.append(total)
                total=0
            else:
                total+=1
            if count==k:
                ans+=left[curr]+1
            if count>k:
                curr+=1
                count-=1
                ans+=left[curr]+1


            right+=1
        return ans
                
