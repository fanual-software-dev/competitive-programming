class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        list=[]
        count=0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i==j:
                    continue
                else:
                    if nums[i]>nums[j]:
                        count+=1
            list.append(count)
            count=0
        return list
