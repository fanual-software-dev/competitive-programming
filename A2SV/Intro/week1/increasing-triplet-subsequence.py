class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:

        ans = []

        for num in nums:

            index = bisect_left(ans,num)

            if index<len(ans):

                ans[index] = num
            else:
                ans.append(num)
            if len(ans)>2:
                return True
        return False
        