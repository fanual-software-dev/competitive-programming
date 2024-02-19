class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        ans = {}
        stack = []
        result = [-1]*len(nums)
        for num in range(2*len(nums)):
            num = num%len(nums)
            while stack and nums[stack[-1]]<nums[num]:
                result[stack[-1]] = nums[num]
                stack.pop()

            stack.append(num)
        
        return result


        