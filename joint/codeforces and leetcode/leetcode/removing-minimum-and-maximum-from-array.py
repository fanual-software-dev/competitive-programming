class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        minimum = nums[0]
        maximum  = nums[0]
        n = len(nums)
        left = 0
        right = 0

        for i in range(len(nums)):
            if nums[i]<minimum:
                left = i
                minimum = nums[i]
            elif nums[i]>maximum:
                right = i
                maximum = nums[i]
        return min(min(right,left) + 1 + n - max(right,left), n-min(right,left) + 1 + max(right,left),n-min(right,left),max(right,left)+1)

        