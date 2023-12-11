class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        nums.sort()
        ans = 0

        if len(nums)<=1:

            return len(nums)

        compare = nums[0]

        count = 1

        for i in range(1,len(nums)):

            if nums[i]-1 == compare:

                count+=1
            elif nums[i] == compare:
                continue
            else:

                count = 1

            compare = nums[i]
            ans = max(ans,count)

        return max(ans,count)
        