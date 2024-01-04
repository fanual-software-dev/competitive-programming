class Solution(object):
        def threeSum(self, nums):
            nums=sorted(nums)
            compare=set()
            answer=[]
            for i in range(len(nums)):
                right=len(nums)-1
                left=i+1
                while left<right:
                    if nums[left]+nums[right]+nums[i]==0:
                        if (nums[i],nums[left],nums[right]) not in compare:
                            answer.append([nums[i],nums[left],nums[right]])
                            compare.add((nums[i],nums[left],nums[right]))
                            left+=1
                            right-=1
                        else:
                            left+=1
                            right-=1

                    elif nums[left]+nums[right]+nums[i]>0:
                        right-=1
                    elif nums[left]+nums[right]+nums[i]<0:
                        left+=1
            return answer