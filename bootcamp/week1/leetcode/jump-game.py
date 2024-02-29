class Solution:
    def canJump(self, nums: List[int]) -> bool:
        nums[-1]='G'
        good =  len(nums)-1
        for i in range(len(nums)-2,-1,-1):
            if nums[i]+i>=good:
                nums[i] = 'G'
                good = i
            else:
                nums[i]='B'
        if nums[0]=='G':
            return True
        else:
            False

        