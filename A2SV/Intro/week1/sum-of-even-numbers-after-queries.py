class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:

        even_sum = 0

        ans_arr = []

        for i in nums:

            if not i%2:
                even_sum += i

        for i in queries:

            if  nums[i[1]]%2 and i[0]%2:

                ans_arr.append(even_sum + nums[i[1]]+i[0])

                even_sum += nums[i[1]] + i[0]

            elif (nums[i[1]]%2 and not i[0]%2):
                ans_arr.append(even_sum)
            elif (not nums[i[1]]%2 and i[0]%2):
                ans_arr.append(even_sum - nums[i[1]])

                even_sum -= nums[i[1]]
            
            elif not nums[i[1]]%2 and not i[0]%2:
                ans_arr.append(even_sum + i[0])

                even_sum += i[0]
            nums [i[1]] = nums[i[1]] + i[0]


        return ans_arr
        